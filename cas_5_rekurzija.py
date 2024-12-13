# factoriel = 1
#
# n = int(input("vnesi eden broj za koj sto sakas da presmetas faktoriel: "))
#
# for i in range(1, n + 1):
#     factoriel = factoriel * i
#
# print(factoriel)


# def find_fac(n):
#     if n == 1:
#         return 1
#     return n * find_fac(n-1)
#
#
# print(f"faktoriel od 4 iznesuva: {find_fac(4)}")

















# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n-1)
#
# # print("power: 2^2", power(2, 2))
# print("power: 2^2", power(2, 8))
#
# rez = 1
# for i in range(1, 9):
#     rez = rez * 2
#
# print(rez)



def power (x,n):
    if n==0:
        return 1
    if n<0:
        return 1/power(x, -n)
    return x * power(x, n-1)

result = power(2,-5)
print(f" {2}^{-5} e: {result}")