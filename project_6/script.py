import requests
import urllib.request
import json
from geopy.geocoders import Nominatim
import io
api_key='aafbf2630f4bb48d5ab05c4f7d93313cf6c92bbfe3f59755fca44a2c'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
result = requests.get('https://isc.sans.edu/block.txt')
file = open('block.txt', 'w')
file.write(result.text)
file.close()

file=open('block.txt','r')
all_lines=[line.rstrip() for line in file.readlines()]
nums = {'0','1','2','3','4','5','6','7','8','9'}
ip_list=[line.split("\t",2)[0] for line in all_lines if (line[0] in nums)]
lat_long=[]
for ip in ip_list:
    headers = {
        'Accept': 'application/json'
    }
    request = urllib.request.Request('https://api.ipdata.co/'+ip+'?api-key=' + api_key, headers=headers)
    response_body = urllib.request.urlopen(request).read()
    data = json.loads(response_body)
    lat=data["latitude"]
    longi=data['longitude']
    lat_long.append((lat,longi))

fp = io.open("my_file.txt", "w", encoding="utf-8")
for l in lat_long:
    geolocator = Nominatim(user_agent='my_application')
    location = geolocator.reverse(str(l[0])+", "+str(l[1]))
    fp.write(location.address+"\n")

fp.close()