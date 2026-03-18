def generate_blocklists(correlated_data):

    ip_list = []
    domain_list = []
    url_list = []

    for item in correlated_data:

        if item["severity"] in ["MEDIUM", "HIGH"]:

            if item["type"] == "ip":
                ip_list.append(item["indicator"])

            elif item["type"] == "domain":
                domain_list.append(item["indicator"])

            elif item["type"] == "url":
                url_list.append(item["indicator"])

    return ip_list, domain_list, url_list


def save_blocklist(filename, data):

    with open(filename, "w") as f:
        for item in data:
            f.write(item + "\n")
