while True:
    i = int(input("请输入成绩（0~100）："))
    if i < 0 or i > 100:
        print("超出范围退出喽！")
        break
    else:
        print("没问题继续输入！")
