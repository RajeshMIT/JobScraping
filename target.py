# -*- coding: utf-8 -*-
__author__ = "Rahul Babu R"

import pandas as pd
from bs4 import BeautifulSoup
import urllib
import json

# lat = '39.2903848'
# lng = '-76.61218930000001'

url = 'https://jobs.target.com/search-jobs/results?CurrentPage=1&RecordsPerPage=500&Distance=50&RadiusUnitType=0&Keywords=baltimore&Location=&Latitude=39.2903848&Longitude=-76.61218930000001&ShowRadius=False&CustomFacetName=&FacetTerm=&FacetType=0&FacetFilters%5B0%5D.ID=7163&FacetFilters%5B0%5D.FacetType=1&FacetFilters%5B0%5D.Count=99&FacetFilters%5B0%5D.Display=Store+Hourly&FacetFilters%5B0%5D.IsApplied=true&FacetFilters%5B0%5D.FieldName=&SearchResultsModuleName=Search+Results&SearchFiltersModuleName=Search+Filters&SortCriteria=0&SortDirection=0&SearchType=1&CategoryFacetTerm=&CategoryFacetType=&LocationFacetTerm=&LocationFacetType=&KeywordType=&LocationType=&LocationPath=&OrganizationIds=1118'
req = urllib2.Request(url,headers={'content-type': 'application/json'})
html = urllib2.urlopen(req)

soup = BeautifulSoup(str(json.loads(html.read())['results']),'html.parser')
i = 0
title = soup.findAll('h2')
ititle = iter(title)
next(ititle)
tList = []
for i in ititle:
    tList.append(i.string.encode('utf-8').strip())

locList = []
for loc in soup.findAll('span',{'class':'job-location'}):
    locList.append(loc.string)

dateList = []
for date in soup.findAll('span',{'class':'job-date-posted'}):
    dateList.append(date.string)
dList = []
for le in range(0, len(locList)):
    dDict = {}
    dDict['Location'] = locList[le]
    dDict['Job_Posting'] = dateList[le]
    dDict['Job Section'] = 'Store Hourly'
    dDict['Job Title'] = tList[le]
    dList.append(dDict)

df = pd.DataFrame(dList)
df.to_csv('target.csv', sep=',',index=False)
