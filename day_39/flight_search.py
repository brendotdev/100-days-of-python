import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "your_tequila_api_key"

class FlightSearch:
    def get_iata_code(self, city_name):
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/locations/query",
            headers=headers,
            params=query
        )
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code
