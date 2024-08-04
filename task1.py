# у рекурсии должен быть выход

def rec(x):
    if x < 4:
        print(x)  # эта строка отработает сразу
        rec(x + 1)  # рекурсивный случай
        print(x)  # эта строка будет работать только после отработки rec в строке выше


"""
стек вызовов для rec:
rec(x=1) | print(1)
    rec(x=2) | print(2)
        rec(x=3) | print(3)
            rec(x=4) -> точка выхода из рекурсии | базовый случай |-> x больше 4
        return 3 | print(3)
    return 2 | print(2)
return 1 | print(1)
"""


def rec2(a: int, test_list=None):
    """
    Пример списка накопителя значений из рекурсивной функции
    написан для того, чтобы понимать как внутри рекурсивной функции происходит накопление значений
    :param a: любое число больше 0
    :param test_list: список в который будут записываться числа
    :return: список с числами
    """
    if not test_list:
        test_list = []
    if a == 0:
        return test_list
    test_list.append(a)
    return rec2(a - 1, test_list)


"""
СТЕК ВЫЗОВОВ ДЛЯ rec2:
    пусть a=4 тогда:
    rec2(4)
        rec2(3)->[4]
            rec2(2)->[4,3]
                rec2(1)->[4,3,2]
                    rec2(0)->[4,3,2,1] |-> базовый случай a=0
                    return [4,3,2,1]
                return [4,3,2,1]
            return [4,3,2,1]
        return [4,3,2,1]
    return [4,3,2,1]
"""

res = rec2(10)
print(res)

if __name__ == '__main__':
    rec(1)
    # rec2(10)
