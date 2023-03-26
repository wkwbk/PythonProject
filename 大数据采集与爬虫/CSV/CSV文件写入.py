import csv

with open('公司名单.csv', 'a', encoding='utf-8', newline='') as f:
    wr = csv.writer(f)
    wr.writerows([['软件999', '好公司都想去', '高级技术员', '学生会主席'], ['软件666', '都想去好公司', '中级技术员', '学生会部长']])
    wr.writerow(['软件555', '好公司都想去', '高级技术员', '学生会主席'])

with open('公司名单.csv', 'r', encoding='utf-8') as f2:
    r = csv.reader(f2)
    for row in r:
        print(row)
