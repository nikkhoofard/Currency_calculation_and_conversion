import requests
import json
from config import url


def get_rate():
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()

    return None

def archive(filename,rates):
    with open(f'archive/{filename}',"w") as f:
        f.write(json.dumps(rates))
        f.close()


if __name__ == "__main__":
    response = get_rate()
    archive(response['timestamp'],response['rates'])


