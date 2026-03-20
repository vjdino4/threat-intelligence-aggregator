import json

def generate_report(correlated_data):

    total = len(correlated_data)

    high = [i for i in correlated_data if i["severity"] == "HIGH"]
    medium = [i for i in correlated_data if i["severity"] == "MEDIUM"]
    low = [i for i in correlated_data if i["severity"] == "LOW"]

    # Top repeated IOCs
    top_iocs = sorted(correlated_data, key=lambda x: x["count"], reverse=True)[:5]

    report = {
        "total_iocs": total,
        "high_risk": len(high),
        "medium_risk": len(medium),
        "low_risk": len(low),
        "top_threats": top_iocs
    }

    return report


def save_report(report):
    with open("outputs/report.json", "w") as f:
        json.dump(report, f, indent=4)
