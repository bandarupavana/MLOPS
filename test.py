import requests
import json

url = "http://127.0.0.1:5003/predict"
print(f"Sending request to: {url}")  

data = {
    "features": [23,10,2002,46986,90,1,0,2000,3,210,1165,0,1,3]
  }
  

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))

print("Status Code:", response.status_code)
print("Response:", response.json())