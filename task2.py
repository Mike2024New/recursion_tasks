"""
факториал числа, это число которое представляет собой произведение предыдущих положительных чисел, например:
f4 = 4*3*2*1 = 24
в данном случае самая простая операция это 1 (то есть это дно рекурсии)
в связи с чем в рекурсивной функции точкой выхода будет достижение значения 1
в функцию будет передаваться число x и из него последовательно будем отнимать по единице, пока оно
не станет равным 1, после на обратном стеке будем возвращать x умноженное на уменьшенное значение x
"""


def factorial(x):
    if x == 1:  # базовый случай если x равен 1, возвращаем 1
        return 1
    return x * factorial(x - 1)  # рекурсивный случай (уменьшение на 1, до тех пор пока x не равен 1)


"""
Стек вызовов (каждое смещение - следующий уровень вложенности):

factorial(x=4)
    factorial(x=3)
        factorial(x=2)
            factorial(x=1) | достигнута точка выхода (базовый случай) т.е. x == 1
            return 1 | в этой точке выхода возвращаем 1 (так как условие выполнено) 
        return 2 | x(1) * 2
    return 3 | x(2) * 3
return 4 | x(3) * 4
"""

res = factorial(4)
print(res)
