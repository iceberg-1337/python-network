# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

table = []

with open('CAM_table.txt', 'r') as f:
    for line in f:
        words = line.split()
        if words != [] and words[0].isdigit():
            words[0] = int(words[0])
            table.append(words)

vlan = int(input('Введите номер VLAN: '))

for words in sorted(table):
    if vlan == words[0]:
        print(f'{words[0]:<9}{words[1]:20}{words[3]}')