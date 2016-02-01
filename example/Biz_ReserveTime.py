# -*- coding: utf-8 -*-

from mysql_python_once import MysqlPythonOnce
import datetime
from Biz_Base import Biz_Base
import uuid
from CommonUtil import hostname

class Biz_ReserveTime(Biz_Base):
    """
        reserve time 
    """

    __tableName = "tb_mzdtestdri_task"

    def __init__(self, db):
        Biz_Base.__init__(self, db)

    def insertReserveTime(self, car_id, obd_id, s_time, e_time):
        cnt = self.db.insert(self.__tableName,\
            id = str(uuid.uuid1()),\
            car_id = car_id, \
            type = 3,\
            explains = 'py',\
            task_status = 2,\
            auditing_result = 2,\
            start_time = s_time, \
            end_time = e_time, \
            operator = hostname() + '_py',\
            action_name = '通过审核')
        return cnt > 0
