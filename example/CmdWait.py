# -*- coding: utf-8 -*-

from CmdBase import CmdBase
from time import sleep
import string
from ErrorCommandFormat import ErrorCommandFormat

class CmdWait(CmdBase):
    """
        wait command.

        Command Format :
        wait <v>
    """
    __sec = None

    def __init__(self, params=None):
        self.id = None
        self.name = "wait command" 
        self.params = params
        self.cmd = "WAIT"

        self.validate()

    def validate(self):
        CmdBase.validate(self)

        if len(self.params) != 2:
            raise ErrorCommandFormat("Command Params Error.")
        else:
            self.__sec = int(self.params[1])

    def execute(self):
        print(self.cmd + ' WAIT=' + str(self.__sec) + '秒...')
        sleep(self.__sec)
