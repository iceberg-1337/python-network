# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""


import subprocess
import concurrent.futures

def ping_ip(ip):
    reply = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if reply.returncode == 0:
        return True
    else:
        return False


def ping_ip_addresses(ip_list, limit=3):
    access_list = []
    unreachable_list = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(ping_ip, ip_list)
        for ip, result in zip(ip_list, results):
            if result:
                access_list.append(ip)
            else:
                unreachable_list.append(ip)
    return access_list, unreachable_list
