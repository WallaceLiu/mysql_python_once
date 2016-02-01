# -*- coding: utf-8 -*-

from Biz_Base import Biz_Base
from mysql_python_once import MysqlPythonOnce
import CommonUtil
from CommonUtil import hostname
import mysql.connector
import datetime
import time

class Msg_Dest(Biz_Base):

    __tableName = "incoming"

    def __init__(self, db):
         Biz_Base.__init__(self, db)

    def insertMsg(self, clientIp, processingData, type):
        cnt = self.db.insert(self.__tableName, \
            clientIp = clientIp, \
            processingData = mysql.connector.Binary(processingData),\
            flag=0,\
            type=type,\
            createdBy=hostname() + '_py')
        return cnt > 0
