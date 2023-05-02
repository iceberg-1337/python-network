# -*- coding: utf-8 -*-

"""
Задание 23.1a

Скопировать и изменить класс IPAddress из задания 23.1.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""


class IPAddress:
    def __init__(self, ip_address):
        self.ip, mask = ip_address.split('/')
        if not self.is_correct_ip(self.ip):
            raise ValueError("Incorrect IPv4 address")
        if not self.is_correct_mask(mask):
            raise ValueError("Incorrect mask")
        self.mask = int(mask)

    @staticmethod
    def is_correct_ip(ip):
        octets = ip.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            if not octet.isdigit() or not 0 <= int(octet) <= 255:
                return False
        return True

    @staticmethod
    def is_correct_mask(mask):
        if not mask.isdigit() or not 8 <= int(mask) <= 32:
            return False
        return True

    def __str__(self):
        return f"IP address {self.ip}/{self.mask}"

    def __repr__(self):
        return f"IPAddress('{self.ip}/{self.mask}')"
