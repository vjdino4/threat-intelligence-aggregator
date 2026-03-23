# Imports
from utils.file_loader import load_file, load_url
from parsers.feed_parser import extract_ips, extract_domains, extract_urls, extract_hashes, extract_emails
from core.validator import validate_ip, validate_domain, validate_url, validate_hash, validate_email
from core.normalizer import normalize
from core.correlation_engine import correlate_iocs
from core.blocklist_generator import generate_blocklists, save_blocklist
from core.report_generator import generate_report, save_report


# -------------------------------
# STEP 1: Load Feeds
# -------------------------------
print("[INFO] Loading feeds...")

ip_data = load_file("feeds/ip_feed.txt")
domain_data = load_file("feeds/domain_feed.txt")
url_data = load_file("feeds/url_feed.txt")

# Live threat feed
live_feed = load_url("https://feodotracker.abuse.ch/downloads/ipblocklist.txt")


# -------------------------------
# STEP 2: Parse Indicators
# -------------------------------
print("[INFO] Parsing IOCs...")

ips = extract_ips(ip_data) + extract_ips(live_feed)
domains = extract_domains(domain_data)
urls = extract_urls(url_data)

hashes = extract_hashes(ip_data + domain_data + url_data)
emails = extract_emails(ip_data + domain_data + url_data)


# -------------------------------
# STEP 3: Validate
# -------------------------------
valid_ips = [ip for ip in ips if validate_ip(ip)]
valid_domains = [d for d in domains if validate_domain(d)]
valid_urls = [u for u in urls if validate_url(u)]
valid_hashes = [h for h in hashes if validate_hash(h)]
valid_emails = [e for e in emails if validate_email(e)]


# -------------------------------
# STEP 4: Normalize
# -------------------------------
ioc_database = []

for ip in valid_ips:
    ioc_database.append(normalize(ip, "ip", "feed"))

for d in valid_domains:
    ioc_database.append(normalize(d, "domain", "feed"))

for u in valid_urls:
    ioc_database.append(normalize(u, "url", "feed"))

for h in valid_hashes:
    ioc_database.append(normalize(h, "hash", "feed"))

for e in valid_emails:
    ioc_database.append(normalize(e, "email", "feed"))


# -------------------------------
# STEP 5: Correlation Engine
# -------------------------------
print("[INFO] Running correlation engine...")

correlated_data = correlate_iocs(ioc_database)


# -------------------------------
# STEP 6: Generate Blocklists
# -------------------------------
print("[INFO] Generating blocklists...")

ip_blocklist, domain_blocklist, url_blocklist = generate_blocklists(correlated_data)

save_blocklist("outputs/blocklist_ips.txt", ip_blocklist)
save_blocklist("outputs/blocklist_domains.txt", domain_blocklist)
save_blocklist("outputs/blocklist_urls.txt", url_blocklist)


# -------------------------------
# STEP 7: Reporting
# -------------------------------
print("[INFO] Generating report...")

report = generate_report(correlated_data)
save_report(report)


# -------------------------------
# FINAL OUTPUT
# -------------------------------
print("\n[✔] Project Completed Successfully!")
