#coding=utf-8
x = '������%d���ˡ�' % 10
binary = 'binary'
do_not = 'don\'t'
y = '��Щ֪��%s ����Щ%s' % (binary,do_not)

#��ӡһ�¿���
print x 
print y 

print 'i said:%s' % x 
print 'i also said:"%s"' % y 

hilarious = False
joke_evaluation = "isn't that joke so funny? %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 