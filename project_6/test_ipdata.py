# IP address to lat/long demo
# Test of ipdata.co geolocation API
#
# Note: you must sign up for a free API key here http://www.ipdata.co
# Replace "api_key" with your key
# Limitations: The free tier allows 1500 requests a day or 45,000 requests a month--> it is up to you to make sure you do not violate these restrictions.


import urllib.request
api_key='aafbf2630f4bb48d5ab05c4f7d93313cf6c92bbfe3f59755fca44a2c'
headers = {
  'Accept': 'application/json'
}
request = urllib.request.Request('https://api.ipdata.co/8.8.8.8?api-key=', headers=headers)

response_body = urllib.request.urlopen(request).read()

print(response_body)
print("\n")
                
import json
foo = json.loads(response_body)
 
print(foo["latitude"])
print(type(foo["longitude"]))