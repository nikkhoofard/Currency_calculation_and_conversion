# import smtplib
# import requests
# from email.mime.text import MIMEText


# sender = "Private Person <from@example.com>"
# receiver = "A Test User <to@example.com>"


# def send_smtp_email(subject, body):
#     message = f"""\
#         subject : {subject} 
#         {body}
#         """

#     with smtplib.SMTP("smtp.mailtrap.io", 2525) as mail_server:
#         mail_server.login("94775ad4def549", "ba9bb165aa6602")
#         mail_server.sendmail(sender, receiver, message)
import smtplib

port = 2525  # For SSL
smtp_server = "smtp.mailtrap.io"
sender_email = "my@gmail.com"  # Enter your address
receiver_email = "your@gmail.com"  # Enter receiver address 
username = '94775ad4def5'
password = 'ba9bb165aa6602'
message = """\
Subject: Hi there

This message is sent from Python."""

# context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.login(username, password)
    server.sendmail(sender_email, receiver_email, message)
