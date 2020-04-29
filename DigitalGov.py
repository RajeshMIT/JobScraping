# -*- coding: utf-8 -*-
__author__ = "Rajesh"

import pandas as pd
import urllib.request
import json

url = "https://api.usa.gov/jobs/search.json?query=baltimore"
req = urllib.request.Request(url,headers={'content-type': 'application/json'})
html = urllib.request.urlopen(req)

dList = []

for j in json.loads(html.read().decode("utf-8")):
        dDict = {}

        dDict['Title'] = j['position_title']
        dDict['Company'] = j['organization_name']
        dDict['JobLink']=j['url']
        # print j
        dDict['Location'] = j['locations']
        dDict['Pay_Max'] = j['maximum']
        dDict['Pay_Min'] = j['minimum']
        dDict['Posting_Start_Date'] = j['start_date']
        dDict['Posting_End_Date'] = j['end_date']

        dList.append(dDict)

df = pd.DataFrame(dList)
df.to_csv('DigitalGov.csv', sep=',',index=False)