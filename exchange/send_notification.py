from kavenegar import *
from config import rules


def send_sms(msg):
    api = KavenegarAPI('6E73374B61763733312F5637652B4D462F7A2B4277786D6854746A73576863542B575762754868624C2F513D')
    params = {
         'sender' : '1000596446',
          'receptor': rules['notification']['receiver'],
           'message' : msg
           }
    response = api.sms_send(params)


