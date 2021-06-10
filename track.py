#http://www.geoplugin.net/json.gp?ip=157.46.182.95
# importing the requests library
import requests
import json
print("IP Tracing tool (Coded By s1b1nTh0mas)\n")  
# api-endpoint
URL = "http://www.geoplugin.net/json.gp"
# location given here
ip_address=input('Enter Ip:')
# defining a params dict for the parameters to be sent to the API
PARAMS = {'ip':ip_address}
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
# extracting data in json format
data = r.json()
print(json.dumps(data, indent=4, sort_keys=True))
