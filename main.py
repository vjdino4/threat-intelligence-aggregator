from utils.file_loader import load_file
from parsers.feed_parser import extract_ips, extract_domains, extract_urls
from core.validator import validate_ip, validate_domain, validate_url
from core.normalizer import normalize
from core.correlation_engine import correlate_iocs
from core.blocklist_generator import generate_blocklists, save_blocklist
from core.report_generator import generate_report, save_report

# Step 1: Load feeds
ip_data = load_file("feeds/ip_feed.txt")
domain_data = load_file("feeds/domain_feed.txt")
url_data = load_file("feeds/url_feed.txt")

# Step 2: Parse
ips = extract_ips(ip_data)
domains = extract_domains(domain_data)
urls = extract_urls(url_data)

# Step 3: Validate
valid_ips = [ip for ip in ips if validate_ip(ip)]
valid_domains = [d for d in domains if validate_domain(d)]
valid_urls = [u for u in urls if validate_url(u)]

# Step 4: Normalize
ioc_database = []

for ip in valid_ips:
    ioc_database.append(normalize(ip, "ip", "ip_feed"))

for d in valid_domains:
    ioc_database.append(normalize(d, "domain", "domain_feed"))

for u in valid_urls:
    ioc_database.append(normalize(u, "url", "url_feed"))

# Step 5: Correlate
correlated_data = correlate_iocs(ioc_database)

# Step 6: Blocklists
ip_blocklist, domain_blocklist, url_blocklist = generate_blocklists(correlated_data)

save_blocklist("outputs/blocklist_ips.txt", ip_blocklist)
save_blocklist("outputs/blocklist_domains.txt", domain_blocklist)
save_blocklist("outputs/blocklist_urls.txt", url_blocklist)

# Step 7: Report
report = generate_report(correlated_data)
save_report(report)

print("\nProject Completed Successfully!")
