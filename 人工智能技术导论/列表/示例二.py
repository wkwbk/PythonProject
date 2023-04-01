shop_list = ["联想电脑", "小米手环", "袜子", "荒岛余生"]
print("我要买", len(shop_list), "件商品。")
print("这些东西分别是：")
for item in shop_list:
    print(item)

new_item = input("我还要购买的商品：")
shop_list.append(new_item)
print("我的购物清单分别是：", shop_list)

print("我买的第一件商品是：", shop_list[0])
old_item = shop_list[0]
del shop_list[0]
print("我的购物清单现在是：", shop_list)
print("我过去买过：", old_item)
