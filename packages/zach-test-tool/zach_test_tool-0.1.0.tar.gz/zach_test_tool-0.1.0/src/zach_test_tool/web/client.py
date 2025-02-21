import requests

def get_json(url: str) -> dict:
    """Fetch JSON data from URL"""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()