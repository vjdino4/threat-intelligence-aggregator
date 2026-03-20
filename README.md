# Threat Intelligence Aggregator

## 📌 Overview
This project is a practical Threat Intelligence Aggregator designed to collect, parse, normalize, and correlate threat intelligence indicators from multiple sources.

It simulates real-world Security Operations Center (SOC) workflows by processing Indicators of Compromise (IOCs) such as IP addresses, domains, URLs, hashes, and emails.

---

## 🎯 Key Features
- Multi-source threat intelligence aggregation
- IOC parsing (IP, Domain, URL, Hash, Email)
- Data normalization with metadata
- Correlation engine for repeated indicators
- Severity classification (Low / Medium / High)
- Live threat feed integration (Abuse.ch)
- Automated blocklist generation
- Advanced reporting with top threats

---

## ⚙️ Technologies Used
- Python
- Requests (API fetching)
- Regex (IOC extraction)
- JSON / CSV (data processing)

---

## 📂 Project Structure
feeds/        -> Input threat feeds  
parsers/      -> IOC extraction logic  
core/         -> Normalization & correlation  
utils/        -> Helper functions  
outputs/      -> Generated blocklists & reports  
screenshots/  -> Project report PDF 

