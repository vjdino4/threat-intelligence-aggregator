# 🚀Threat Intelligence Aggregator (Non-AI)
## Overview

A Python-based Threat Intelligence Aggregator that collects, parses, normalizes, and correlates Indicators of Compromise (IOCs) from multiple threat intelligence feeds — without using AI/ML.

The system transforms raw threat data into actionable intelligence, generating blocklists and reports for security operations.

---

## Key Features
Multi-source threat intelligence aggregation
IOC parsing (IP, Domain, URL, Hash, Email)
Data normalization with metadata
Correlation engine for repeated indicators
Severity classification (Low / Medium / High)
Automated blocklist generation
Threat intelligence reporting

---

## Tech Stack

##Language:

Python

## Libraries:

requests – Fetch threat feeds
re – Pattern matching (IOC extraction)
json, csv – Data parsing
ipaddress – IP validation
hashlib – Hash validation

## Data Sources:

OSINT feeds (e.g., Abuse.ch)
Local files (CSV, TXT, JSON)

---

## How It Works
- Load threat feeds (files or URLs)
- Extract IOCs (IP, domain, URL, hash, email)
- Normalize data into a standard format
- Correlate indicators across multiple sources
- Assign severity based on frequency
- Generate blocklists
- Export final threat intelligence report

---

## Core Modules
1. Feed Loader – Imports IOC data
2. Parser Engine – Extracts indicators
3. Normalization Engine – Standardizes data
4. Correlation Engine – Identifies repeated threats
5. Blocklist Generator – Creates deployable lists
6. Reporting Module – Generates summaries

---

## Project Structure
feeds/        # Input threat feeds  
parsers/      # IOC extraction logic  
core/         # Normalization & correlation  
utils/        # Helper functions  
outputs/      # Blocklists & reports  
screenshots/  # Project report  

---

## Output
- Normalized IOC dataset
- High-risk correlated indicators
- Blocklists (IP, Domain, URL, Hash)
- Threat intelligence report

---

## Use Cases
- SOC threat monitoring
- Firewall / IDS rule generation
- Malware infrastructure detection
- Threat intelligence automation

---

## Learning Outcomes
- IOC parsing & validation
- Threat intelligence workflows
- Data normalization & correlation
- Blue team defensive techniques

---

## Documentation
Full report available:
screenshots/Outputs file-GitHub.pdf

# Author
Vijaya  
SOC Analyst (Aspiring) | Threat Intelligence | SIEM | Incident Response | Python
