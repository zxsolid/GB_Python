import os
import function as fn

menuitems = [
        ("1.", "Вывод автобусов"),
        ("2.", "Добавление автобуса"),
        ("3.", "Вывод водителей"),
        ("4.", "Добавление водителя"),
        ('5.', "Вывод маршрута"),
        ('6.', "Добавление маршрута"),
        ("7.", "Выход")]

os.system('cls')

print('МЕНЮ: ')
for point in menuitems:
    print(point[0], point[1])

routes = fn.ReadDataFromFile('route.txt')
m = routes[0]
n = m[2]
print(n)

number = input('Введите номер команды: ')
if number == '1':
    busData = fn.PrintBus()
    for data in busData:
        print(f'Id: {data[0]}, Госномер: {data[1]}')
elif number == '2':
    fn.AddBus()
elif number == '3':
    driverData = fn.PrintDriver()
    for data in driverData:
        print(f'Id: {data[0]}, ФИО водителя: {data[1]}')
elif number == '4':
    fn.AddDriver()
elif number == '5':
    dataRoute = fn.PrintRoute()
    for data in dataRoute:
        print(f'Id: {data[0]}, № автобуса: {data[1]}, id автобуса: {data[2]}, id водителя: {data[3]}')
    print(f'Имя водителя: {fn.GetDriver()}')
elif number == '6':
    fn.AddRoute()
elif number == '7':
    exit(0)