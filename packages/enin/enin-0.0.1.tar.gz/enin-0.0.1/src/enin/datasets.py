import requests

def system_status():
    return requests.get("https://api.enin.ai/datasets/v1/system-status").json()
