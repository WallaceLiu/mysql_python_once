# -*- coding: utf-8 -*-

from mysql_python_once import MysqlPythonOnce
import datetime
from Biz_Base import Biz_Base
import time
from CommonUtil import hostname

class Biz_Fence(Biz_Base):
    """
        fence 
    """

    __masterTableName = "tb_base_fence"
    __slaveTableName = 'tb_base_fence_point'

    def __init__(self, db):
         Biz_Base.__init__(self, db)

    def updateFenceOuterRadius(self, id, outerRadius):
        sql_update = "id=%s"
        cnt = self.db.update(self.__masterTableName,\
            sql_update,\
            id, \
            outside_radius = outerRadius,\
            update_time = time.strftime('%Y-%m-%d %X', time.localtime()),\
            update_by = hostname() + '_py')
        return cnt > 0

    def updateFenceInnerRadius(self, id, innerRadius):
        sql_update = "id=%s"
        cnt = self.db.update(self.__masterTableName,\
            sql_update,\
            id, \
            inside_radius=innerRadius,\
            update_time = time.strftime('%Y-%m-%d %X', time.localtime()),\
            update_by = hostname() + '_py')
        return cnt > 0

    def updateFenceRadius(self, id, outerRadius, innerRadius):
        sql_update = "id=%s"
        cnt = self.db.update(self.__masterTableName,\
            sql_update,\
            id, \
            inside_radius=innerRadius,\
            outside_radius = outerRadius,\
            update_time = time.strftime('%Y-%m-%d %X', time.localtime()),\
            update_by = hostname() + '_py')
        return cnt > 0

    def updateFenceLocation(self, id, lng, lat):
        sql_update = "id=%s"
        cnt = self.db.update(self.__slaveTableName,\
            sql_update,\
            id, \
            lng_baidu = lng, \
            lat_baidu =lat)
        return cnt > 0

    def updateFence(self, id, lng, lat, outerRadius, innerRadius):
        f = self.getFence(id)
        bl = self.updateFenceRadius(f[0][0], outerRadius,innerRadius)
        bl = self.updateFenceLocation(f[0][1], lng, lat)
        return bl

    def getFence(self, org_id):
        sql_sel = "SELECT \
                      t1.id, \
                      t2.id AS fid \
                    FROM \
                      tb_base_fence t1, \
                      tb_base_fence_point t2 \
                    WHERE t1.owner_id = %s  \
                      AND t1.id = t2.fence_id "
        f = self.db.select_advanced(sql_sel, ('owner_id', org_id))
        return f
