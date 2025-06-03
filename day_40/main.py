from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "SFO"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months,
    )
    if flight and flight.price < destination["lowestPrice"]:
        msg = (
            f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
            f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
        notification_manager.send_email(msg)
