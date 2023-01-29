import requests
import json
from config import url


def get_rate():
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()

    return None


if __name__ == "__main__":
    response = get_rate()
    print(response['rates'])


