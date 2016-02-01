# -*- coding: utf-8 -*-

from CmdBase import CmdBase
import string
from Biz_Fence import Biz_Fence
from ErrorCommandFormat import ErrorCommandFormat
from Biz_Base import Biz_Base

class CmdSet_F(CmdBase):
    """
        set command.

        Command Format :
        set <[r|reserve][c|collect]> <org id>=<[-,-]>
        set <[f|fence]> <org id>=<[-,-,-,-]>
    """
    __lng = None      # lng
    __lat = None      # lat
    __outerRadius = None   #
    __innerRadius = None
    __biz_fence = None

    def __init__(self, params, db):
        self.id = ""
        self.name = "set command" 
        self.params = params
        self.cmd = "SET"
        self.type = "fence"
        __biz_fence = Biz_Fence(db)

        self.validate()

    def validate(self):
        p = str.split(self.params[2],'=')

        if len(p) != 2:
            raise ErrorCommandFormat("Command Params Error : set <[f|fence]> <id>=<-,-,-,->")
        else:
            org_id = p[0]
            p2s = str.split(p[1],',')
                
            if len(p2s) == 4 :
                self.id = org_id
                self.__lng = None if p2s[0] == "-" else float(p2s[0])
                self.__lat = None if p2s[1] == "-" else float(p2s[1])
                self.__outerRadius = None  if p2s[2] == "-" else float(p2s[2])
                self.__innerRadius = None  if p2s[3] == "-" else float(p2s[3])

            else:
                raise ErrorCommandFormat("Command Params Error : set <[f|fence]> <id>=<-,-,-,->")

    def execute(self):
        print(self.cmd + ' ORG_ID=' + self.id + \
           ',LNG=' + str(self.__lng) + \
           ',LAT=' + str(self.__lat) + \
           ',INNERRADIUS=' + str(self.__innerRadius) + \
           ',OUTERRADIUS=' + str(self.__outerRadius))
        if self.__lng != None and self.__lat != None and self.__outerRadius != None and self.__innerRadius != None:
            bl = self.__biz_fence.updateFence(self.id,self.__lng,self.__lat,self.__outerRadius,self.__innerRadius)
        else:
            if self.__lng != None and self.__lat != None :
                bl = self.__biz_fence.updateFenceLocation(self.id,self.__lng, self.__lat)
            if self.__outerRadius != None :
                bl = self.__biz_fence.updateFenceOuterRadius(self.id,self.__outerRadius)
            if self.__innerRadius != None:
                bl = self.__biz_fence.updateFenceInnerRadius(self.id,self.__innerRadius)
        print(bl)
