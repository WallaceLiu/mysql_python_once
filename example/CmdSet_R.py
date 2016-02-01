# -*- coding: utf-8 -*-

from CmdBase import CmdBase
import string
from ErrorCommandFormat import ErrorCommandFormat
from Biz_ReserveTime import Biz_ReserveTime

class CmdSet_R(CmdBase):
    """
        set command.

        Command Format :
        set <[r|reserve]> <-,->=<-,->
    """
    __obd_id = None   # obd id
    __car_id = None   # car id
    __b_time = None   # begin time
    __e_time = None   # end time
    __biz_ReserveTime = None

    def __init__(self, params, db):
        self.id = None
        self.name = "set command" 
        self.params = params
        self.cmd = "SET"
        self.type = "reserve"
        __biz_ReserveTime = Biz_ReserveTime(db)

        self.validate()

    def validate(self):
        p = str.split(self.params[2],'=')

        if len(p) != 2:
            raise ErrorCommandFormat("Command Params Error : set <[r|reserve]> <-,->=<-,->")
        else:
            obd_car_id = str.split(p[0],',')
            b_e_times = str.split(p[1],',')

            if len(obd_car_id) == 2 and len(b_e_times) == 2 :
                self.__obd_id = obd_car_id[0]
                self.__car_id = obd_car_id[1]
                self.__b_time = b_e_times[0]
                self.__e_time = b_e_times[1]
            else:
                raise ErrorCommandFormat("Command Params Error : set <[r|reserve]> <org id>=<-,->")

    def execute(self):
        bl = self.__biz_ReserveTime.insertReserveTime(self.__car_id, self.__obd_id, self.__b_time, self.__e_time)
        print(bl)
       
