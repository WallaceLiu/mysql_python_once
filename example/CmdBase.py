# -*- coding: utf-8 -*-

class CmdBase(object):
    """
        command base class.
    """

    def __init__(self, params=None):
        self.id = None
        self.name = None
        self.params = params
        self.cmd = None
        self.type = None
     
    def validate(self):
        print(self.params)

    def execute(self):
        pass

