#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
while 1:
    i = input("Введите цифру")
    i = i.split(" ")
    a = 0
    while a < len(i):
        try:
            i[a] = int(i[a])
        except ValueError:
            print("Value Error")
            break
        a = a + 1
    z = 0
    for c in i:
        z = z + c
    print(z)
