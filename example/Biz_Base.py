# -*- coding: utf-8 -*-

from LoadConf import LoadConf
from mysql_python_once import MysqlPythonOnce

class Biz_Base(object):

    def __init__(self, db):
        self.db = db
