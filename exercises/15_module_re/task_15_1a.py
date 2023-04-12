# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""


import re


def get_ip_from_cfg(filename):
    result = {}
    regex_intf = re.compile(r'^interface (\S+)')
    regex_ip = re.compile(r' ip address (\S+) (\S+)')
    with open(filename) as f:
        for line in f:
            match_intf = regex_intf.search(line)
            if match_intf:
                intf = match_intf.group(1)
            match_ip = regex_ip.search(line)
            if match_ip:
                ip = match_ip.group(1)
                mask = match_ip.group(2)
                result[intf] = (ip, mask)
    return result
