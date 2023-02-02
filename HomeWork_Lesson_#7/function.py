import os

def ReadDataFromFile(name):
    rawdata_list = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            rawdata_list.append(line.strip('\n').split(','))
        return rawdata_list

def SaveDataToFile(name, command):
    with open(name, 'a', encoding = 'utf8') as datafile:
        datafile.write(command + '\n')

def PrintBus():
    os.system('cls')
    print('Сведения об автобусах:')
    return ReadDataFromFile('bus.txt')

def AddBus():
    os.system('cls')
    return SaveDataToFile('bus.txt', input('Введите данные автобуса: '))

def PrintDriver():
    os.system('cls')
    print('Сведения о водителях:')
    return ReadDataFromFile('driver.txt')

def AddDriver():
    os.system('cls')
    return SaveDataToFile('driver.txt', input('Введите данные вводителя: '))

def PrintRoute():
    os.system('cls')
    print('Сведения о маршрутах:')
    return ReadDataFromFile('route.txt')

def AddRoute():
    os.system('cls')
    return SaveDataToFile('route.txt', input('Введите данные маршрута: '))

def GetDriver():
    txt = input('Введите id водителя, курсирующего по соответствующему маршруту: ')
    drivers = ReadDataFromFile('driver.txt')
    i = 0
    k = -1
    while i < len(drivers):
        if txt in drivers[i][0]:
            k = i
        i = i + 1
    return drivers[k][1]