import requests

url = "http://127.0.0.1:8000/logout/"
headers = {
    "Authorization": "Token a77f9baec29fafe5b9c80cfb2ba45a0240086320"
}

response = requests.post(url, headers=headers)

if response.status_code == 200:
    print(response.json())  # {"message": "Logout realizado com sucesso."}
else:
    print(response.json())  # Em caso de erro