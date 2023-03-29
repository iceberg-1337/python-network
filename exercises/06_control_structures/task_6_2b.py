# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    ip = input('Введите IP-адрес: ')
    valid_ip = True

    for i in ip.split("."):
        if not i.isdigit() or not 0 <= int(i) <= 255 or i[0] == '0' and len(i) > 1 or len(ip.split(".")) != 4:
            valid_ip = False

    if valid_ip:
        break
    print('Неправильный IP-адрес')

first_byte = int(ip.split('.')[0])
if 1 <= first_byte <= 223:
    print('unicast')
elif 224 <= first_byte <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')