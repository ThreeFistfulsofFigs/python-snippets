from ipwhois import IPWhois


def get_whois_info(ip_address):
    """
    Retrieves WHOIS information for the given IP address.

    Args:
        ip_address (str): The IP address to query.

    Returns:
        dict: WHOIS data if successful, prints error if failed.
    """
    try:
        obj = IPWhois(ip_address)
        whois_data = obj.lookup_rdap()
        print(f"WHOIS for {ip_address}:")
        print(f"Net Range: {whois_data.get('network', {}).get('cidr', 'N/A')}")
        print(f"Organization: {whois_data.get('network', {}).get('name', 'N/A')}")
        print(f"Country: {whois_data.get('network', {}).get('country', 'N/A')}")
        print(f"Created: {whois_data.get('network', {}).get('created', 'N/A')}")
    except Exception as e:
        print(f"Failed to get WHOIS for {ip_address}: {e}")


# Example usage with your IPs
ip_list = ["59.1.245.206", "170.64.193.174", "175.107.196.29", "182.187.140.93"]
for ip in ip_list:
    get_whois_info(ip)