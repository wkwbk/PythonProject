import csv

filetouse = "公司名单.csv"
with open(filetouse, 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    file_header = next(r)
    print(file_header)

    for id, file_header_col in enumerate(file_header):
        print(id, file_header_col)

    for row in r:
        if row[3] == "团支书":
            print(row)
