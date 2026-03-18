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
