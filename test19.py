#coding=utf-8
'''
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers =50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)

print "And we can aombine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)#֧�ֱ���������

print "����һ�¿���"
a=input('��һ����')#raw_input���ܶ������ַ�������input������֣��ַ����ӡ�������ֱ��
b=input('�ڶ�����')

cheese_and_crackers(a,b)
'''

def abing(a,b):
	if a > b:
		print '%d ���� %d ' % (a,b)
	elif a < b:
		print '%d С�� %d ' % (a,b)
	else:
		print 'һ����'

a = input('��һ����')
b = input('�ڶ�����')
#c = input('��������')

abing(a,b)
