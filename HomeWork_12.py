'''
вариант 1
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
'''
import random
import os
from math import sqrt
def helpKaty(S, P):
    D = S * S - 4 * P
    resultX = 0
    if D < 0:
        print('Петя чего-то напутал')
    elif D == 0:
        resultX = S / 2
    else:
        resultX = (S + sqrt(D)) / 2
    resultY = S - resultX

    if (int(resultX)) == resultX and (int(resultY)) == resultY:
        print(f'{int(resultY):3} {int(resultX):3}')
    else:
        print('  Петя врет! цифры не целые', end='')
        print(f'({resultY:3.2f}  {resultX:3.2f})')

plan = [(4, 4),
        (5, 6),
        (9, 20),
        (15, 55),
        (31, 209),
        (28, 52),
        ]
print('   S    P       X   Y')
print('---- ----     --- ---')
for item in plan:
    S, P = item
    print(f'{S:4} {P:4}  -> ', end='')
    helpKaty(S, P)
'''
X	Y		S	P
5	4		9	20
7	8		15	56
20	11		31	220
2	26		28	52
'''
