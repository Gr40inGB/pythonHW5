# Задача 28: Напишите рекурсивную функцию sum(a, b)
# , возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2    4

def just_joke(x: int, y: int):
    if y == 0:
        return x
    return 1 + just_joke(x, y - 1)


a, b = [int(input(f'Please input number {x}: ')) for x in ('A', 'B')]
print(f'A({a}) plus B({b}) is {just_joke(a, b)}')
