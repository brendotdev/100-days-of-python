import requests
from datetime import datetime

USERNAME = "yourusername"
TOKEN = "yourtoken"  # Generate a unique token for Pixela API
GRAPH_ID = "graph1"

# -------------------- Create a User -------------------- #
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# To create a user, uncomment the line below:
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# -------------------- Create a Graph -------------------- #
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# To create a graph, uncomment the line below:
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# -------------------- Post a Pixel -------------------- #
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")
pixel_data = {
    "date": today,
    "quantity": "1"
}

# To add a pixel:
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# -------------------- Update a Pixel -------------------- #
update_endpoint = f"{pixel_creation_endpoint}/{today}"
new_pixel_data = {
    "quantity": "2"
}

# To update a pixel:
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# -------------------- Delete a Pixel -------------------- #
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
