import re

def extract_ips(text):
    pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    return re.findall(pattern, text)

def extract_domains(text):
    pattern = r"\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r"https?://[^\s]+"
    return re.findall(pattern, text)


def extract_hashes(text):
    import re
    
    md5_pattern = r"\b[a-fA-F0-9]{32}\b"
    sha256_pattern = r"\b[a-fA-F0-9]{64}\b"
    
    md5 = re.findall(md5_pattern, text)
    sha256 = re.findall(sha256_pattern, text)
    
    return md5 + sha256


def extract_emails(text):
    import re
    
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)
