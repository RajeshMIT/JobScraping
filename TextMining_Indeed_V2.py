# Categorisation of job data from the job title
__author__ = "Rajesh"

import pandas as pd
import csv
import os

owd = os.getcwd()

#dir_path = os.path.dirname(os.path.realpath("TextMining_Indeed_V2.ipynb"))

if not os.path.exists("JobsCategorized"):
    os.makedirs("JobsCategorized")

dir_path = os.path.dirname("JobsCategorized")

csv_file = open('in_15000.csv', encoding="utf8")
csv_data = csv.reader(csv_file)
next(csv_data, None)

jobTitle = []
jobOrg = []
jobDate = []
jobLoc = []
jobDesc = []
jobLink = []

dList = []
seen = set()

for row in csv_data:
    check = row[3] + row[0] + row[5]
    if check not in seen:
        seen.add(check)
        jobOrg.append(row[0])
        jobDesc.append(row[1])
        jobDate.append(row[2])
        jobTitle.append(row[3])
        jobLink.append(row[4])
        jobLoc.append(row[5])

csv_file = open('ind_15-25000.csv', encoding="utf8")
csv_data = csv.reader(csv_file)
next(csv_data, None)

for row in csv_data:
    check = row[3] + row[0] + row[5]
    if check not in seen:
        seen.add(check)
        jobOrg.append(row[0])
        jobDesc.append(row[1])
        jobDate.append(row[2])
        jobTitle.append(row[3])
        jobLink.append(row[4])
        jobLoc.append(row[5])

csv_file = open('ind_25 - 35000.csv', encoding="utf8")
csv_data = csv.reader(csv_file)
next(csv_data, None)

for row in csv_data:
    check = row[3] + row[0] + row[5]
    if check not in seen:
        seen.add(check)
        jobOrg.append(row[0])
        jobDesc.append(row[1])
        jobDate.append(row[2])
        jobTitle.append(row[3])
        jobLink.append(row[4])
        jobLoc.append(row[5])

retail_words = ["customer", "Customer", "sales", "Sales", "representative", "Representative", "retail", "Retail",
                "cashier", "Cashier", "merchandiser", "Merchandiser"]
restaurant_words = ["barista", "Barista", "bartender", "Bartender", "waiter", "Waiter", "busser", "Busser", "food",
                    "Food", "restaurant", "Restaurant", "mess", "Mess", "dishwasher", "Dishwasher", "buser", "chef",
                    "cook", "Buser", "Chef", "Cook", "Server", "server", "Dining", "dining", "baker", "Baker", "coffee",
                    "Coffee", "banquet", "Banquet", "catering", "Catering", "pastry", "Pastry", "culinary", "Culinary"]
accountant_words = ["accountant", "Accountant", "accounting", "Accounting", "biller", "Biller", "payroll", "Payroll"]
pharma_words = ["pharmacist", "Pharmacist", "chemist", "Chemist"]
admin_words = ["administrative", "Administrative", "clerk", "Clerk", "clerical", "Clerical", "receptionist",
               "Receptionist", "admin", "Admin"]
auto_words = ["automotive", "Automotive", "auto", "Auto", "mechanic", "Mechanic"]
bank_words = ["teller", "Teller"]
build_words = ["concierge", "Concierge", "cleaner", "Cleaner", "janitor", "Janitor", "housekeeper", "Housekeeper",
               "housekeeping", "Housekeeping", "Maintenance", "maintenance", "lawn", "Lawn", "HVAC"]
transpo_words = ["Driver", "driver", "Bus", "bus", "CDL", "Roller", "roller", "Paver", "paver", "steward", "Steward",
                 "transportation", "Transportation"]
recreation_words = ["Lifeguard", "lifeguard", "gym", "Gym"]

CatList = []

for job in jobTitle:

    count_retail = 0
    count_res = 0
    count_acc = 0
    count_pharma = 0
    count_admin = 0
    count_auto = 0
    count_bank = 0
    count_build = 0
    count_transpo = 0
    count_recre = 0

    words = job.split(' ')

    for word in words:
        if word in retail_words:
            count_retail = count_retail + 1
        if word in restaurant_words:
            count_res = count_res + 1
        if word in accountant_words:
            count_acc = count_acc + 1
        if word in pharma_words:
            count_pharma = count_pharma + 1
        if word in admin_words:
            count_admin = count_admin + 1
        if word in auto_words:
            count_auto = count_auto + 1
        if word in bank_words:
            count_bank = count_bank + 1
        if word in build_words:
            count_build = count_build + 1
        if word in transpo_words:
            count_transpo = count_transpo + 1
        if word in recreation_words:
            count_recre = count_recre + 1

    max_val = count_retail

    if count_res > max_val:
        max_val = count_res

    if count_acc > max_val:
        max_val = count_acc

    if count_pharma > max_val:
        max_val = count_pharma

    if count_admin > max_val:
        max_val = count_admin

    if count_auto > max_val:
        max_val = count_auto

    if count_bank > max_val:
        max_val = count_bank

    if count_build > max_val:
        max_val = count_build

    if count_transpo > max_val:
        max_val = count_transpo

    if count_recre > max_val:
        max_val = count_recre

    if count_retail == max_val:
        CatList.append("Retail")
    elif count_res == max_val:
        CatList.append("Restaurant")
    elif count_acc == max_val:
        CatList.append("Accounting")
    elif count_pharma == max_val:
        CatList.append("Pharmaceutical")
    elif count_admin == max_val:
        CatList.append("Administrative and Clerical")
    elif count_auto == max_val:
        CatList.append("Automotive")
    elif count_bank == max_val:
        CatList.append("Retail Banking")
    elif count_build == max_val:
        CatList.append("Building Services and Maintenance")
    elif count_transpo == max_val:
        CatList.append("Transportation Services")
    elif count_recre == max_val:
        CatList.append("Recreation")
    else:
        CatList.append("Not applicable")

lenList = len(CatList)

for le in range(0, lenList):
    dDict = {}
    dDict['Title'] = jobTitle[le]
    dDict['Job Category'] = CatList[le]
    dDict['Company'] = jobOrg[le]
    dDict['Location'] = jobLoc[le]
    dDict['Date Posted'] = jobDate[le]
    dDict['Job_Description'] = jobDesc[le]
    dDict['Job link'] = jobLink[le]

    dList.append(dDict)

df = pd.DataFrame(dList)

os.chdir("JobsCategorized")

df.to_csv('Indeed_cat.csv', sep=',', index=False)

os.chdir(owd)