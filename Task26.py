# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
def input_num(message: str) -> int:
    input_error: bool = True
    while input_error:
        try:
            temp = int(input(message))
        except ValueError:
            print("Вы ввели не число!")
        else:
            input_error = False
            return temp


def pow(x: int, y: int) -> int:
    if y < 2:
        return x
    return x * pow(x, y - 1)


a, b = input_num("input A: "), input_num("input B: ")
print(f'A to the power of B is {pow(a, b)}')
