__author__ = "Rajesh Sridhar"

import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

titleList = []
comList = []
locList = []
dateList = []
descList = []
dList = []

for i in range(1, 201):

    catUrl = 'https://www.metrobaltimorejobs.com/j/c-Retail-Wholesale-l-Baltimore,-MD-jobs-c1566-p'
    catUrl = catUrl + str(i) + '-ob2.html'
    catRequest = urllib.request.Request(catUrl)
    catResponse = urllib.request.urlopen(catRequest)

    catHtml = catResponse.read().decode('utf-8')

    soup = BeautifulSoup(catHtml, 'html.parser')

    for sap in soup.findAll('span', {'style': 'font-size:1.1em;'}):
        if sap.string.strip() is not None:
            titleList.append((sap.string.encode('utf-8').strip()).decode('utf-8'))
        else:
            titleList.append(None)

    for sap4 in soup.findAll('span', {'class': 'float-right'}):
        if sap4.string is not None:
            dateList.append((sap4.string.encode('utf-8').strip()).decode('utf-8'))

    for sap5 in soup.findAll('div', {'class': 'columns medium-10'}):
        if sap5.string is not None:
            descList.append((sap5.string.encode('utf-8').strip()).decode('utf-8'))

    for sap2 in soup.findAll('div', {'class': 'columns medium-2'}):
        soup = BeautifulSoup(str(sap2), 'html.parser')
        if len(soup.findAll('a')) > 0:
            for sap1 in soup.findAll('a'):
                if sap1.string is not None:
                    comList.append(sap1.string)
        else:
            if sap2.string is not None:
                if (sap2.string.encode('utf-8').strip()).decode('utf-8') == 'T-MOBILE USA, Inc.':
                    comList.append((sap2.string.encode('utf-8').strip()).decode('utf-8'))
                else:
                    locList.append((sap2.string.encode('utf-8').strip()).decode('utf-8'))

lenList = len(titleList)

print (lenList)
if len(comList) < lenList:
    lenList = len(comList)

if len(locList) < lenList:
    lenList = len(locList)

if len(dateList) < lenList:
    lenList = len(dateList)

if len(descList) < lenList:
    lenList = len(descList)

for le in range(0, lenList):
    dDict = {}

    dDict['Title'] = titleList[le]
    dDict['Company'] = comList[le]
    dDict['Location'] = locList[le]
    dDict['Date Posted'] = dateList[le]
    dDict['Job_Description'] = descList[le]

    dList.append(dDict)

df = pd.DataFrame(dList)
df.to_csv('MetroBaltimore.csv', sep=',', index=False)

