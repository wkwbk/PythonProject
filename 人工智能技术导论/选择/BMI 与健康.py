def bmiStandard():
    height = float(input("输入身高（米）："))
    weight = float(input("请输入体重（千克）"))
    bmi = round(weight/(height**2), 1)

    print("你的 BMI 为：", bmi)

    if bmi < 18.5:
        chinaStand = "偏瘦，相关疾病发病的危险性：低（但其他疾病危险性增加）"
    elif bmi < 24:
        chinaStand = "正常范围，相关疾病发病的危险性：平均水平"
    elif bmi < 28:
        chinaStand = "偏胖，相关疾病发病的危险性：增加"
    elif bmi < 30:
        chinaStand = "肥胖，相关疾病发病的危险性：中度增加"
    elif bmi < 40:
        chinaStand = "重度肥胖，相关疾病发病的危险性：严重增加"
    else:
        chinaStand = "极重度肥胖，相关疾病发病的危险性：非常严重增加"

    print(chinaStand)
