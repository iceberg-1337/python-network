# -*- coding: utf-8 -*-
"""
Задание 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM.
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt
и шаблоне templates/sh_ip_int_br.template.
"""


from textfsm import TextFSM
from io import StringIO


def parse_command_output(template, command_output):
    with open(template) as f:
        template_data = f.read()
    fsm = TextFSM(StringIO(template_data))
    result = fsm.ParseText(command_output)
    column_names = fsm.header
    rows = [list(row) for row in result]
    rows.insert(0, column_names)
    return rows


def parse_output_to_dict(template, command_output):
    rows = parse_command_output(template, command_output)
    column_names = rows[0]
    result = []
    for row in rows[1:]:
        row_dict = {}
        for i, value in enumerate(row):
            row_dict[column_names[i]] = value
        result.append(row_dict)
    return result


if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt") as f:
        output = f.read()
    result = parse_output_to_dict("templates/sh_ip_int_br.template", output)
    print(result)

