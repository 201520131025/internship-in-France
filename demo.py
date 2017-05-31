#-*- coding:utf-8 -*-
import re
a='a'
if a=='a':
    print ('yes')
totalCount = 'B_u2base(ITEM_ID_14,USER_ID_460).'   #取出字符串中的数字
totalCount = re.sub("\D", " ", totalCount)

print (totalCount)
print(type(totalCount))
print(type(totalCount.split()[0]))