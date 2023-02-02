import os
os.system('cls')

import function as fn

expression = input('Введите числовое выражение,\n'
                    'состоящее из двух чисел и одного действия: ')
components = expression.split()
operation = fn.GetNameOfOperation(components[1])
result = fn.Operation(components[0], components[1], components[2])
print(f'Результат {operation}: {result}.')