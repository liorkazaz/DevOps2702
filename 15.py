import requests
def check_if_url_uo(url):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        return True
    return False

print(check_if_url_uo())