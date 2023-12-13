import requests

api_url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(api_url)

headers = {
    "User-Agent": "MyApp/1.0"
}

get_response = requests.get(api_url, headers=headers)

print("\nHTTP Status Code:", get_response.status_code)
print("\nResponse Headers:")
for key, val in get_response.headers.items():
    print(f"{key}: {val}")
print("\nResponse Content:", get_response.text)

post_data = {
    "title": "The Dog",
    "body": "My dog is cute <3"
}

post_response = requests.post(api_url, json=post_data)

print("\nHTTP Status Code:", post_response.status_code)
print("\nResponse Content:", post_response.text)