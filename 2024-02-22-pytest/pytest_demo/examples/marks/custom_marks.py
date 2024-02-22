import requests


def internet_connection(url: str):
    """"""
    result = requests.post(url=url)
    return result.status_code
