```python
# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
## *Пример:*
## A = 3; B = 5 -> 243 (3⁵)
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
print(f'A({a}) to the power of B({b}) is {pow(a, b)}')

```

```python
# Задача 28: Напишите рекурсивную функцию sum(a, b)
# , возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
## *Пример:*
## 2 2    4

def just_joke(x: int, y: int):
    if y == 0:
        return x
    return 1 + just_joke(x, y - 1)

a, b = [int(input(f'Please input number {x}: ')) for x in ('A', 'B')]
print(f'A({a}) plus B({b}) is {just_joke(a, b)}')

```
```python
# # Дана последовательность натуральных чисел (одно число в строке),
# # завершающаяся числом 0. Определите значение второго по величине элемента в этой последовательности,
# # то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.
# # В этой задаче нельзя использовать глобальные переменные.
# # Функция получает данные, считывая их с клавиатуры, а не получая их в виде параметра.
# # В программе на языке Python функция возвращает результат в виде кортежа из нескольких чисел
# # и функция вообще не получает никаких параметров. В программе на языке C++ результат записывается в
# # переменные, которые передаются в функцию по ссылке. \
# # Других параметров, кроме как используемых для возврата значения, функция не получает.
# # Гарантируется, что последовательность содержит хотя бы два числа (кроме нуля).
# #
# # 1 3 5 7 3 6 8 4 3 2 0 -> 7
# # # 1 2 3 4 5 6 3 1 2 5 3 -> 5
# #

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

def almost_bigger(almost=0, bigger=0):
    temp = input_num('please enter number: ')
    if temp == 0:
        return almost, bigger
    elif temp > bigger:
        almost = bigger
        bigger = temp
    elif temp > almost:
        almost = temp
    return almost_bigger(almost, bigger)

print(almost_bigger()[0])

```

```python
# # Даны натуральные числа k и s. Определите, сколько существует k-значных натуральных чисел,
# # сумма цифр которых равна s. Запись натурального числа не может начинаться с цифры 0.
# # В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.
# # 3 15 -> 69
# # 4 16 -> 564
# # 2 3 -> 3
# # 6, 40 ->10746
import time

k, s = [int(input(f'input {x}: ')) for x in ('k', 's')]
count = 0
start_time = time.time()
for k_numbers in range(10 ** (k - 1), int('9' * k)):
    if sum(map(int, str(k_numbers))) == s:
        count += 1
end_time = time.time()
print('we have', count, 'numbers')
print(end_time - start_time)

```