#1 Функция на заполнение массива случайными именами
import numpy as np
import random
from collections import Counter
MyNames = ['AMELIA','OLIVIA','EMILY','AVA','ISLA','JESSICA','POPPY','ISABELLA','SOPHIE','MIA','OLIVER','JACK','HARRY','JACOB','CHARLIE','THOMAS','OSCAR','WILLIAM','JAMES','GEORGE']
MyFunkName = []
def RamdomNames (x, *args):

    '''
    :param names: Массив всех Имён
    :param x: количество повторений
    :return: Заполненый массив случайными именами
    '''

    return(np.random.choice(*args, size=x, replace=True, p=None))

MyFunkName = RamdomNames(100 ,MyNames)
print(MyFunkName)
#2 Функция по выводу самого частого имени из массива

from collections import Counter
def Mostname(*args):
    '''
    :param args: в функцию передаётся массив имён
    :return: имя, которое чаще всего встречается в массиве
    '''
    return Counter(*args).most_common(1)

print(Mostname(MyFunkName))


#3 Функция по выводу самой редкой первой бувы в имени
def MyFirst(myarr):
    Mydict = {}
    My = []
    '''
    :param myarr: массив имён
    :return: самая редкая первая буква имени
    '''
    for i in myarr:
        if i[0] in Mydict:
            Mydict[i[0]] += 1
        else: Mydict[i[0]] = 1

    for key, values in Mydict.items():
        if values == min(Mydict.values()):
            My.append([key, values])

    return My

print(MyFirst(MyFunkName))

#4 обработка файла с логами
with open('log', mode = 'rt', encoding = 'utf-8') as MyFile:
    from datetime import datetime
    text = MyFile.read()
MyNew = []
MyNewall = []
MyDate = text.split('\n')
MyDate.remove('')
for i in MyDate:
    MyNew = i.split(',')
    MyNewall.append(MyNew[0])
MyNewall.sort(key=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'), reverse=True)
print('время последнего лога: ', MyNewall[0])







