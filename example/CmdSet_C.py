# -*- coding: utf-8 -*-

from CmdBase import CmdBase
import string
from Biz_CollectTime import Biz_CollectTime
from ErrorCommandFormat import ErrorCommandFormat
import Biz_Base

class CmdSet_C(CmdBase):
    """
        set command.

        Command Format :
        set <[c|collect]> <org id>=<[-,-]>
    """
    __b_time = None   # begin time
    __e_time = None   # end time
    __biz_collectTime = None

    def __init__(self, params, db):
        self.id = ""
        self.name = "set command" 
        self.params = params
        self.cmd = "SET"
        self.type = "collect"
        __biz_collectTime = Biz_CollectTime(db)

        self.validate()

    def validate(self):
        p = str.split(self.params[2],'=')

        if len(p) != 2:
            raise ErrorCommandFormat("Command Params Error : set <[c|collect]> <org id>=<-,->")
        else:
            org_id = p[0]
            b_e_times = str.split(p[1],',')

            if len(b_e_times) == 2 :
                self.id = org_id
                self.__b_time = None  if b_e_times[0] == "-" else b_e_times[0]
                self.__e_time = None  if b_e_times[1] == "-" else b_e_times[1]
            else:
                raise ErrorCommandFormat("Command Params Error : set <[c|collect]> <org id>=<-,->")

    def execute(self):
        print(self.cmd + 'UPDATE COLLECT TIME' + ',SHOPID=' + self.id + \
            ',BEGINTIME=' + self.__b_time + \
            ',ENDTIME=' + self.__e_time + '...')
        bl = self.__biz_collectTime.updateCollectTime(self.id, self.__b_time, self.__e_time)
        print(bl)
