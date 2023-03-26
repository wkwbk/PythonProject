import turtle

pen = turtle.Pen()

colorOfStar = input("请输入颜色：")
lengthOfSide = int(input("请输入长度："))

pen.color(colorOfStar)

for i in range(5):
    pen.forward(lengthOfSide)
    pen.right(144)

turtle.done()
