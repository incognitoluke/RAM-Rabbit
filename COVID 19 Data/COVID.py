from urllib.request import urlopen
import json

url = "https://covidtracking.com/api/states/daily"
response = urlopen(url)
j = json.load(response)
n = 0
cases = 0
for i in j:
    if (j[n])['state'] == 'CA':
        print(j[n])
        cases += (j[n])['positiveIncrease']
    else:
         n += 1
         continue
    n += 1
print(cases)