def mul(*num):
    tot = 1
    for num in num:
        tot *= num
    return tot


print(mul(2, 3, 4, 5))
# print(num)
