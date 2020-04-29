# -*- coding: utf-8 -*-
__author__ = "Rajesh"

import pandas as pd
import urllib.request
import json

url = "http://service.dice.com/api/rest/jobsearch/v1/simple.json?city=21201&text=retail&pgcnt=500&age=60"
req = urllib.request.Request(url,headers={'content-type': 'application/json'})
html = urllib.request.urlopen(req)

dList = []

for j in json.loads(html.read().decode("utf-8"))['resultItemList']:
        dDict = {}
        dDict['Title'] = j['jobTitle']
        dDict['Company'] = j['company']
        # print j
        dDict['Location'] = j['location']
        dDict['Date'] = j['date']

        dList.append(dDict)

df = pd.DataFrame(dList)
df.to_csv('ZipR.csv', sep=',',index=False)