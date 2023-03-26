import math

savings = float(input("请输入你手头的闲钱（元）："))
target = float(input("请输入你的目标（元）："))
rate = float(input("请输入年利率（1年定期）："))/100

yearsSingle = math.ceil((target - savings) / (savings * rate))
yearsCompound = math.ceil(math.log(target/savings, 1+rate))
perDiff = (yearsCompound-yearsSingle)/yearsSingle

outStr = \
    "年利率：{} \n" \
    "手头有：{}元\n" \
    "单利需要：{}年\n" \
    "复利需要：{}年\n" \
    "能拿回：{}元\n" \
    "复利比单利在年数上要少：{}\n" \
    .format(rate, savings, yearsSingle, yearsCompound, target, perDiff)

print(outStr)
