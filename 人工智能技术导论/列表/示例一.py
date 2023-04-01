score = [75, 58, 96, 85, 68, 79, 90, 82, 43]
print("未排序：", score)
score.sort()
print("排序后：", score)
del score[0]
del score[-1]
print("去掉最高分和最低分：", score)

total_score = 0
for i in score:
    total_score += i

average_score = total_score / len(score)

print("平均分：%.2f" % average_score)
