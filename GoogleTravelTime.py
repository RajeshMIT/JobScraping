__author__ = "Rajesh"

import pandas as pd
import urllib.request
import json
import time

dList = []
for i in range(1, 121):
    dDict = {}
    epoch_time = 1479906000 + (i - 1) * 60
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))

    dDict['Start time'] = current_time

    url1 = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=61+strathmore+road+brighton+MA&destinations=staples+drive+framingham+MA&departure_time=" + str(
        epoch_time) + "&traffic_model=best_guess&key=<apikey>"
    url2 = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=61+strathmore+road+brighton+MA&destinations=staples+drive+framingham+MA&departure_time=" + str(
        epoch_time) + "&traffic_model=optimistic&key=<apikey>"
    url3 = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=61+strathmore+road+brighton+MA&destinations=staples+drive+framingham+MA&departure_time=" + str(
        epoch_time) + "&traffic_model=pessimistic&key=<apikey>"

    request = urllib.request.Request(url1, headers={'content-type': 'application/json'})
    html = urllib.request.urlopen(request)
    datafile = json.loads(html.read().decode("utf-8"))
    dDict['Commute time - Best guess scenario'] = datafile["rows"][0]['elements'][0]['duration_in_traffic']['text']

    request = urllib.request.Request(url2, headers={'content-type': 'application/json'})
    html = urllib.request.urlopen(request)
    datafile = json.loads(html.read().decode("utf-8"))
    dDict['Commute time - Optimistic scenario'] = datafile["rows"][0]['elements'][0]['duration_in_traffic']['text']

    request = urllib.request.Request(url3, headers={'content-type': 'application/json'})
    html = urllib.request.urlopen(request)
    datafile = json.loads(html.read().decode("utf-8"))
    dDict['Commute time - Pessimistic scenario'] = datafile["rows"][0]['elements'][0]['duration_in_traffic']['text']

    dList.append(dDict)

df = pd.DataFrame(dList)
df.to_csv('GoogleTravelTime.csv', sep=',', index=False)
