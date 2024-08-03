def sum_list(list_input: list) -> int or float:
    """
    Возвращает сумму всех элементов списка
    :param list_input: список элементы которого нужно сложить, в списке допустимы только int или float
    :return: сумма всех элементов списка
    ============================================
    Пример использования:
    sum_list(list_input=[100, -200, ]) # -> вернет 100
    ============================================
    Обрабатываемые исключения:
    ValueError:
        -вместо списка передан другой тип данных
    TypeError:
        -если в списке содержатся элементы не int или не float
    """
    if not isinstance(list_input, list):
        raise ValueError(f"входным типом объекта должен быть список(list) а передан тип: {type(list_input)}")
    if not all(isinstance(element, (float, int)) for element in list_input):
        raise TypeError(f"список должен содержать элементы только типов int или float")
    if not list_input:
        return 0  # базовый случай -> список стал пустым
    return list_input[-1] + sum_list(list_input[:-1])


"""
СТЕК ВЫЗОВОВ:
    входные данные: [1,2,3,4,5]
    sum_list([1,2,3,4,5])
        sum_list([1,2,3,4])
            sum_list([1,2,3])
                sum_list([1,2])
                    sum_list([1])
                        sum_list([]) |-> БАЗОВЫЙ СЛУЧАЙ (ВЫХОД ИЗ РЕКУРСИИ), длина списка равна 1
                        return 0
                    return 0 + 1 -> 1
                return 1 + 2 -> 3
            return 3 + 3 -> 6
        return 6 + 4 -> 10
    return 10 + 5 -> 15

    идея решения: рекурсивно уменьшаем список до полного опустошения (это и будет базовый случай рекурсии), 
    достигнув "дна", возвращаем сумму текущего и предыдущего элемента функции.
"""

if __name__ == '__main__':
    res = sum_list(list_input=[100, 200, 100.5])
    print(res)
