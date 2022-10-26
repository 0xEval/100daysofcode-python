from datetime import datetime
from dateutil.relativedelta import relativedelta

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

from pprint import pprint

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


sheet_id = '3d25f658aa1c388eeeb613343ffa7c48'
project_name = 'flightDeals'
sheet_name = 'prices'
dm = DataManager(
    sheet_id=sheet_id, project_name=project_name, sheet_name=sheet_name
)

flight_search = FlightSearch()
notification = NotificationManager()

now = datetime.now()
later_date = now + relativedelta(months=+6)
date_format = '%d/%m/%Y'

for data in dm.get_rows()['prices']:
    flight = FlightData(data, now, later_date)
    price_query = flight_search.get_lowest_price_between_range(
        fly_from=flight.iata_from,
        fly_to=flight.iata_to,
        date_from=now.strftime(date_format),
        date_to=later_date.strftime(date_format),
    )
    print(price_query)
    if price_query < flight.lowest_price:
        notification.send_sms_notification(flight)
        dm.edit_row(
            row_id=flight.row_id,
            lowestPrice=price_query,
        )
