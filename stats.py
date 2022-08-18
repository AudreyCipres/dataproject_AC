from pandas import read_json
import json

# read file
myjsonfile = open(' /download/2020-biannual-incident-report.csv', 'r')
jsondata = myjsonfile.read()

# Parse
obj = json.loads(jsondata)

print(str(obj['Date/Time Opened']))
print(str(obj['Operational Directorate']))
print(str(obj['Primary Category']))
print(str(obj['Summary of the Incident (External Distribution)']))
