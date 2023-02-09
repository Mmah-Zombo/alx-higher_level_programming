
# def pascal_trianle(n):
#     if n <= 0:
#         return 

def pascalT(n):
    lis = []
    lis2 = []
    finallisst = []
    num = 0

    if n <= 0:
        return lis

    for each in range(n):
        if each == 0 or each == n - 1:
            lis.append(1)
            lis2.append(1)
        else:
            num = lis2[each - 2] + lis2[each - 1]
        lis.append(num)
        lis2 = [a for a in lis]
        finallisst.append(lis)

    return finallisst

print(pascalT(3))