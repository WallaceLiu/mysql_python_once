# -*- coding: utf-8 -*-

from CommandChain import CommandChain

class TestCommandChain(object):
    """
        测试命令
    """
    __commandChain = None

    def __init__(self):
        self.__commandChain = CommandChain()

    def test(self):
        self.__commandChain.loadCmdList("list.txt")
        self.__commandChain.execute()
