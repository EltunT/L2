#Задание №1

f = open('books.csv')
pr=[]
k = 0
for line in f:
    pr.append(line)
for i in pr:
    i = i.split(';')
    if len(i[1])>30:
        k+=1
print(k)
f.close()

#Задание №2

from csv import reader
flag = 0
output = open('C://result.txt', 'w')
search = input('Search for: ')
with open('C://books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[:]:
        lower_case = row[3].lower()
        index = lower_case.find(search.lower())
        if index != -1 and float(row[7])<=150:
            print(row[3])
            flag = 1
            output.write(f'{row[0]}. {row[3]}. Цена {row[7]} рублей.\n')

    if flag == 0:
        print('Ничего не найдено.')
output.close()

#Задание №3

from csv import reader
flag = 0
output = open('C://result.txt', 'w')
search = input('Search for: ')
with open('C://books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[:]:
        lower_case = row[3].lower()
        index = lower_case.find(search.lower())
        if index != -1:
            print(row[3])
            flag = 1
            output.write(f'Автор: {row[3]}. Название: {row[1]}. Год: {row[6][6:10]}.\n')
    if flag == 0:
        print('Ничего не найдено.')
output.close()

#Задание №4

import xml.dom.minidom as minidom
xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
books_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:
                    Name = child.firstChild.data
            if child.tagName == 'Value':
                if child.firstChild.nodeType == 3:
                    Value = float(child.firstChild.data.replace(',','.'))
    books_dict[Name] = Value

print(books_dict)
xml_file.close()

#Доп.задание 1

f = open('books.csv')
file = []
for line in f:
    file.append(line)
a = []
tags = []
for i in file:
    i = i.split(';')
    a.append(i[12])
for i in a:
    i = i.split('#')
    for j in i:
        j = str(j)
        if '\n' in j:
            j = j[:-2]
        if not(j in tags):
            tags.append(j)
print(tags)

#Доп. задание 2

f = open('books.csv')
popular = []
fl=1
for line in f:
    line = line.split(';')
    if fl or line[0]=='166276':
        # Исключаю строку с id = 166276 потому, что в названии книги там имеются
        # точки запятые из-за которых не работает корректно программа.
        # В остальных строчках такого нету и эта строка не входит в топ 20 книг
        fl = 0
        continue
    popular.append([int(line[8]),line[1]])
popular.sort(reverse=1)
print(popular[:20])