#coding=utf-8
def print_two(*args):
	arg1,arg2 ,arg3= args #����һ��ķ�ʽ������֮ǰʹ��argv
	print "arg1:%r,arg2:%r,arg3:%s" % (arg1,arg2,arg3)
	
def print_two_again(arg1,arg2):
	print "arg1:%r, arg2:%r" % (arg1,arg2)

def print_one(arg1):
	print "arg1:%r" % arg1

def print_none():#�ã�����ʾ��һ�н���
	print "I got nothing."#�ĸ��ո����ֱ��TAB����
#����ĩβҪ���У�����
print_two("A","B",'��')
print_two_again("X","Y")
print_one("SSSSS")
print_none()