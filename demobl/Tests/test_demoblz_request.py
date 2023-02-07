import requests
import json

url = "https://api.demoblaze.com/bycat"

payload = json.dumps({
  "cat": "phone"
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
for Items in response:
  print(Items)

print(response.text)