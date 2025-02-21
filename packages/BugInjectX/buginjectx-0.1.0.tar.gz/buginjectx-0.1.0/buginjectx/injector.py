import asyncio
import aiohttp
from utils.logger import log_info, log_warning, log_error
from utils.response_handler import handle_response_analysis
from utils.request_handler import prepare_request_headers
import random
from colorama import Fore, Style

# Load user agents from UserAgents.txt for rotating requests
def load_user_agents(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

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
            original_content = ""  # You would have a way to fetch this from a baseline (like downloading the page first)
            handle_response_analysis(modified_url, original_content, response_text, payload, response, vulnerability_type)

    except Exception as e:
        log_error(f"Error injecting payload {payload} into {url}: {e}")

# Main injection process
async def inject_payloads(targets, payloads, headers=None, vulnerability_type="SQLi"):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in targets:
            for payload in payloads:
                tasks.append(inject_payload(session, url, payload, headers, vulnerability_type))

        # Wait for all tasks (payload injections) to complete
        await asyncio.gather(*tasks)

# Function to handle the color-coded output for various results
def log_colored_output(message, color=Fore.WHITE):
    print(f"{color}{message}{Style.RESET_ALL}")

# Main method for running the injection process
def run_injections():
    targets = []  # Load your target URLs from a file or user input
    payloads_sql = []  # Load SQLi payloads from a file (e.g., SQLI_Payloads.txt)
    payloads_ssrf = []  # Load SSRF payloads from a file (e.g., SSRF_Payloads.txt)
    payloads_xss = []  # Load XSS payloads from a file (e.g., XSS_Payloads.txt)

    headers = {"X-BUG-HUNTER-ID": "z3r0-s3c@greynodesecurity.com"}  # Example header
    user_agents = load_user_agents("UserAgents.txt")

    # Choose a random user-agent for each request (optional, for anonymity)
    headers["User-Agent"] = random.choice(user_agents)

    # Choose the vulnerability type (SQLi, SSRF, XSS)
    vulnerability_type = "SQLi"  # or SSRF, XSS based on the user input or testing context

    # Display start message with color coding
    log_colored_output("Starting payload injection process...")

    # Inject SQLi, SSRF, and XSS payloads concurrently
    asyncio.run(inject_payloads(targets, payloads_sql, headers, "SQLi"))
    asyncio.run(inject_payloads(targets, payloads_ssrf, headers, "SSRF"))
    asyncio.run(inject_payloads(targets, payloads_xss, headers, "XSS"))

    # Display completion message
    log_colored_output("Payload injection process completed!", Fore.GREEN)

# If running as a standalone script
if __name__ == "__main__":
    run_injections()
