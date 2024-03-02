base_url = "http://thingsboard.frankfurt-14.cloud.example.com"
token = "access-token"

import requests
import random
import time

url = base_url + "/api/v1/" + token + "/telemetry"
try:
	while True:
		temp = random.randint(20, 25)
		requests.post(url, json={"temperature": temp})
		print(f"New entry: {temp}")
		time.sleep(1)
except KeyboardInterrupt:
	exit(0)