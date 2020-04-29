# -*- coding: utf-8 -*-
__author__ = "Rahul Babu R"

import pandas as pd
import urllib.request
import json

url = "https://mylocalmcds.com/v2/api/public/jobspertype/?city=Baltimore&state=MD"
req = urllib.request.Request(url,headers={'content-type': 'application/json'})
html = urllib.request.urlopen(req)

dList = []

for i in json.loads(html.read().decode("utf-8")):

    for j in i['restaurants']:
        dDict = {}
        dDict['Title'] = i['title']
        dDict['Description'] = i['description'].encode('ascii', 'ignore')
        if i['type'] == 'crew':
            dDict['Department'] = 'Crew'
        elif i['type'] == 'management':
            dDict['Department'] = 'Management'
        elif i['type'] == 'maintenance':
            dDict['Department'] = 'Maintenance'
        # print j
        dDict['Location'] = j['location']['address'] + ',  ZIP:- ' + str(j['location']['zipcode'])
        dDict['Loc_lat'] = j['location']['center']['lat']
        dDict['Loc_long'] = j['location']['center']['lng']
        dDict['Salary'] = j['payrange']
        dDict['Hours'] = j['shift']
        dDict['City'] = j['friendlyCity']

        dList.append(dDict)

df = pd.DataFrame(dList)
df.to_csv('McD.csv', sep=',',index=False)