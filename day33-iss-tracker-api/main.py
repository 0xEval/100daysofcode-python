from datetime import datetime
import math
import requests
import smtplib
import email.message
import threading

URL1 = 'https://api.sunrise-sunset.org/json'
URL2 = 'http://api.open-notify.org/iss-now.json'
MY_LAT = 36.7201600
MY_LONG = -4.4203400


def is_iss_overhead() -> bool:
    """Returns True whether ISS station's coords is within +/- 5 deg from our coordinates"""
    response = requests.get(URL2)
    response.raise_for_status()

    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    return math.isclose(longitude, MY_LONG, abs_tol=5) and math.isclose(
        latitude, MY_LAT, abs_tol=5
    )


def is_nighttime() -> bool:
    """Returns True whether it is dark so the ISS can be seen"""
    parameters = {'lat': MY_LAT, 'lng': MY_LONG}

    response = requests.get(URL1, data=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    date_now = datetime.now().strftime('%-I:%M:%S %p')
    return date_now >= sunset and date_now <= sunrise


def send_mail(body) -> None:
    """Notify to 'Look Up!' by email"""
    HOST = 'smtp.mailtrap.io'
    PORT = 2525
    USER = '9f166af6dd0aaf'
    PASSWORD = 'a4955fa966cc22'

    receiver = 'Receiver <receiver@localhost.home>'
    sender = 'Sender <sender@localhost.home>'
    # Use Python built-in email class to avoid formatting issues
    m = email.message.Message()
    m['From'] = sender
    m['To'] = receiver
    m['Subject'] = 'Look Up!'
    m.set_payload(body)

    with smtplib.SMTP('smtp.mailtrap.io', 2525) as server:
        server.starttls()
        server.login('9f166af6dd0aaf', 'a4955fa966cc22')
        server.sendmail(sender, receiver, m.as_string())


def main():
    def look_up():
        if is_nighttime() and is_iss_overhead():
            send_mail('ISS is overhead')

    threading.Timer(60, look_up)


main()
