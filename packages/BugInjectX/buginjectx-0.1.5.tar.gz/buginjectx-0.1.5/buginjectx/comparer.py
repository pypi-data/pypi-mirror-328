import difflib
import hashlib
import re

def compare_responses(original_response, injected_response, url, payload, config):
    """
    Compare the original and injected responses to detect vulnerabilities.
    This method accounts for different edge cases and ensures accuracy.
    """
    if not original_response or not injected_response:
        return

    original_body = original_response.text
    injected_body = injected_response.text
    original_hash = generate_hash(original_body)
    injected_hash = generate_hash(injected_body)

    # If the hash differs, there was a change in the content.
    if original_hash != injected_hash:
        print(f"Content difference detected for URL: {url}")
        print(f"Injected Payload: {payload}")
        
        # Run through detailed vulnerability checks
        if config['sql_injection']:
            detect_sql_injection(original_response, injected_response, url, payload)

        if config['ssrf']:
            detect_ssrf(original_response, injected_response, url, payload)

        if config['xss']:
            detect_xss(original_response, injected_response, url, payload)

def generate_hash(response_body):
    """Generate a hash of the response body for fast comparison."""
    return hashlib.md5(response_body.encode('utf-8')).hexdigest()

def detect_sql_injection(original_response, injected_response, url, payload):
    """Detect SQLi by analyzing error messages, status codes, or body changes."""
    original_body = original_response.text
    injected_body = injected_response.text

    # Check for typical SQLi error messages
    sql_errors = ["syntax error", "sql", "error", "mysql", "database", "warning", "query"]
    for error in sql_errors:
        if error.lower() in injected_body.lower() and error.lower() not in original_body.lower():
            log_vulnerability("SQL Injection", url, payload, original_response, injected_response)
            return

    # Check for 500 errors or unusual status codes
    if injected_response.status_code == 500 and original_response.status_code != 500:
        log_vulnerability("SQL Injection (Server Error)", url, payload, original_response, injected_response)
        return

def detect_ssrf(original_response, injected_response, url, payload):
    """Detect SSRF by looking for signs of internal resource access."""
    original_body = original_response.text
    injected_body = injected_response.text

    # Detect SSRF patterns (e.g., localhost, 127.0.0.1, internal network addresses)
    ssrf_indicators = ["localhost", "127.0.0.1", "internal", "loopback", "private", "cloud"]
    for indicator in ssrf_indicators:
        if indicator in injected_body and indicator not in original_body:
            log_vulnerability("SSRF", url, payload, original_response, injected_response)
            return

def detect_xss(original_response, injected_response, url, payload):
    """Detect XSS by checking for reflected scripts or HTML injection."""
    original_body = original_response.text
    injected_body = injected_response.text

    # Detect if there are any <script> tags or alert statements in the injected body
    xss_indicators = ["<script>", "alert(", "onerror=", "javascript:"]
    for indicator in xss_indicators:
        if indicator in injected_body and indicator not in original_body:
            log_vulnerability("XSS", url, payload, original_response, injected_response)
            return

def log_vulnerability(vuln_type, url, payload, original_response, injected_response):
    """Log detailed vulnerability findings."""
    log_message = f"!!!POTENTIAL {vuln_type} FOUND!!!\n"
    log_message += f"URL: {url}\nPayload: {payload}\n"
    log_message += f"Original Response Code: {original_response.status_code}\n"
    log_message += f"Injected Response Code: {injected_response.status_code}\n"
    log_message += f"Original Response Body:\n{original_response.text[:500]}\n"  # Limit body preview
    log_message += f"Injected Response Body:\n{injected_response.text[:500]}\n\n"  # Limit body preview

    # Save the result in the vulnerability reports file
    with open("vulnerability_reports.txt", "a") as f:
        f.write(log_message)
    
    # Also print the log message to console for immediate feedback
    print(log_message)

