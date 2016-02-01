# -*- coding: utf-8 -*-

import string
import os
import sys
from configparser import ConfigParser

class LoadConf(object):

    __configFileName = "app.conf"

    def __init__(self):
        config = ConfigParser()
        config.read(self.__configFileName)

        self.biz_db_host = config.get("biz_db","host") 
        self.biz_db_user = config.get("biz_db","user") 
        self.biz_db_password = config.get("biz_db","password")
        self.biz_db_database = config.get("biz_db","database")
          
        self.src_msg_db_host = config.get("src_msg_db","host")
        self.src_msg_db_user = config.get("src_msg_db","user")
        self.src_msg_db_password = config.get("src_msg_db","password")
        self.src_msg_db_database = config.get("src_msg_db","database")
         
        self.dest_msg_db_host = config.get("dest_msg_db","host") 
        self.dest_msg_db_user = config.get("dest_msg_db","user") 
        self.dest_msg_db_password = config.get("dest_msg_db","password") 
        self.dest_msg_db_database = config.get("dest_msg_db","database") 
