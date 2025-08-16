import requests
import validators

def check_url_safety(url: str) -> dict:
    result = {
        "url": url,
        "valid": False,
        "safe": False,
        "reason": ""
    }

    # Validate URL format
    if not validators.url(url):
        result["reason"] = "Invalid URL format"
        return result

    result["valid"] = True

    try:
        # Try to connect to the URL
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            result["safe"] = True
            result["reason"] = "The website is reachable and seems safe"
        else:
            result["reason"] = f"Returned status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        result["reason"] = f"Connection error: {str(e)}"

    return result