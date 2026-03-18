import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False

def validate_domain(domain):
    return "." in domain

def validate_url(url):
    return url.startswith("http")
