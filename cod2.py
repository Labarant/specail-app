print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

# Я ИЗВИНЯЮСЬ НО ВООБЩЕ НЕ ПОНЯТНО С ЭТИМИ СУММА РЯДА. 
# Я СКОПИРОВАЛ КОД ГОТОВЫЙ ДУМАЛ РАЗОБРАТЬ , ОБЫЧНО ПОЛУЧАЕТСЯ ПОНЯТЬ ОТ КУДА И ДЛЯ ЧЕГО НАЗНАЧАЛИСЬ ПРЕМЕНЫЕ , НО ТУТ ЖЕ ВСЕ ЗАПУТАНО . ХОЧЕТСЯ РАЗОБРАТЬ УЖЕ С ЭТИМИ ФОРМУЛАМИ ПОТОМУ  ЧТО ЗНАЮ ЭТО ОТКРОЕТ ПОНИМАНИЕ ЭТОГО ПРОЦЕСССА

equal = 1
number = 1
last = 0

def fact(x):
  factorial = 1
  for number in range(2, x + 1):
    factorial *= number
  return factorial

def pow(x, k):
  y = 1
  for i in range(k):
    y *= x
  return y


precision = float(input('Укажите точность: '))
x = float(input('Введите x: '))

while abs(equal - last) > precision:
  last = equal
  equal += (pow(x, number * 2) / fact(number * 2)) * (-1) ** number
  number += 1
print('Сумма ряда =', equal)

print('Ха-Ха')

