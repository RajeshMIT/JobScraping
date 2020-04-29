try:
    url = "http://customprinting.officedepot.com/CustomPrintingPrice.aspx"
    data = "__EVENTTARGET=cboItem&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTQ0MDQ3NTM4NA9kFgICAg9kFgYCAQ8PFgIeC05hdmlnYXRlVXJsBRpqYXZhc2NyaXB0OndpbmRvdy5jbG9zZSgpO2RkAgMPEGQQFRMMRXZlbnQgVGlja2V0C1Byb21vdGlvbmFsE0JhZGdlcy9MdWdnYWdlIFRhZ3MOQnVzaW5lc3MgQ2FyZHMSQnVzaW5lc3MgRW52ZWxvcGVzDkJ1c2luZXNzIEZvcm1zCUNhbGVuZGFycwlFbWJvc3NlcnMURW52ZWxvcGVzL0xldHRlcmhlYWQOR3JlZXRpbmcgQ2FyZHMXSW52aXRhdGlvbnMvIE5vdGUgQ2FyZHMGTGFiZWxzCU1hcmtldGluZwlNZW1vIFBhZHMNUG9zdC1pdCBOb3RlcwlQb3N0Y2FyZHMNU2F2ZSBUaGUgRGF0ZQ1TaWducy9CYW5uZXJzDVN0YW1wcy9EYXRlcnMVEwQzNjkxBDM2ODcEMzY5MgQxMDA2BDEwMDcEMTAwOAQxMDA5BDEwODIEMTAxNQQzNzk1BDEwMzkEMTAxMAQzODI0BDEwMTcEMTAyMwQxMDIyBDM3MzAEMzc2NQQxMDI4FCsDE2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIFD2QWBAIBDzwrABECAA8WAh4LXyFJdGVtQ291bnQCB2QMFCsABhYIHgROYW1lBQhRdWFudGl0eR4KSXNSZWFkT25seWgeBFR5cGUZKwIeCURhdGFGaWVsZAUIUXVhbnRpdHkWCB8CBR1GdWxsIENvbG9yIEZvcm0sIDItUGFydDIgUGFydB8DaB8EGSsCHwUFHUZ1bGwgQ29sb3IgRm9ybSwgMi1QYXJ0MiBQYXJ0FggfAgUdRnVsbCBDb2xvciBGb3JtLCAzLVBhcnQzIFBhcnQfA2gfBBkrAh8FBR1GdWxsIENvbG9yIEZvcm0sIDMtUGFydDMgUGFydBYIHwIFHENvbnNlY3V0aXZlIE51bWJlcmluZyBDaGFyZ2UfA2gfBBkrAh8FBRxDb25zZWN1dGl2ZSBOdW1iZXJpbmcgQ2hhcmdlFggfAgUIRGVsaXZlcnkfA2gfBBkrAh8FBQhEZWxpdmVyeRYIHwIFDkFydHdvcmsgVXBsb2FkHwNoHwQZKwIfBQUOQXJ0d29yayBVcGxvYWRkAgMPPCsAEQIADxYCHwECCGQMFCsABxYIHwIFCFF1YW50aXR5HwNoHwQZKwIfBQUIUXVhbnRpdHkWCB8CBQVQcmljZR8DaB8EGSsCHwUFBVByaWNlFggfAgUUQmxhbmsgT3V0ZXIgRW52ZWxvcGUfA2gfBBkrAh8FBRRCbGFuayBPdXRlciBFbnZlbG9wZRYIHwIFMFByaW50ZWQgU3RhbmRhcmQgRW52ZWxvcGUgUmVzcG9uZCBBZGRyZXNzIC0gRWNydR8DaB8EGSsCHwUFMFByaW50ZWQgU3RhbmRhcmQgRW52ZWxvcGUgUmVzcG9uZCBBZGRyZXNzIC0gRWNydRYIHwIFL1ByaW50ZWQgU3RhbmRhcmQgRW52ZWxvcGUgUmV0dXJuIEFkZHJlc3MgLSBFY3J1HwNoHwQZKwIfBQUvUHJpbnRlZCBTdGFuZGFyZCBFbnZlbG9wZSBSZXR1cm4gQWRkcmVzcyAtIEVjcnUWCB8CBQhEZWxpdmVyeR8DaB8EGSsCHwUFCERlbGl2ZXJ5FggfAgUOQXJ0d29yayBVcGxvYWQfA2gfBBkrAh8FBQ5BcnR3b3JrIFVwbG9hZGQYAgUFY3RsMDUPPCsADAEIAgFkBQVjdGwwNA88KwAMAQgCAWSvXXSYj%2FQtauwA7j77rSNNOvjcyg%3D%3D&__VIEWSTATEGENERATOR=1905A3D9&__EVENTVALIDATION=%2FwEdABUZ%2BHbcxXuL7iTkYjvhr2da0zqf6Z3ayNHoJNG9f0ctDhlZPjCu7Mk%2B3VfQw%2Fyl%2FYtz33xCw4eZ0tuEcAQ61UEr9II3ZJYpcEnng1FbWDELkm%2B6wjKedytIvvKOdbbSQwC8HSqzPrQnxH3UgQeUfZNwRU6oVbcaU7LHmZka%2FR3RjIoCoVbWWb8S4S0Ryh6XT6GWjpDAGs6RJ3RmhbtXrk%2Bnx8L1Mw5duR3SffcC3Ok6%2BkhM%2Ft4MGKDo4lNeyPfSpObo6p6ItE98NUqVdIws63xhnst8PN99ZErhfBM8ZozkKMI3M%2FHZ1FJfxPZXX5xi3MHUqalSbUwprfkCzYMXBLtdnTdIhZxuVFZ4r1AfD%2FUevxMTNFKJibxAWttKf7pJewNjCSUxjXwYNJyHjcYTSRQbFf5ITKrhjFu9OxiWLW2O92V%2FfA2EJvrmA7B952eIA%2BSu8Q5ApkS%2FXBC%2BTgs%2FUVTluD%2FCxQ%3D%3D&cboItem=1039"
    request = urllib2.Request(url=url,data=data)
    response = urllib2.urlopen(request)
    html = response.read()
except urllib2.URLError:
    pass

soup = BeautifulSoup(html,'html.parser')
tables = soup.find_all('table', attrs = {'class':'PriceGrid'})

list1 = tables[0].find_all('td')

Quantity = []
for i in range(6,len(list1),6):
	Quantity.append(list1[i].text.replace('/td','').replace(",",""))

List_Price = []
for i in range(7,len(list1),6):
    List_Price.append(list1[i].text.replace('/td','').replace('$','').replace(",",""))

data= []
for i in range(0,len(Quantity)):
    data.append([Quantity[i],List_Price[i]])

od_invitation = []
od_invitation_actual = []
od_invitation_discounted = []
for i in range(0,len(data)):
    od_invitation_actual.append(['National',\
                                 'Cards & Invitations',\
                                 '"Basic Ecru Invitations" w/ Ecru Envelopes( 5 1/2" W x 7 3/4" H )',\
                                 'Actual',\
                                 data[i][0].encode('ascii','replace'),\
                                 'Office Depot',\
                                 data[i][1].encode('ascii','replace'),\
                                 time.strftime('%d-%m-%Y'),\
                                 '5 x 7 - Basic'])

for i in range(0,len(data)):
    od_invitation_discounted.append(['National',\
                                     'Cards & Invitations', \
									 '"Basic Ecru Invitations" w/ Ecru Envelopes( 5 1/2" W x 7 3/4" H )',\
                                     'Discounted',\
                                     data[i][0].encode('ascii','replace'),\
                                     'Office Depot',\
                                     0,\
                                     time.strftime('%d-%m-%Y'),\
                                     '5 x 7 - Basic'])

od_invitation = od_invitation_actual + od_invitation_discounted