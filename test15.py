#coding=utf-8
from sys import argv

script,filename = argv #������д�븳ֵ

txt = open(filename) #��ȡĳ���ļ�����������

print "Here's your file %r:" % filename
print txt.read() #������������

#print "Type the filename again:"
#file_again = raw_input(">")

#txt_again = open(file_again)

print txt_again.read()
