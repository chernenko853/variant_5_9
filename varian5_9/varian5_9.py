ACTION_PERMISSION = { #устанавливаем соотвествие разрешений символам (создание словаря), ключ read значение R
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}
#цикл ввода названий файлов, и разрешений, создание словаря с названиями файлов и разрешениями 
file_permissions = {}
for i in range(int(input())):#обозначение количества вводимых далее файлов
    file, *permissions = input().split()#ввод названий, с пробелами и символами разрешений, *premissions принимает 0 и более аргументов
    file_permissions[file] = set(permissions)#присвоение разрешений введенным файлам
 #цикл ввода названий файлов и проверки разрешений, вывод ОК или Access denied
for i in range(int(input())):
    action, file = input().split()
    #сравнение значений из словаря с введенными значениями, в зависимости от результата вывод
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')

