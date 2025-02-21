import argparse
import os
import time
from injector import run_injections
from utils.logger import log_info, log_error
from colorama import Fore, Style, init

# Initialize colorama for colored text output
init(autoreset=True)

# ASCII Art Logo
ASCII_ART = f"""{Fore.BLUE}
 ____              ___        _           _  __  __
| __ ) _   _  __ _|_ _|_ __  (_) ___  ___| |_\ \/ /
|  _ \| | | |/ _` || || '_ \ | |/ _ \/ __| __|\  / 
| |_) | |_| | (_| || || | | || |  __/ (__| |_ /  \ 
|____/ \__,_|\__, |___|_| |_|/ |\___|\___|\__/_/\_\
             |___/         |__/                    
                                             
  {Style.RESET_ALL}"""

# Function to display loading screen
def loading_screen():
    print(ASCII_ART)
    time.sleep(0.5)
    print(Fore.GREEN + "Designed by: Z3r0 S3c")
    time.sleep(0.5)
    print(Fore.RED + "A simple tool to test payload injection attacks")
    time.sleep(0.5)

# Dependency check
def check_dependencies():
    try:
        import aiohttp
        import colorama
        log_info("All required dependencies are installed!", Fore.CYAN)
    except ImportError as e:
        log_error(f"Missing dependency: {e.name}. Install it using: pip install {e.name}")
        exit(1)

# Load targets from a file
def load_targets(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    else:
        log_error(f"Targets file not found: {file_path}")
        return []

# Load payloads from a file
def load_payloads(file_path):
    if not os.path.exists(file_path):
        log_error(f"Payloads file not found: {file_path}")
        exit(1)
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Load headers from a file
def load_headers(file_path):
    headers = {}
    if file_path and os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file.readlines():
                parts = line.split(":", 1)  # Ensure we split correctly
                if len(parts) == 2:
                    headers[parts[0].strip()] = parts[1].strip()
                else:
                    log_error(f"Invalid header format: {line.strip()}")
    return headers

# Load user-agents from a file
def load_user_agents(file_path):
    if file_path and os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

# Main function
def main():
    loading_screen()
    check_dependencies()  # Ensure all dependencies are installed

    # Argument parser
    parser = argparse.ArgumentParser(description="BugInjectX - Automated payload injection tool")
    parser.add_argument("-t", "--targets", type=str, help="File containing target URLs")
    parser.add_argument("-p", "--payloads", type=str, help="Payloads file (SQLi, XSS, SSRF)", required=True)
    parser.add_argument("-r", "--headers", type=str, help="File containing headers for requests")
    parser.add_argument("-u", "--user-agent", type=str, help="User-Agent file for rotating requests")
    parser.add_argument("-v", "--vulnerability", type=str, choices=["SQLi", "SSRF", "XSS"], help="Type of vulnerability to test", required=True)
    args = parser.parse_args()

    # Handle interactive mode if targets file isn't provided
    if not args.targets:
        log_info("No target file specified. Enter URLs interactively:", Fore.YELLOW)
        targets_input = input(Fore.YELLOW + "Enter your target URLs (comma-separated): ")
        targets = [url.strip() for url in targets_input.split(",") if url.strip()]
    else:
        targets = load_targets(args.targets)

    # Load payloads
    payloads = load_payloads(args.payloads)

    # Load headers
    headers = load_headers(args.headers)

    # Load user-agents
    user_agents = load_user_agents(args.user_agent)

    # Ensure at least one target is provided
    if not targets:
        log_error("No targets specified! Please provide valid URLs.", Fore.RED)
        exit(1)

    # Start injections
    log_info(f"Starting injection tests for {args.vulnerability} vulnerabilities...", Fore.GREEN)
    run_injections(targets, payloads, headers=headers, vulnerability_type=args.vulnerability)

    log_info(f"Injection process for {args.vulnerability} completed successfully!", Fore.GREEN)

if __name__ == "__main__":
    main()
