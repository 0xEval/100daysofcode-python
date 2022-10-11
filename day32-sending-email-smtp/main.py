import datetime as dt
import smtplib
import email.message
import random

HOST = 'smtp.mailtrap.io'
PORT = 2525
USER = '9f166af6dd0aaf'   # Credentials were rotated :)
PASSWORD = 'a4955fa966cc22'   # DevOops?

receiver = 'Receiver <receiver@localhost.home>'
sender = 'Sender <sender@localhost.home>'


def send_mail(body) -> None:
    # Use Python built-in email class to avoid formatting issues
    m = email.message.Message()
    m['From'] = sender
    m['To'] = receiver
    m['Subject'] = 'Motivation for the Day'
    m.set_payload(body)

    # Indentation is not kept for a multi-line INSIDE a function!!!
    #     message = f"""\
    # From: {sender}
    # To: {receiver}
    # Subject: Motivation for the Day

    # {body}"""

    with smtplib.SMTP('smtp.mailtrap.io', 2525) as server:
        server.starttls()
        server.login('9f166af6dd0aaf', 'a4955fa966cc22')
        server.sendmail(sender, receiver, m.as_string())


try:
    # If today() is Tuesday
    now = dt.datetime.now()
    weekday = now.weekday()
    if weekday == 1:
        with open('quotes.txt', 'r') as read_f:
            quote = random.choice(read_f.readlines())
            send_mail(quote)
except FileNotFoundError as err:
    print(err)
