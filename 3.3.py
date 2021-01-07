#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
a = int(input("Введите число №1: "))
b = int(input("Введите число №2: "))
c = int(input("Введите число №3: "))

def my_func(a, b, c):
    if a >= b and c >= b:
        return a + c
    elif a > c and b < a:
        return a + b
    else:
        return b + c
print(my_func(a, b, c))
