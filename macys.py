# -*- coding: utf-8 -*-
__author__ = "Rahul Babu R"

import pandas as pd
from bs4 import BeautifulSoup
import urllib2

lat = '39.2903848'
lng = '-76.61218930000001'

#get all the categories

catUrl = 'https://macysjobs.com/umbraco/surface/AjaxJobSearch/Dynamic_CategoryFilterGenerator?keyword=&lat='+lat+'&lng='+lng+'&distance=25&schedule=&shifts=&locationkeyword='
catRequest = urllib2.Request(catUrl)
catResponse = urllib2.urlopen(catRequest)

catHtml = catResponse.read()
soup = BeautifulSoup(catHtml,'html.parser')

catTag = soup.find_all('input')
categories = []
for i in catTag:
    soup = BeautifulSoup(str(i),'html.parser')
    if soup.find('input').get('data-category') is None:
        pass
    else:
        categories.append(soup.find('input').get('data-category'))

#getting data of each job categories
dList = []
for i in categories:
    print i
    displayed = 0
    count = -1
    jcb = 0
    locList = []
    descList = []
    sectionList = []
    timeList = []
    while count != 0:
        #iterating through all the jobs in a particular category
        if jcb == 1:
            catDetailsUrl = 'https://macysjobs.com/umbraco/surface/AjaxJobSearch/Dynamic_JobList?currentnumberofjobsdisplayed='+str(numDisplayed)+'&keyword=&location=&lat='+lat+'&lng='+lng+'&distance=25&categories='+str(i)+'&areasofbusiness=&positiontypenames=&schedule=&shifts=&sorting=Nearest&locationkeyword=&homepageinitialload=false'
        else:
            catDetailsUrl = 'https://macysjobs.com/umbraco/surface/AjaxJobSearch/Dynamic_JobList?keyword=&location=&lat='+lat+'&lng='+lng+'&distance=25&categories='+str(i)+'&areasofbusiness=&positiontypenames=&schedule=&shifts=&sorting=Nearest&locationkeyword='
        if jcb == 1:
            catDetailsRequest = urllib2.Request(catDetailsUrl,None,headers = headers)
            catDetailsResponse = urllib2.urlopen(catDetailsRequest)
        else:
            catDetailsRequest = urllib2.Request(catDetailsUrl)
            catDetailsResponse = urllib2.urlopen(catDetailsRequest)
        #extracting cookie for the next iteration
        cookie = catDetailsResponse.info()['Set-Cookie'].split(';')[0]
        headers = {'Cookie':str(cookie)}
        jcb = 1
        soup = BeautifulSoup(str(catDetailsResponse.read()),'html.parser')
        if soup.find('input').get('data-jobcount') is not None:
            total = soup.find('input').get('data-jobcount')
        else:
            total = total
        #getting number of jobs displayed per request
        numDisplayed = soup.find('input').get('data-currentnumberofjobsdisplayed')
        if soup.find('input').get('data-currentnumberofjobsdisplayed') is not None:
            displayed += int(soup.find('input').get('data-currentnumberofjobsdisplayed'))
        else:
            displayed = int(total)
        print displayed
        #calculating how much jobs left to display
        count = int(total) - int(displayed)
        # print count
        for sap in soup.findAll('span',{'class':'location'}):
            if sap.string.strip() is not None:
                locList.append(sap.string.encode('utf-8').strip())
            else:
                locList.append(None)
        for desc in soup.findAll('h3'):
            if desc.string is not None:
                descList.append(desc.string.encode('utf-8'))
            else:
                descList.append(None)
        for details in soup.findAll('div',{'class':'col-md-10'}):
            soup = BeautifulSoup(str(details),'html.parser')
            if len(soup.findAll('div',{'class':'job-detail-item'})) > 0:
                if soup.findAll('div',{'class':'job-detail-item'})[0].string.strip() is not None:
                    sectionList.append(soup.findAll('div',{'class':'job-detail-item'})[0].string.encode('utf-8').strip())
                else:
                    sectionList.append(None)
                if soup.findAll('div', {'class':'job-detail-item'})[2].string.strip() is not None:
                    timeList.append(soup.findAll('div', {'class':'job-detail-item'})[2].string.encode('utf-8').strip())
                else:
                    timeList.append(None)

    for le in range(0,len(locList)):
        dDict = {}
        dDict['Location'] = locList[le]
        dDict['Job_Description'] = descList[le]
        dDict['Job Section'] = sectionList[le]
        dDict['Job Timing'] = timeList[le]
        dList.append(dDict)


df = pd.DataFrame(dList)
df.to_csv('macys.csv', sep=',',index=False)

