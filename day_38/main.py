import requests
from datetime import datetime

# ------------------ Nutritionix API ------------------ #
GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 175
AGE = 28

NUTRITIONIX_APP_ID = "your_app_id"
NUTRITIONIX_API_KEY = "your_api_key"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

user_input = input("What exercise did you do? ")

exercise_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
result = exercise_response.json()

# ------------------ Sheety API ------------------ #
SHEETY_ENDPOINT = "https://api.sheety.co/<your_project>/workouts"

today = datetime.now()
for exercise in result["exercises"]:
    sheety_data = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_data)
    print(sheety_response.text)
