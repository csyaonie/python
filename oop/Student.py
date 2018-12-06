#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by zyf on 2018/11/27.
class Student(object):
    def __init__(aa, name, age):
        aa.__name = name
        aa._age = age

s=Student('xiaoming',23)
#print(s.__name)
print(s._age)

#私有属性用两个下横杆来标识  self 可用aa代替
