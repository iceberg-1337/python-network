# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""

from netmiko import ConnectHandler
from typing import List
from task_21_3 import parse_command_dynamic


def send_and_parse_show_command(
        device_dict: dict, command: str, templates_path: str, index: str = "index"
) -> List[dict]:
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command)

    attributes = {"Command": command, "Vendor": device_dict["device_type"]}
    result = parse_command_dynamic(output, attributes, index_file=index, templ_path=templates_path)

    return result