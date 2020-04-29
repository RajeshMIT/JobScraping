# -*- coding: utf-8 -*-
__author__ = "Rajesh"

import pandas as pd
import urllib.request
import json


dList = []
for i in range(1,10):
    print (i)
    url = 'https://api-v2.themuse.com/jobs?location=MD&page='
    url = url + str(i)

    try:
        req = urllib.request.Request(url, headers={'content-type': 'application/json'})
        html = urllib.request.urlopen(req)

        for j in json.loads(html.read().decode("utf-8"))['results']:
            dDict = {}
            dDict['Title'] = j['name']
            dDict['Company'] = j['company']['name']
            # print j
            for k in j['locations']:
                dDict['Location'] = k['name']
            dDict['Date'] = j['publication_date']
            dDict['Job Link'] = j['refs']['landing_page']
            dDict['Job description'] = j['contents']

            dList.append(dDict)
    except:
        pass


df = pd.DataFrame(dList)
df.to_csv('Muse.csv', sep=',',index=False)