import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time
from selenium.webdriver.common.keys import Keys
import urllib.request

chrome_path = r"C:\Users\Rajesh Sridhar\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.instagram.com/explore/tags/pandora/')
html_source = driver.page_source
# data = html_source.encode('utf-8')

time.sleep(1)

driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[3]/a""").click()

time.sleep(1)

elem = driver.find_element_by_tag_name("body")

no_of_pagedowns = 5000

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1

html_source = driver.page_source

soup = BeautifulSoup(html_source, "lxml")

# PostsData = []
urlList = []
dList = []

# for sap in soup.findAll('div', {'class': '_jjzlb'}):
#    sap2 = BeautifulSoup(str(sap), 'html.parser')
#    for sap3 in sap2.findAll('img'):
#        try:
#            PostsData.append(sap3['alt'])
#        except:
#            pass

for sapURL in soup.findAll('a', {'class': '_8mlbc _vbtk2 _t5r8b'}):
    try:
        urlList.append("http://www.instagram.com" + sapURL['href'])
    except:
        pass

lenList1 = len(urlList)

UserName = []
FullName = []
Caption = []
Nlikes = []
Nviews = []
Ncomments = []
PostingDate = []

for le in range(0, lenList1):

    try:
        catUrl = urlList[le]
        catRequest = urllib.request.Request(catUrl, headers={'content-type': 'application/json'})
        catResponse = urllib.request.urlopen(catRequest)

        catHtml = catResponse.read().decode('utf-8')

        soup = BeautifulSoup(catHtml, 'html.parser')

        for sap in soup.findAll('script', {'type': 'text/javascript'}):
            if sap.string is not None:
                if sap.string[0:18] == "window._sharedData":
                    with open("Output_File.txt", "w") as text_file:
                        text_file.write(sap.string[21:-1])

        with open('Output_File.txt', 'r') as fobj:
            data = json.load(fobj)

        with open('Output_JSON.json', 'w') as fobj:
            json.dump(data, fobj)
        try:
            if data['entry_data']['PostPage'][0]['media']['owner']['username'] is not None:
                UserName.append(data['entry_data']['PostPage'][0]['media']['owner']['username'])
            else:
                UserName.append("N/A")
        except KeyError:
            UserName.append("N/A")

        try:
            if data['entry_data']['PostPage'][0]['media']['owner']['full_name'] is not None:
                FullName.append(data['entry_data']['PostPage'][0]['media']['owner']['full_name'])
            else:
                FullName.append("N/A")
        except KeyError:
            FullName.append("N/A")

        try:
            if data['entry_data']['PostPage'][0]['media']['caption'] is not None:
                Caption.append(data['entry_data']['PostPage'][0]['media']['caption'])
            else:
                Caption.append("N/A")
        except KeyError:
            Caption.append("N/A")

        try:
            if data['entry_data']['PostPage'][0]['media']['likes']['count'] is not None:
                Nlikes.append(data['entry_data']['PostPage'][0]['media']['likes']['count'])
            else:
                Nlikes.append("N/A")
        except KeyError:
            Nlikes.append("N/A")

        try:
            if data['entry_data']['PostPage'][0]['media']['is_video'] == True:
                if data['entry_data']['PostPage'][0]['media']['video_views'] is not None:
                    Nviews.append(data['entry_data']['PostPage'][0]['media']['video_views'])
                else:
                    Nviews.append("N/A")
            else:
                Nviews.append(0)
        except KeyError:
            Nviews.append("N/A")

        try:
            if data['entry_data']['PostPage'][0]['media']['comments']['count'] is not None:
                Ncomments.append(data['entry_data']['PostPage'][0]['media']['comments']['count'])
            else:
                Ncomments.append("N/A")
        except KeyError:
            Ncomments.append("N/A")

        try:
            if data['entry_data']['PostPage'][0]['media']['date'] is not None:
                PostingDate.append(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(data['entry_data']['PostPage'][0]['media']['date'])))
            else:
                PostingDate.append("N/A")
        except KeyError:
            PostingDate.append("N/A")

    except:
        pass

lenList = len(Caption)

for le in range(0, lenList):
    dDict = {}

    dDict['Post Caption'] = Caption[le]
    # dDict['Link'] = urlList[le]
    dDict['User Name'] = UserName[le]
    dDict['Full Name'] = FullName[le]
    dDict['Number of likes'] = Nlikes[le]
    dDict['Number of Views'] = Nviews[le]
    dDict['Number of comments'] = Ncomments[le]
    dDict['Posting date'] = PostingDate[le]

    dList.append(dDict)

df = pd.DataFrame(dList)
df.to_csv('Pandora_new.csv', sep=',', index=False)

lenList = len(UserName)

dList = []

for le in range(0, lenList):
    dDict = {}
    dDict['User Name'] = UserName[le]
    dList.append(dDict)

df = pd.DataFrame(dList)
df.to_csv('Pandora_UserName.csv', sep=',', index=False)

dList = []

lenList = len(urlList)
for le in range(0, lenList):
    dDict = {}
    dDict['URL'] = urlList[le]
    dList.append(dDict)

df = pd.DataFrame(dList)
df.to_csv('Pandora_URL.csv', sep=',', index=False)