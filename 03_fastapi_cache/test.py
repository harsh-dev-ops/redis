import requests

url = "http://localhost:8000/api/books"

response = requests.get(url)

print(response.json())

# Didn't worked with postman, python requests and curl