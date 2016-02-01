# -*- coding: utf-8 -*-

from CmdBase import CmdBase
import string
from ErrorCommandFormat import ErrorCommandFormat

class CmdEcho(CmdBase):
    """
        echo command.

        Command Format :
        echo word

    """
    __txt = None

    def __init__(self, params=None):
        self.id = ""
        self.name = "echo command" 
        self.params = params
        self.cmd = "ECHO"
        self.type = "*"

        self.validate()

    def validate(self):
        CmdBase.validate(self)

        if len(self.params) != 2:
            raise ErrorCommandFormat("Command Params Error.")
        else:
            self.__txt = str(self.params[1])

    def execute(self):
        print(self.cmd + ' ' + str(self.__txt))
