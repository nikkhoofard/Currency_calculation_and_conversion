BASE_PATH = 'https://api.apilayer.com/fixer/latest?'
apikey = 'apikey=kfxU5IKoRTLcX8UvEhO6qJ3DZO0xHyv2'


url = BASE_PATH+apikey


EMAIL_RECEIVER = "hosein@inprobes.com"

# rules = {
#     'archive': True,
#     'send_mail': True,
#     # preferred default is None
#     # 'preferred': None
#     'preferred': ['BTC', 'IRR', "IQD", "USD", "CAD", "AED"],
#     'notification': True
# }

rules = {
    'archive': True,
    'email': {
        'receiver': 'hosein@inprobes.com',
        'enable': True,
        'preferred': ['BTC', 'IRR', "IQD", "USD", "CAD", "AED"],
    },
    'notification': {
        'enable': True,
        'receiver': '09910904518',
        'preferred': {
            'BTC': {'min': 0.000101, 'max': 0.000110},
            'IRR': {'min': 45000, 'max': 50000},
        }
    }
}