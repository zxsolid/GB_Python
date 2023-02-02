import os
os.system('cls')

import function as fn

expression = input('Введите числовое выражение: ')
components = expression.split()
multDiv = []

result = 0
for i in range(0, len(components) - 2, 2):
    if components[i + 1] == '*' or components[i + 1] == '/':
        result = fn.Operation(components[i], components[i + 1], components[i + 2])
        multDiv.append(str(result))
    else:
        multDiv.append(components[i])
        multDiv.append(components[i + 1])

print(multDiv)