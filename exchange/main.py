import requests
import smtplib
import json
from mail2 import send_mail2
from config import url ,rules


def get_rates():
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()

    return None


def send_mail(timestamp, rates):
    subject = f'{timestamp} rates'
    if rules['email']['preferred'] is not None:
        tmp = dict()
        for exc in rules['email']['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp

    text = json.dumps(rates)
    
    send_mail2(subject,text)

    



def archive(filename,rates):
    with open(f'archive/{filename}', "w") as f:
        f.write(json.dumps(rates))
        f.close()


if __name__ == "__main__":
    res = get_rates()

    if rules['archive']:
        archive(res['timestamp'], res['rates'])

    if rules['email']['enable']:
        # send_mail2(res['timestamp'], res['rates'])
        send_mail(res['timestamp'], res['rates'])
    # if rules['notification']['enable']:
    #     notification_msg = check_notify_rules(res['rates'])
    #     if notification_msg:
    #         send_notification(notification_msg)

