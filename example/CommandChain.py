# -*- coding: utf-8 -*-

from CmdBase import CmdBase
from CmdSend import CmdSend
from CmdSet import CmdSet
from CmdWait import CmdWait
import string
from ErrorCommandFormat import ErrorCommandFormat
from CmdEcho import CmdEcho
from mysql_python_once import MysqlPythonOnce
from LoadConf import LoadConf

class CommandChain(CmdBase):

    __commandCollection = []
    __loadConf = None
    __bizDb = None    
    __src_msgDb = None
    __dest_msgDb = None

    def __init__(self, params=None):
        self.name = "command chain" 
        self.params = params
        self.cmd = self.name

        self.__loadConf = LoadConf()
        self.__bizDb = MysqlPythonOnce(self.__loadConf.biz_db_host,\
                 self.__loadConf.biz_db_user, \
                 self.__loadConf.biz_db_password,\
                 self.__loadConf.biz_db_database)
    
        self.__src_msgDb = MysqlPythonOnce(self.__loadConf.src_msg_db_host, \
                 self.__loadConf.src_msg_db_user, \
                 self.__loadConf.src_msg_db_password, \
                 self.__loadConf.src_msg_db_database)

        self.__dest_msgDb = MysqlPythonOnce(self.__loadConf.dest_msg_db_host, \
                 self.__loadConf.dest_msg_db_user, \
                 self.__loadConf.dest_msg_db_password, \
                 self.__loadConf.dest_msg_db_database)

        self.__bizDb.open()
        self.__src_msgDb.open()
        self.__dest_msgDb.open()

    def execute(self):
        try:
            for x in self.__commandCollection:
                x.execute()

            print('DONE.')
        except  ErrorCommandFormat as e:
            print(e.value)
        finally:
            self.__commandCollection.clear()
            self.__bizDb.close()
            self.__src_msgDb.close()
            self.__dest_msgDb.close()

    def loadCmdList(self):
        self.loadCmdList("list.txt")

    def loadCmdList(self, path):
        try: 
            with open(path, "r") as f:
                c = None
                while True:  
                    line = f.readline()  
                    if not line:  
                        break
                    else:  
                        line = str.lower(line)
                        lines = line.split()
                        if len(lines) > 0 and not str.strip(line).startswith("#",0,1):
                            if lines[0] == "send":
                                c = CmdSend(lines, self.__src_msgDb, self.__dest_msgDb)
                                self.__commandCollection.append(c)
                            elif lines[0] == "set":
                                c = CmdSet(lines, self.__bizDb)
                                self.__commandCollection.append(c)
                            elif lines[0] == "wait":
                                c = CmdWait(lines)
                                self.__commandCollection.append(c)
                            elif lines[0] == 'echo':
                                c = CmdEcho(lines)
                                self.__commandCollection.append(c)
        except Exception as e:
            print(e.args)

