# -*- coding: utf-8 -*-
# Created by zyf on 2018/11/27.
filename = 'C:\\Users\\Administrator\\PycharmProjects\\pythondemo\\base\\pyfile.txt'
filename2 = "C:\\Users\\Administrator\\PycharmProjects\\pythondemo\\base\\pyfile2.txt"
with open(filename) as fileobj:
    content = fileobj.read()
    print(content)
with open(filename) as fileobj:
    for line in fileobj:
        print(line.rstrip())
with open(filename) as fileobj:
    lines = fileobj.readlines()
for line in lines:
    print(line)
with open(filename) as fileobj:
    lines = fileobj.readline()
for line in lines:
    print(line)
with open(filename2, 'a') as fileobj:
    fileobj.write('I love python\n')
    fileobj.write('好不好\n')
    fileobj.write('对读写操作还是真实友好呢\n')
