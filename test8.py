#coding=utf-8
formatter = "%r %r %s %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % ("һ","��","��","��")#%r ���ܴ�ӡ�����ģ����ǵ�s
print formatter % (True,False,True,False)#�Դ��Ĳ���ֵ������Ҫ����
print formatter % (formatter,formatter,formatter,formatter)#r�������ԭʼֵ
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",#���Ų�Ҫ���ǿ�������
	"So I said goodnight."
)