from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

key = sys.argv[1]
busline = sys.argv[2]
filename = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + busline

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)

# this line opens a file for writing using the name you chose
# the "w" tells it you are opening for writing, not reading
fout = open(sys.argv[3], "w")

buses = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

for i in range(len(buses)):
    Latitude = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    Longitude = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    try:
        Stop_Name = buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except KeyError:
        Stop_Name = 'N/A'
    try:
        Stop_Status = buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except KeyError:
        Stop_Status = 'N/A'
    fout.write('%s,%s,%s,%s\n'%(Latitude,Longitude,Stop_Name,Stop_Status))
