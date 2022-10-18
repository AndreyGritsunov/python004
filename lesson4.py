n= int(input("Введите любое число: "))
m = 0
while (n != 0):
    m = m + n % 10
    n = n // 10
print("Сумма равна: ", m)