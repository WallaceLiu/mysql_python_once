# -*- coding: utf-8 -*-
from CommandChain import CommandChain
# from testCommandChain import TestCommandChain

# 测试
#t = TestCommandChain()
#t.test()
cmds = CommandChain()
cmds.loadCmdList("usecase_drive\case_01.txt");
cmds.execute()
