import smtplib


def send_mail2(subject, text):
    # print(subject)
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"

    message = f"""\
    Subject: {subject}
    To: {receiver}
    From: {sender}

    {text}."""

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("94775ad4def549", "ba9bb165aa6602")
        server.sendmail(sender, receiver, message)

