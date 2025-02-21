import argparse
import os
from injector import run_injections
from utils.logger import log_info, log_error
from colorama import Fore, Style

# Helper function to check for required dependencies
def check_dependencies():
    try:
        import aiohttp
        import colorama
        log_info("All required dependencies are installed!")
    except ImportError as e:
        log_error(f"Missing dependency: {e.name}. Please install it using pip.")

# Function to load the targets from a file
def load_targets(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    else:
        log_error(f"Targets file not found: {file_path}")
        return []

# Main method for running the application
def main():
    check_dependencies()  # Ensure dependencies are present

    # Setup argument parser for CLI
    parser = argparse.ArgumentParser(description="BugInjectX - Automated vulnerability injection tool")
    parser.add_argument("-t", "--targets", type=str, help="File containing target URLs")
    parser.add_argument("-p", "--payloads", type=str, help="Payloads file (SQLi, XSS, SSRF)", required=True)
    parser.add_argument("-r", "--headers", type=str, help="File containing headers to be used in the injections")
    parser.add_argument("-u", "--user-agent", type=str, help="User-Agent file for rotating requests", required=False)
    parser.add_argument("-v", "--vulnerability", type=str, choices=["SQLi", "SSRF", "XSS"], help="Vulnerability type to test for", required=True)
    args = parser.parse_args()

    # Handle missing arguments and interactive mode
    if not args.targets:
        log_info("No target file specified. Please input your target URLs interactively.")
        targets_input = input("Enter your target URLs (comma-separated): ")
        targets = [url.strip() for url in targets_input.split(",")]
    else:
        targets = load_targets(args.targets)

    # Load payloads and headers
    with open(args.payloads, 'r') as file:
        payloads = [line.strip() for line in file.readlines()]

    headers = {}
    if args.headers:
        with open(args.headers, 'r') as file:
            headers = {line.split(":")[0].strip(): line.split(":")[1].strip() for line in file.readlines()}

    user_agents = []
    if args.user_agent:
        with open(args.user_agent, 'r') as file:
            user_agents = [line.strip() for line in file.readlines()]

    # Run injections
    log_info(f"Starting injection for {args.vulnerability} vulnerabilities...")
    run_injections(targets, payloads, headers=headers, vulnerability_type=args.vulnerability)

    # Color-coded output for completion
    log_info(f"Injection process for {args.vulnerability} completed!", Fore.GREEN)

if __name__ == "__main__":
    main()
