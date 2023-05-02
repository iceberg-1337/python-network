# -*- coding: utf-8 -*-

"""
Задание 22.1a

Скопировать класс Topology из задания 22.1 и изменить его.

Перенести функциональность удаления "дублей" в метод _normalize.
При этом метод __init__ должен выглядеть таким образом:
"""


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        normalized = {}
        for key, value in topology_dict.items():
            if normalized.get(value) != key:
                normalized[key] = value
        return normalized


