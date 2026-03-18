def correlate_iocs(ioc_database):

    ioc_map = {}

    # Count occurrences
    for ioc in ioc_database:

        key = ioc["indicator"]

        if key not in ioc_map:
            ioc_map[key] = {
                "type": ioc["type"],
                "sources": set([ioc["source"]])
            }
        else:
            ioc_map[key]["sources"].add(ioc["source"])

    # Convert to final list with severity
    correlated_list = []

    for indicator, data in ioc_map.items():

        count = len(data["sources"])

        # Severity logic
        if count >= 3:
            severity = "HIGH"
        elif count == 2:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        correlated_list.append({
            "indicator": indicator,
            "type": data["type"],
            "sources": list(data["sources"]),
            "count": count,
            "severity": severity
        })

    return correlated_list
