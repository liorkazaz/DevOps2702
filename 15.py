import requests
def check_if_url_uo(url):
    dd = 1234
    response = requests.get(url)
    if 200 <= response.status_code < 350:
        return True
    return False

print(check_if_url_uo())