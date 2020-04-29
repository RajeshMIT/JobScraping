__author__ = "Rajesh"

import pandas as pd
import urllib.request
import json

dList = []
for i in range(1, 25):
    dDict = {}
    time = 1479906000 + (i - 1) * 3600
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=61+strathmore+road+brighton+MA&destinations=New+york+city+NY&departure_time=" + str(
        time) + "&traffic_model=optimistic&key=AIzaSyC_RO1xK2sO8HUL494XRcY1y575KF04h5U"

    try:
        request = urllib.request.Request(url, headers={'content-type': 'application/json'})
        html = urllib.request.urlopen(request)
        datafile = json.loads(html.read().decode("utf-8"))
        dDict['Time'] = datafile["rows"][0]['elements'][0]['duration_in_traffic']['text']
        dList.append(dDict)
    except:
        pass

df = pd.DataFrame(dList)
df.to_csv('GoogleTime.csv', sep=',', index=False)