import requests
import pprint

param = {
    "q" : "html"
}

response = requests.get("https://api.github.com/search/repositories", params=param)


response_json = response.json()

print(response.status_code)
pprint.pprint(response_json["total_count"])

pprint.pprint(response_json)
