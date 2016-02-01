# -*- coding: utf-8 -*-

from mysql_python_once import MysqlPythonOnce
import datetime
from Biz_Base import Biz_Base
import time
from CommonUtil import hostname

class Biz_CollectTime(Biz_Base):
    """
        collect time
    """

    __tableName = "tb_base_4s_shop"

    def __init__(self, db):
         Biz_Base.__init__(self, db)

    def updateCollectTime(self,id, s_time, e_time):
        sql_update = "id=%s"
        cnt = self.db.update(self.__tableName,\
            sql_update,\
            id, \
            TestDriveBeginTime = s_time, \
            TestDriveEndTime = e_time, \
            update_time = time.strftime('%Y-%m-%d %X', time.localtime()),\
            update_by = hostname() + '_py')
        return cnt > 0

    def updateFenceOuterRadius(self,id,radius):
        sql_update = "id=%s"
        cnt = self.db.update(self.__tableName,\
            sql_update,\
            id, \
            radius=radius)
        return cnt > 0

    def updateFenceInnerRadius(self,id,innerRadius):
        sql_update = "id=%s"
        cnt = self.db.update(self.__tableName,\
            sql_update,\
            id, \
            radius=innerRadius)
        return cnt > 0

    def updateFenceLocation(self,id,lng,lat):
        sql_update = "id=%s"
        cnt = self.db.update(self.__tableName,\
            sql_update,\
            id, \
            lng = lng, \
            lat =lat)
        return cnt > 0

    def updateFence(self,id,lng,lat,outerRadius,innerRadius):
        sql_update = "id=%s"
        cnt = self.db.update(self.__tableName,\
            sql_update,\
            id, \
            lng=lng, \
            lat=lat, \
            radius=outerRadius,\
            innerRadius=innerRadius)
        return cnt > 0
