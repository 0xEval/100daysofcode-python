class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, data, date_from, date_to) -> None:
        self.row_id = data['id']
        self.city_from = 'London'
        self.iata_from = 'LON'
        self.city_to = data['city']
        self.iata_to = data['iataCode']
        self.lowest_price = data['lowestPrice']
        self.date_from = date_from
        self.date_to = date_to
