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


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + busline


response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)

buses = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print("Bus Line : " + dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName'])
print("Number of Active Buses : ",len(buses))
for i in range(len(buses)):
    print("Bus", i, "is at latitude", buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], "and longitude",
         buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
