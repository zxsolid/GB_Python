def IfNumber(line):
    array = list(line)
    for element in array:
        if ord(element) < 48 and ord(element) != 46 or ord(element) > 57:
            return False
    return True


def IfArithmeticSign(symbol):
    if len(symbol) != 1:
        return False
    else:
        if ord(symbol) != 42 and ord(symbol) != 43 and ord(symbol) != 45 and ord(symbol) != 47:
            return False
    return True


def GetNameOfOperation(symbol):
    if IfArithmeticSign(symbol):
        if symbol == '+':
            return 'сложения'
        elif symbol == '-':
            return 'вычитания'
        elif symbol == '*':
            return 'умножения'
        elif symbol == '/':
            return 'деления'
    else:
        return 'несуществующий символ'


def Operation(a, b, c):
    if IfNumber(a) and IfNumber(c) and IfArithmeticSign(b):
        if b == '+':
            return (float(a) + float(c))
        elif b == '-':
            return (float(a) - float(c))
        elif b == '*':
            return (float(a) * float(c))
        elif b == '/':
            return (float(a) / float(c))
    else:
        return 'Некорректный ввод данных. Повторите попытку'