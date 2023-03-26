total = 0
count = 0

while True:
    score = eval(input("请输入成绩（0~100，超出范围就退出）："))
    if score < 0 or score > 100:
        break
    total += score
    count += 1
