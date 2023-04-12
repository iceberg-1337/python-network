# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""


import re


def parse_sh_ip_int_br(filename):
    result = []
    with open(filename) as f:
        for line in f:
            match = re.search(r'^(\S+)\s+'
                              r'([\d.]+|unassigned)\s+'
                              r'\S+\s+\S+\s+'
                              r'(up|down|administratively down)\s+'
                              r'(up|down)', line)
            if match:
                intf = match.group(1)
                ip_addr = match.group(2)
                status = match.group(3)
                protocol = match.group(4)
                result.append((intf, ip_addr, status, protocol))
    return result
