

# on cloud9 run pip install requests to fetch the library

import requests, time

url = 'https://0qvcl8cdd0.execute-api.eu-west-1.amazonaws.com/Prod/'

obj1 = '{"Name": "Horsiana","Weight": 50}'
obj2 = '{"Name": "Bucefalos","Weight": 65}'
obj3 = '{"Name": "Goldilax","Weight": 45}'
obj4 = '{"Name": "Redmalicious","Weight": 55}'
obj5 = '{"Name": "Pegasina","Weight": 30}'



x = requests.post(url, data = obj1)
print(x)
x = requests.post(url, data = obj2)
print(x)
x = requests.post(url, data = obj3)
print(x)
x = requests.post(url, data = obj4)
print(x)
x = requests.post(url, data = obj5)
print(x)