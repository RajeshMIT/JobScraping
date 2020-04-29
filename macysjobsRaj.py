# -*- coding: utf-8 -*-
__author__ = "Rajesh"

import pandas as pd
from bs4 import BeautifulSoup
import urllib.request


dList = []
for i in range(1,200):
    dDict = {}
    print (i)
    url = 'https://www.macysjobs.com/JobDescriptions/?JobId='
    url = url + str(i)
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response.read(), 'html.parser')
        dDict['Title'] = soup.find('h1').string.encode('utf-8')
        dDict['Description'] = soup.find('div',{'class':'description'}).text.encode('utf-8').strip()
        dList.append(dDict)
    except:
        pass


df = pd.DataFrame(dList)
df.to_csv('macysjobs.csv', sep=',',index=False)