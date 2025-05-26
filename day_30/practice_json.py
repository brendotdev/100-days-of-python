import json

# Writing JSON
data = {
    "website": "example.com",
    "email": "user@example.com",
    "password": "12345"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Reading JSON
with open("data.json", "r") as file:
    content = json.load(file)
    print(content["website"])