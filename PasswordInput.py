import requests

url = 'http://127.0.0.1:5000/classify-password'
password = '!flinkmovingaverage343'
data = {'password': password}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    strength = result['strength']
    print(f"The strength of the password '{password}' is: {strength}")
else:
    print(f"Error: {response.status_code}, {response.json()}")
