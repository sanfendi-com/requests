#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: test_structures.py
Author: 提昂(zsc1528@gmail.com)
Date: 2024/4/11 14:49
Copyright: 三分地信息技术有限公司
"""
import pytest

from requests.structures import CaseInsensitiveDict
from requests.structures import LookupDict


class TestCaseInsensitiveDict(object):
    @pytest.fixture(autouse=True)
    def setup(self):
        """CaseInsensitiveDict instance with "Accept" header"""
        self.case_insensitive_dict = CaseInsensitiveDict()
        self.case_insensitive_dict["Accept"] = "application/json"

    def test_list(self):
        assert list(self.case_insensitive_dict) == ["Accept"]



