from random import randint
from time import time

while True:
    ans = input("是否开始测试（y/n）：")
    if ans != "y" and ans != "n":
        print("输入错误，请重新输入")
    if ans == "y":
        print("测试开始……")
        countRight = 0
        numOfQues = int(input("输入本次小测的题目数："))

        print("开始计时……")
        startSec = time()

        for rp in range(numOfQues):
            number1 = randint(10, 99)
            number2 = randint(10, 99)
            ansRight = number1 + number2
            question = "{} + {} = ".format(number1, number2)
            print(question, end="")
            ansQues = int(input())

            if ansQues == ansRight:
                countRight += 1

        endSec = time()
        print("结束计时……")

        result = "本次测试 {} 题，答对了 {} 道题，用时 {:.2f} 秒，正确率为 {:.2%}。".format(numOfQues, countRight, endSec - startSec, countRight/numOfQues)
        print(result)
        print("-------------------- 本次测试结束 --------------------")
    if ans == "n":
        print("测试结束……")
        break
