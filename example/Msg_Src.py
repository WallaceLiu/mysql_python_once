# -*- coding: utf-8 -*-

from Biz_Base import Biz_Base
from mysql_python_once import MysqlPythonOnce

class Msg_Src(Biz_Base):

    __tableName = "incoming"

    def __init__(self, db):
         Biz_Base.__init__(self, db)

    def getMsg(self, id):
        sql_sel = "id=%s"
        msg = self.db.select(self.__tableName, \
            sql_sel, \
            'id', 'clientIp', 'processingData', 'type', \
            id = id)
        return msg

    def getMsgCollection(self, frm_id, to_id):
        sql_sel = "select `id`,`clientIp`,`processingData`,`type` from {0} where id>={1} and id<{2} order by id asc"
        sql_sel = sql_sel.format(self.__tableName,frm_id,to_id)
        msg = self.db.select_advanced(sql_sel)
        return msg;
