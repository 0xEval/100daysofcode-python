import random
import smtplib
import email.message
import datetime as dt
import pandas as pd

################################################################################
#                                  CONSTANTS                                   #
################################################################################

HOST = 'smtp.mailtrap.io'
PORT = 2525
USER = '9f166af6dd0aaf'   # Credentials were rotated :)
PASSWORD = 'a4955fa966cc22'   # DevOops?
PLACEHOLDER = '[NAME]'

################################################################################
#                                  FUNCTIONS                                   #
################################################################################


def send_mail(body) -> None:
    # Use Python built-in email class to avoid formatting issues
    m = email.message.Message()
    m['From'] = sender
    m['To'] = receiver
    m['Subject'] = 'Happy Birthday!'
    m.set_payload(body)

    with smtplib.SMTP('smtp.mailtrap.io', 2525) as server:
        server.starttls()
        server.login('9f166af6dd0aaf', 'a4955fa966cc22')
        server.sendmail(sender, receiver, m.as_string())


################################################################################
#                                DATA HANDLING                                 #
################################################################################

now = dt.datetime.now()
try:
    data = pd.read_csv('birthdays.csv')
    matches = data[(data['month'] == now.month) & (data['day'] == now.day)]
    name = matches['name'].values[0]
except FileNotFoundError as err:
    print(err)


letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
letter = random.choice(letters)
try:
    with open(f'letter_templates/{letter}', 'r') as read_f:
        contents = read_f.read()
        body = contents.replace(PLACEHOLDER, name)
except FileNotFoundError as err:
    print(err)

sender = 'Bob <bob@localhost.home>'
receiver = f'{name.title()} <{matches["email"].values[0]}>'
send_mail(body)
