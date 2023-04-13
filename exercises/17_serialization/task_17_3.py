# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

import re

def parse_sh_cdp_neighbors(output):
    result = {}
    device = re.search(r'(\S+)>show', output).group(1)
    regex = re.compile(r'(?P<device>\S+)\s+(?P<local_intf>\S+ \S+)\s+\d+.* (?P<remote_intf>\S+ \S+)')
    matches = regex.finditer(output)
    device_dict = {}
    for match in matches:
        remote_device, local_intf, remote_intf = match.groups()
        device_dict[local_intf] = {remote_device: remote_intf}
        result[device] = device_dict
    return result
