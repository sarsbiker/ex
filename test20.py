#coding=utf-8
from sys import argv

script,input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0) #seek��ʼλ��Ϊ�ļ��еĵڼ����ַ�

def print_a_line(line_count,f):
	print line_count,f.readline()#��ȡһ��

current_file = open(input_file)

print "first let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)
#rewind(current_file) #˵����ǰ��ȡ��λ�����ļ�������
#current_line += 1#���������ֵļ�д��+=����
print_a_line(current_line,current_file)#ÿ������readline�󣬶������һ�У�Ȼ��������о�����һ��
print current_line
current_line = current_line + 1
print_a_line(current_line,current_file)

current_file.close()