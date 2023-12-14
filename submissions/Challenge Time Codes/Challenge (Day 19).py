import requests

api_url = " https://api.spacexdata.com/v5/launches/latest"

response = requests.get(api_url)

if response.status_code == 200:
    print("SpaceX API Latest SpaceX Launch Information:\n")
    data = response.json()
    for key, val in data.items():
        print(f"{key}: {val}")
else:
    print(f"Request failed with {response.status_code} status code.")
