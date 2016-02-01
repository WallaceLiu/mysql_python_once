# -*- coding: utf-8 -*-

from CmdBase import CmdBase
from Biz_CollectTime import Biz_CollectTime
from Biz_ReserveTime import Biz_ReserveTime
import string
from Biz_Fence import Biz_Fence
from CmdSet_C import CmdSet_C
from CmdSet_R import CmdSet_R
from CmdSet_F import CmdSet_F
from ErrorCommandFormat import ErrorCommandFormat
from Biz_Base import Biz_Base

class CmdSet(CmdBase):
    """
        set command.

        Command Format :
        set <[c|collect]> <org id>=<-,->
        set <[f|fence]> <org id>=<-,-,-,->
        set <[r|reserve]> <-,->=<-,->
    """
    __subCommand = None

    def __init__(self, params, db):
        self.db = db
        self.id = ""
        self.name = "set command" 
        self.params = params
        self.cmd = "SET *"
        self.type = "*"

        self.validate()

    def validate(self):
        CmdBase.validate(self)

        if len(self.params) != 3:
            raise ErrorCommandFormat("Command Params Error.")
        else:
            if self.params[1].startswith('c', 0, 1):
                self.__subCommand = CmdSet_C(self.params, self.db)
            elif self.params[1].startswith('r', 0, 1):
                self.__subCommand = CmdSet_R(self.params, self.db)
            elif self.params[1].startswith('f', 0, 1):
                self.__subCommand = CmdSet_F(self.params, self.db)

    def execute(self):
        self.__subCommand.execute()
