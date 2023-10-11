import openpyxl
from datetime import datetime

today = datetime.now()
today = str(today)
today = today[:-10]
today = today.replace(" ", "").replace(":", "").replace("-", "")


def main(data):
    # Call a Workbook() function of openpyxl
    # to create a new blank Workbook object
    wb = openpyxl.Workbook()

    sheet = wb.active

    for datas in data:
        sheet.append(datas)

    wb.save("records/"+today+".xlsx")
    # wb.save("abc.xlsx")
    print("excel created")

#main((("1","kanniaha","cs"),("2","nitish","cs")))