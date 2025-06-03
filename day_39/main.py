from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()

# Fill in missing IATA codes
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_iata_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
