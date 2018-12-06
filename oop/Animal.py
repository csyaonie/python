#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by zyf on 2018/11/27.

class Animal(object):
    name='lala'
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass
dog=Dog()
dog.run()

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c,Animal))

print(type(123))
print(type(123)==int)
print(type('abc'))
print(type('abc')==str)
print(type(dog))
print(type(dog)==Dog)
print(type(dog.run))
#print(type(dog.run)==method)
#print(type(abs)==function)

print(hasattr(dog,'name'))
print(getattr(dog,'name'))
setattr(dog,'name','dudu')
print(getattr(dog,'name'))
print('----')
print(Dog.name)
print(dog.name)
del dog.name
print(dog.name)


