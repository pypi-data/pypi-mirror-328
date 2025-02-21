import asyncio
import aiohttp
import random
import os
from utils.logger import log_info, log_warning, log_error
from utils.response_handler import handle_response_analysis
from utils.request_handler import prepare_request_headers
from colorama import Fore, Style


# Load user agents from a file for rotating requests
def load_user_agents(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        log_error(f"User agents file not found: {file_path}")
        return []

# Perform asynchronous injection of payloads into URL and Header parameters
async def inject_payload(session, url, payload, headers, vulnerability_type="SQLi"):
    try:
        # Add payload to URL parameters or header as required
        modified_url = url
        if "?" in url:
            # Inject payload into URL parameters
            modified_url = f"{url}&{payload}"
        else:
            # If URL doesn't have parameters, assume header injection
            headers = prepare_request_headers(headers, payload)

        # Perform the HTTP request with injected payload
        async with session.get(modified_url, headers=headers) as response:
            response_text = await response.text()

            # Pass the original content and response content to response handler for analysis
            original_content = ""  # Ideally, fetch this from a baseline (or first request)
            await handle_response_analysis(modified_url, original_content, response_text, payload, response, vulnerability_type)

    except aiohttp.ClientError as e:
        log_error(f"Network error injecting payload {payload} into {url}: {e}")
    except Exception as e:
        log_error(f"Error injecting payload {payload} into {url}: {e}")

# Main injection process
async def inject_payloads(targets, payloads, headers=None, vulnerability_type="SQLi"):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in targets:
            for payload in payloads:
                tasks.append(inject_payload(session, url, payload, headers, vulnerability_type))
        # Run injections concurrently, improving performance
        await asyncio.gather(*tasks)

# Function to handle the color-coded output for various results
def log_colored_output(message, color=Fore.WHITE):
    print(f"{color}{message}{Style.RESET_ALL}")

# Dynamically load payloads from a file based on vulnerability type
def load_payloads(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        log_error(f"Payload file not found: {file_path}")
        return []

# Main method for running the injection process
async def run_injections(targets, payloads_sql, payloads_ssrf, payloads_xss, headers=None):
    # Dynamically load payloads based on the vulnerability type
    payloads_dict = {
        "SQLi": payloads_sql,
        "SSRF": payloads_ssrf,
        "XSS": payloads_xss
    }

    # Display start message with color coding
    log_colored_output("Starting payload injection process...")

    # Inject payloads concurrently for SQLi, SSRF, and XSS
    # Optimized by creating a list of tasks and running them all concurrently
    injection_tasks = []
    for vuln_type, payloads in payloads_dict.items():
        if payloads:
            injection_tasks.append(inject_payloads(targets, payloads, headers, vuln_type))
    
    # Run all tasks concurrently
    await asyncio.gather(*injection_tasks)

    # Display completion message
    log_colored_output("Payload injection process completed!", Fore.GREEN)

# If running as a standalone script
if __name__ == "__main__":
    # Example of loading necessary files dynamically, ensuring flexibility
    targets = load_user_agents("targets.txt")  # Or load from the command line arguments
    payloads_sql = load_payloads("SQLi_Payloads.txt")
    payloads_ssrf = load_payloads("SSRF_Payloads.txt")
    payloads_xss = load_payloads("XSS_Payloads.txt")
    
    headers = {
        "X-BUG-HUNTER-ID": "z3r0-s3c@greynodesecurity.com"
    }  # You can update or pass headers dynamically as well

    # Run the injection process asynchronously
    asyncio.run(run_injections(targets, payloads_sql, payloads_ssrf, payloads_xss, headers))
