#coding=utf-8
# ������ֵ
cars=100
space_in_a_car=4.0
drivers=30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
#��ӡ���
print '������',cars,'������'
print '������',drivers,'��˾��'
print '���Ի�ʣ',cars_not_driven,'�ճ�'
print '���ǿ�������',carpool_capacity,'��'
print '������',passengers,'�˿�'
print '������Ҫ����ÿ����',average_passengers_per_car,'�˿�'
print 'hey %s there.'%'you'