import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import json

# from selenium import webdriver
# chrome_path = r"C:\Users\Rajesh Sridhar\Downloads\chromedriver.exe"
# driver = webdriver.Chrome(chrome_path)
# driver.get('https://www.instagram.com/explore/tags/pandora/')
# driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[3]/a""").click()

catUrl = 'https://www.instagram.com/explore/tags/pandora/'
catRequest = urllib.request.Request(catUrl)
catResponse = urllib.request.urlopen(catRequest)

catHtml = catResponse.read().decode('utf-8')

soup = BeautifulSoup(catHtml, 'html.parser')

for sap in soup.findAll('script', {'type': 'text/javascript'}):
    if sap.string is not None:
        if sap.string[0:18] == "window._sharedData":
            #print(sap.string[21:-1])
            with open("Output.txt", "w") as text_file:
                text_file.write(sap.string[21:-1])

with open('Output.txt', 'r') as fobj:
    data = json.load(fobj)

with open('Output2.json', 'w') as fobj:
    json.dump(data, fobj)

with open('Output2.json') as data_file:
    data = json.load(data_file)


dList = []

for i in range(0,15):
    dDict = {}
    dDict['Caption'] = data['entry_data']['TagPage'][0]['tag']['media']['nodes'][i]['caption']
    dDict['Owner ID'] = data['entry_data']['TagPage'][0]['tag']['media']['nodes'][i]['owner']['id']
    dDict['Number of likes'] = data['entry_data']['TagPage'][0]['tag']['media']['nodes'][i]['likes']['count']

    dList.append(dDict)



df = pd.DataFrame(dList)
df.to_csv('Insta.csv', sep=',',index=False)