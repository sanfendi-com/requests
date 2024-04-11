#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: test_mapping.py
Author: 提昂(zsc1528@gmail.com)
Date: 2024/4/11 15:29
Copyright: 三分地信息技术有限公司
"""
from typing import Dict
from collections.abc import Mapping, MutableMapping


def process_mapping(data):
    """
    examples
    """
    if isinstance(data, Mapping):
        for k, v in data.items():
            print(f"key: {k}, value: {v}")
    else:
        print("Data is not a Mapping")


class CustomMapping(MutableMapping):
    def __init__(self, data: Dict):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._data})"


class CaseInsensitiveMapping(MutableMapping):
    def __init__(self, data):
        self._data = {key.lower(): value for key, value in data.items()}

    def __getitem__(self, key):
        return self._data[key.lower()]

    def __setitem__(self, key, value):
        self._data[key.lower()] = value

    def __delitem__(self, key):
        del self._data[key.lower()]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        """
        repr
        """
        return f"{self.__class__.__name__}({self._data})"


def test_mapping():
    my_dict = {"name": "John", "age": 30}
    process_mapping(my_dict)
    my_list = [1, 2, 3]
    process_mapping(my_list)


def test_custom_mapping():
    data = {"name": "John", "age": 30, "address": "北京"}
    custom_mapping = CustomMapping(data)
    setattr(custom_mapping, "phone", 1234567)
    # custom_mapping.phone = 1234567
    print(custom_mapping)
    print(custom_mapping.__dict__)


def test_caseinsensitive_mapping_demo():
    """
    case insensitive mapping demo
    """
    case_insensitive_mapping = CaseInsensitiveMapping({"Name": "John", "Age": 30})
    print(case_insensitive_mapping)
    case_insensitive_mapping.phone = 888
    print(case_insensitive_mapping.phone)
    print(repr(case_insensitive_mapping))


