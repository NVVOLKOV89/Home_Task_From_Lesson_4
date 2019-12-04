#1 Функция на заполнение массива случайными именами
import numpy as np
import random
from functools import reduce
from collections import Counter
MyNames = ['AMELIA','OLIVIA','EMILY','AVA','ISLA','JESSICA','POPPY','ISABELLA','SOPHIE','MIA','OLIVER','JACK','HARRY','JACOB','CHARLIE','THOMAS','OSCAR','WILLIAM','JAMES','GEORGE']
print(MyNames)
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








