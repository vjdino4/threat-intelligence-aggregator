import json

def generate_report(correlated_data):

    total = len(correlated_data)

    high = len([i for i in correlated_data if i["severity"] == "HIGH"])
    medium = len([i for i in correlated_data if i["severity"] == "MEDIUM"])
    low = len([i for i in correlated_data if i["severity"] == "LOW"])

    report = {
        "total_iocs": total,
        "high_risk": high,
        "medium_risk": medium,
        "low_risk": low
    }

    return report


def save_report(report):

    with open("outputs/report.json", "w") as f:
        json.dump(report, f, indent=4)
