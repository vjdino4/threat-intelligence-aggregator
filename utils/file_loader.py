def load_file(path):
    with open(path, "r") as file:
        data = file.read()
    return data



import requests

def load_url(url):
    try:
        response = requests.get(url)
        return response.text
    except:
        return ""
