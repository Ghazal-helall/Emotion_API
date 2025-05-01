import requests

url = "http://127.0.0.1:8000/predict-emotion"
data = {"text": "I am so happy today!"}

response = requests.post(url, json=data)
print(response.json())
