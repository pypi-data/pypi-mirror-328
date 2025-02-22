#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: MaJian
@Time: 2025/2/19 16:38
@SoftWare: PyCharm
@Project: mortal
@File: __init__.py.py
"""
from .sqlglot_main import MortalSQLGlotMain


class MortalSQLGlot(MortalSQLGlotMain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def format(self, sql):
        return self._format(sql)
    
    def parse(self, sql, dialect="mysql", callback="print"):
        return self._parse(sql, dialect, callback)
