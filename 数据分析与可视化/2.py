import math

for i in range(101, 201):
    is_prime = True
    temp = int(math.sqrt(i)) + 1
    for j in range(2, temp):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
