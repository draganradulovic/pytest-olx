import csv

def read_from_csv(fileName):
    rows = []
    dataFile=open(fileName, "r")
    reader=csv.reader(dataFile)
    print(reader)
    next(reader)

    for row in reader:
        rows.append(row)
    return rows


