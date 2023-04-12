# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
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
                if intf in result:
                    result[intf].append((ip, mask))
                else:
                    result[intf] = [(ip, mask)]
    return result
