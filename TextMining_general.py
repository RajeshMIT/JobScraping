# Categorisation of job data from the job title
__author__ = "Rajesh"

import pandas as pd
import csv
import os

owd = os.getcwd()

jobTitle = []
jobOrg = []
jobDate = []
jobLoc = []
jobDesc = []
jobType = []
jobSalary = []

dList = []
CatList = []

seen = set()

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

if not os.path.exists("JobsCategorized"):
    os.makedirs("JobsCategorized")

for filename in os.listdir(owd + '\CSV\\'):

    ind_com = -1
    ind_loc = -1
    ind_date = -1
    ind_title = -1
    ind_desc = -1
    ind_type = -1
    ind_salary = -1

    if filename.endswith(".csv"):
        try:
            csv_file = open(owd + '\CSV\\' + filename, encoding="ascii", errors="surrogateescape")
        except:
            pass

        csv_data = csv.reader(csv_file)
        row1 = next(csv_data, None)

        for elem in row1:
            elem_words = elem.split(' ')
            for word_val in elem_words:
                if word_val in ["Company", "Organization"]:
                    ind_com = row1.index(elem)
                    break
                if word_val in ["Title"]:
                    ind_title = row1.index(elem)
                    break
                if word_val in ["Location", "City"]:
                    ind_loc = row1.index(elem)
                    break
                if word_val in ["Salary", "Compensation"]:
                    ind_salary = row1.index(elem)
                    break
                if word_val in ["Date"]:
                    ind_date = row1.index(elem)
                    break
                if word_val in ["Description", "Summary"]:
                    ind_desc = row1.index(elem)
                    break
                if word_val in ["Type"]:
                    ind_type = row1.index(elem)
                    break

        for row in csv_data:
            if ind_com == -1:
                if ind_loc == -1:
                    check = row[ind_title] + filename.split('.')[0]
                else:
                    check = row[ind_title] + filename.split('.')[0] + row[ind_loc]
            else:
                if ind_loc == -1:
                    check = row[ind_title] + row[ind_com]
                else:
                    check = row[ind_title] + row[ind_com] + row[ind_loc]

            if check not in seen:
                seen.add(check)

                if ind_com == -1:
                    jobOrg.append(filename.split('.')[0])
                else:
                    jobOrg.append(row[ind_com])

                if ind_loc > -1:
                    jobLoc.append(row[ind_loc])
                else:
                    jobLoc.append("N/A")

                if ind_date > -1:
                    jobDate.append(row[ind_date])
                else:
                    jobDate.append("N/A")

                if ind_title > -1:
                    jobTitle.append(row[ind_title])
                else:
                    jobTitle.append("N/A")

                if ind_desc > -1:
                    jobDesc.append(row[ind_desc])
                else:
                    jobDesc.append("N/A")

                if ind_type > -1:
                    jobType.append(row[ind_type])
                else:
                    jobType.append("N/A")
                if ind_salary > -1:
                    jobSalary.append(row[ind_salary])
                else:
                    jobSalary.append("N/A")

        continue
    else:
        continue

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
    dDict['Job Type'] = jobType[le]
    dDict['Salary Estimate'] = jobSalary[le]

    dList.append(dDict)

df = pd.DataFrame(dList)

os.chdir("JobsCategorized")

df.to_csv('Jobs_Cat.csv', sep=',', index=False)

os.chdir(owd)