import csv

def read_from_csv(fileName):
    rows = []
    dataFile=open(fileName, "r")
    reader=csv.reader(dataFile)
    print(reader)
    next(reader)
    print('**********************')
    for row in reader:
        print(row)
        rows.append(row)
    return rows


read_from_csv(r"C:\Users\User\PycharmProjects\letskodeit\utilities\negative_test_data.csv")