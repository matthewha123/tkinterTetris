# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:13:58 2017

@author: matth
"""

class tester(object):
    num = []
    def putNum(self,n):
        self.num.append(n)
    def returnNum(self):
        return self.num
t = tester()
a = [5]
t.putNum(a)
a.append(5)
print(t.returnNum())