#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by zyf on 2018/11/27.
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
s.remove(3)
print(s)
#s.add([1,2])
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)