# ============================================================================
# IP WHOIS INFORMATION LOOKUP TOOL
# ============================================================================
# A comprehensive tool for retrieving and displaying WHOIS information for
# IP addresses. Provides network registration details, organizational data,
# geographical information, and administrative records for network analysis
# and security investigations.
# ============================================================================

# Import required libraries
from ipwhois import IPWhois  # For WHOIS data retrieval and RDAP lookups
import re  # For IP address validation using regular expressions
from typing import Dict, List, Optional, Any  # For type hints and annotations

# ============================================================================
# CONFIGURATION CONSTANTS
# ============================================================================
# Define standard display formatting
SEPARATOR_LINE = "-" * 50
SECTION_HEADER = "=" * 60

# Define WHOIS data field mappings for display
WHOIS_DISPLAY_FIELDS = {
    'cidr': 'Net Range',
    'name': 'Organization',
    'country': 'Country',
    'created': 'Created Date',
    'updated': 'Last Updated',
    'description': 'Description'
}


# ============================================================================
# IP ADDRESS VALIDATION
# ============================================================================
def validate_ip_address(ip_address: str) -> bool:
    """
    Validates if the provided string is a valid IPv4 or IPv6 address.

    Args:
        ip_address (str): The IP address string to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    # IPv4 VALIDATION PATTERN
    # Matches standard IPv4 format: xxx.xxx.xxx.xxx where xxx is 0-255
    ipv4_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    # IPv6 VALIDATION PATTERN (simplified)
    # Matches basic IPv6 format with hexadecimal groups separated by colons
    ipv6_pattern = r'^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$|^::1$|^::$'

    # VALIDATION CHECK
    # Test against both IPv4 and IPv6 patterns
    if re.match(ipv4_pattern, ip_address.strip()) or re.match(ipv6_pattern, ip_address.strip()):
        return True

    return False


# ============================================================================
# WHOIS DATA EXTRACTION
# ============================================================================
def extract_network_info(whois_data: Dict[str, Any]) -> Dict[str, str]:
    """
    Extracts and formats network information from raw WHOIS data.

    Args:
        whois_data (Dict[str, Any]): Raw WHOIS data from RDAP lookup.

    Returns:
        Dict[str, str]: Formatted network information with standardized keys.
    """
    # NETWORK DATA EXTRACTION
    # Extract network section from WHOIS response
    network_data = whois_data.get('network', {})

    # INFORMATION FORMATTING
    # Create clean, formatted output for display
    formatted_info = {
        'cidr': network_data.get('cidr', 'N/A'),
        'name': network_data.get('name', 'N/A'),
        'country': network_data.get('country', 'N/A'),
        'created': network_data.get('created', 'N/A'),
        'updated': network_data.get('updated', 'N/A'),
        'description': network_data.get('remarks', [{}])[0].get('description', 'N/A') if network_data.get(
            'remarks') else 'N/A'
    }

    return formatted_info


# ============================================================================
# WHOIS LOOKUP FUNCTIONALITY
# ============================================================================
def perform_whois_lookup(ip_address: str) -> Optional[Dict[str, Any]]:
    """
    Performs RDAP-based WHOIS lookup for the specified IP address.

    Args:
        ip_address (str): The IP address to query for WHOIS information.

    Returns:
        Optional[Dict[str, Any]]: WHOIS data dictionary if successful, None if failed.

    Raises:
        Exception: Various exceptions related to network connectivity or invalid IP.
    """
    try:
        # WHOIS OBJECT INITIALIZATION
        # Create IPWhois instance for the target IP address
        whois_obj = IPWhois(ip_address)

        # RDAP LOOKUP EXECUTION
        # Perform Registration Data Access Protocol (RDAP) lookup
        # RDAP is the modern replacement for traditional WHOIS protocol
        # Provides structured JSON data instead of plain text
        whois_data = whois_obj.lookup_rdap()

        return whois_data

    # SPECIFIC ERROR HANDLING
    except ConnectionError as e:
        print(f"Network connection error for {ip_address}: {e}")
        return None
    except ValueError as e:
        print(f"Invalid IP address format {ip_address}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error during WHOIS lookup for {ip_address}: {e}")
        return None


# ============================================================================
# DISPLAY FORMATTING
# ============================================================================
def display_whois_results(ip_address: str, network_info: Dict[str, str]) -> None:
    """
    Formats and displays WHOIS information in a user-friendly format.

    Args:
        ip_address (str): The IP address that was queried.
        network_info (Dict[str, str]): Formatted network information to display.
    """
    # HEADER DISPLAY
    print(f"\n{SECTION_HEADER}")
    print(f"WHOIS INFORMATION FOR: {ip_address}")
    print(f"{SECTION_HEADER}")

    # INFORMATION DISPLAY
    # Display each piece of network information with proper formatting
    for field_key, display_name in WHOIS_DISPLAY_FIELDS.items():
        value = network_info.get(field_key, 'N/A')
        print(f"{display_name:15}: {value}")

    # FOOTER SEPARATOR
    print(f"{SEPARATOR_LINE}\n")


# ============================================================================
# SINGLE IP WHOIS QUERY
# ============================================================================
def get_whois_info(ip_address: str) -> Optional[Dict[str, str]]:
    """
    Retrieves and displays comprehensive WHOIS information for a single IP address.

    Args:
        ip_address (str): The IP address to query for WHOIS information.

    Returns:
        Optional[Dict[str, str]]: Formatted WHOIS data if successful, None if failed.
    """
    # INPUT VALIDATION
    # Clean and validate the IP address format
    cleaned_ip = ip_address.strip()

    if not validate_ip_address(cleaned_ip):
        print(f"Error: Invalid IP address format: {ip_address}")
        return None

    # WHOIS LOOKUP EXECUTION
    # Perform the actual WHOIS query
    whois_data = perform_whois_lookup(cleaned_ip)

    if whois_data is None:
        print(f"Failed to retrieve WHOIS information for: {ip_address}")
        return None

    # DATA PROCESSING
    # Extract and format network information
    network_info = extract_network_info(whois_data)

    # RESULTS DISPLAY
    # Show formatted results to user
    display_whois_results(cleaned_ip, network_info)

    return network_info


# ============================================================================
# BATCH PROCESSING FUNCTIONALITY
# ============================================================================
def process_ip_list(ip_addresses: List[str]) -> Dict[str, Optional[Dict[str, str]]]:
    """
    Processes multiple IP addresses and retrieves WHOIS information for each.

    Args:
        ip_addresses (List[str]): List of IP addresses to query.

    Returns:
        Dict[str, Optional[Dict[str, str]]]: Dictionary mapping IP addresses to their WHOIS data.
    """
    # RESULTS STORAGE
    results = {}

    # BATCH PROCESSING HEADER
    print(f"\n{SECTION_HEADER}")
    print(f"PROCESSING {len(ip_addresses)} IP ADDRESSES")
    print(f"{SECTION_HEADER}")

    # SEQUENTIAL PROCESSING
    # Process each IP address in the provided list
    for index, ip_address in enumerate(ip_addresses, 1):
        print(f"\nProcessing IP {index}/{len(ip_addresses)}: {ip_address}")

        # INDIVIDUAL LOOKUP
        whois_info = get_whois_info(ip_address)
        results[ip_address] = whois_info

        # PROGRESS INDICATION
        if whois_info:
            print(f"✓ Successfully processed: {ip_address}")
        else:
            print(f"✗ Failed to process: {ip_address}")

    # BATCH COMPLETION SUMMARY
    successful_lookups = sum(1 for result in results.values() if result is not None)
    print(f"\n{SEPARATOR_LINE}")
    print(f"BATCH PROCESSING COMPLETE")
    print(f"Successful lookups: {successful_lookups}/{len(ip_addresses)}")
    print(f"{SEPARATOR_LINE}")

    return results


# ============================================================================
# MAIN PROGRAM LOGIC
# ============================================================================
def main() -> None:
    """
    Main function to demonstrate WHOIS lookup functionality with sample IP addresses.

    Processes a predefined list of IP addresses and displays their WHOIS information.
    Can be easily modified to accept user input or read from files.
    """
    # SAMPLE IP ADDRESS LIST
    # Collection of IP addresses for demonstration purposes
    # These can be replaced with user input or file-based input
    sample_ip_list = [
        "23.176.184.152"
        "59.1.245.206",  # Sample IP from Asia-Pacific region
        "170.64.193.174",  # Sample IP from North America
        "175.107.196.29",  # Sample IP from Asia-Pacific region
        "182.187.140.93"  # Sample IP from Asia-Pacific region
    ]

    try:
        # BATCH PROCESSING EXECUTION
        # Process all IP addresses in the sample list
        results = process_ip_list(sample_ip_list)

        # ADDITIONAL PROCESSING
        # Results dictionary can be used for further analysis
        # Such as generating reports, filtering by country, etc.

    # COMPREHENSIVE ERROR HANDLING
    except KeyboardInterrupt:
        print("\n\nWHOIS lookup process interrupted by user.")
    except Exception as e:
        print(f"\nUnexpected error during batch processing: {e}")


# ============================================================================
# INTERACTIVE MODE FUNCTIONALITY
# ============================================================================
def interactive_mode() -> None:
    """
    Provides an interactive mode for single IP address lookups.

    Allows users to input IP addresses manually for real-time WHOIS queries.
    """
    print("=== INTERACTIVE WHOIS LOOKUP MODE ===")
    print("Enter IP addresses to query (type 'quit' to exit)")

    while True:
        # USER INPUT COLLECTION
        user_ip = input("\nEnter IP address: ").strip()

        # EXIT CONDITION
        if user_ip.lower() in ['quit', 'exit', 'q']:
            print("Exiting interactive mode.")
            break

        # EMPTY INPUT HANDLING
        if not user_ip:
            print("Please enter a valid IP address.")
            continue

        # SINGLE IP LOOKUP
        get_whois_info(user_ip)


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    # EXECUTION MODE SELECTION
    # Default: Run with sample IP addresses
    # Uncomment the interactive mode and comment out main() for full interactive mode

    #main()  # Batch processing with sample IPs
    interactive_mode()  # Uncomment for interactive single IP queries
