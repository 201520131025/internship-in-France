#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import re
# print "hello!"
with open("Positive.txt", "r") as ins:
    arr = []
    for line in ins:
        arr.append(line)
# print (len(arr))  #166486
# print (arr[0])
# print (len(arr[0]))
# print (arr[0][17])
# print (arr[0][0:5])
countUserIDAndAge=0
countUserIDAndGender=0
countItemIDAndAction=0
countItemIDAndDrama=0
countItemIDAndHorror=0
countB_u2base=0
countRating_1=0
countRating_2=0
countRating_3=0
countRating_4=0
countRating_5=0

for each in arr:
    if each[0:3]=='Age':
        countUserIDAndAge =countUserIDAndAge+1
    elif each[0:6]=='Gender':
        countUserIDAndGender=countUserIDAndGender+1
    elif each[0:6]=='action':
        countItemIDAndAction = countItemIDAndAction+1
    elif each[0:5] == 'drama':
        countItemIDAndDrama=countItemIDAndDrama+1
    elif each[0:6] == 'horror':
        countItemIDAndHorror=countItemIDAndHorror+1
    elif each[0:8] == 'B_u2base':
        countB_u2base=countB_u2base+1
    elif each[0:8] == 'rating_1':
        countRating_1=countRating_1+1
    elif each[0:8] == 'rating_2':
        countRating_2=countRating_2+1
    elif each[0:8] == 'rating_3':
        countRating_3=countRating_3+1
    elif each[0:8] == 'rating_4':
        countRating_4=countRating_4+1
    else:
        countRating_5=countRating_5+1
# print (countUserIDAndAge,countUserIDAndGender,countItemIDAndAction,countItemIDAndDrama,countItemIDAndHorror,countB_u2base,countRating_1,countRating_2,countRating_3,countRating_4,countRating_5)


def getNumber(str):
    str = re.sub("\D", " ", str)
    str=str.split()
    # str[0]=int(str[0])
    # str[1]=int(str[1])
    return str

#计算user和age矩阵
row = countUserIDAndAge
colomn = 2
matrixUserIDAndAge = [[0]*colomn for i in range(row)]
for i in range(countUserIDAndAge):
    matrixUserIDAndAge[i][0]=(getNumber(arr[i])[1])
    matrixUserIDAndAge[i][1]=(getNumber(arr[i])[0])
# print (matrixUserIDAndAge[0:10])
arrayUserIDAndAge = np.array(matrixUserIDAndAge) #将数据以数组array表示
# print (arrayUserIDAndAge[:,0])
# print (type(arrayUserIDAndAge[:,0]))
maxUser=0
for i in range(len(matrixUserIDAndAge)):
    intNo=int(matrixUserIDAndAge[i][0])
    if intNo>maxUser:
        maxUser=intNo
# print (maxUser)
# print (countUserIDAndAge)
# print (countUserIDAndGender)

#计算user和gender矩阵
row = countUserIDAndGender
matrixUserIDAndGender = [[0]*colomn for i in range(row)]
for i in range(countUserIDAndGender):
    str = re.sub("\D", "", arr[i+countUserIDAndAge])
    matrixUserIDAndGender[i][0]=(str)
    matrixUserIDAndGender[i][1]=arr[i+countUserIDAndAge][7]
# print(matrixUserIDAndGender[0:10])
arrayUserIDAndGender = np.array(matrixUserIDAndGender[0:10]) #将数据以数组array表示
# print(arrayUserIDAndGender)
maxUser1=0
for i in range(len(matrixUserIDAndGender)):
    intNo=int(matrixUserIDAndGender[i][0])
    if intNo>maxUser1:
        maxUser1=intNo
# print (maxUser1)

userNo=max(maxUser,maxUser1) #计算user的个数


# matrixUserIDAndAge=np.matrix(matrixUserIDAndAge)
# print (matrixUserIDAndAge[:,0])
# print (arrayUserIDAndAge)
# print (arrayUserIDAndAge[:,0])
#计算user age gender矩阵
# left=pd.DataFrame({'id': matrixUserIDAndAge[:,0],
#                    'age': matrixUserIDAndAge[:,1], })
# right=pd.DataFrame({'id': matrixUserIDAndGender[:,0],
#                    'gender': matrixUserIDAndGender[:,1], })
# result = pd.merge(left, right, on='id')
# print (result)

#计算item和action矩阵
row = countItemIDAndAction
matrixItemIDAndAction = [[0]*colomn for i in range(row)]
for i in range(countItemIDAndAction):
    matrixItemIDAndAction[i][0]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender])[1]
    matrixItemIDAndAction[i][1]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender])[0]
# print(matrixItemIDAndAction)
maxItem1=0
for i in range(len(matrixItemIDAndAction)):
    intNo=int(matrixItemIDAndAction[i][0])
    if intNo>maxItem1:
        maxItem1=intNo
# print (maxItem1)

#计算item和drama矩阵
row = countItemIDAndDrama
matrixItemIDAndDrama = [[0]*colomn for i in range(row)]
for i in range(countItemIDAndDrama):
    matrixItemIDAndDrama[i][0]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction])[1]
    matrixItemIDAndDrama[i][1]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction])[0]
# print(matrixItemIDAndDrama)
maxItem2=0
for i in range(len(matrixItemIDAndDrama)):
    intNo=int(matrixItemIDAndDrama[i][0])
    if intNo>maxItem2:
        maxItem2=intNo
# print (maxItem2)

#计算item和horror矩阵
row = countItemIDAndHorror
matrixItemIDAndHorror = [[0]*colomn for i in range(row)]
for i in range(countItemIDAndHorror):
    matrixItemIDAndHorror[i][0]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama])[1]
    matrixItemIDAndHorror[i][1]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama])[0]
# print(matrixItemIDAndHorror)
maxItem3=0
for i in range(len(matrixItemIDAndHorror)):
    intNo=int(matrixItemIDAndHorror[i][0])
    if intNo>maxItem3:
        maxItem3=intNo
# print (maxItem3)

itemNo=max(maxItem1,maxItem2,maxItem3) #计算item的个数

#计算countB_u2base矩阵
#此处需要计算item和user的最大值 然后生成一个矩阵,矩阵中的值是binary 0或1
row = countB_u2base
matrixB_u2base = [[0]*colomn for i in range(row)]
for i in range(countB_u2base):
    matrixB_u2base[i][0]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror])[1]
    matrixB_u2base[i][1]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror])[2]
# print(matrixB_u2base)
binaryMatrixB_u2base=[[0]*userNo for i in range(itemNo)]
for element in matrixB_u2base:
    binaryMatrixB_u2base[int(element[0])-1][int(element[1])-1]=1
# print (len(binaryMatrixB_u2base))

#计算rating1矩阵
row = countRating_1
matrixRating_1 = [[0]*colomn for i in range(row)]
for i in range(countRating_1):
    matrixRating_1[i][0]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror+countB_u2base])[1]
    matrixRating_1[i][1]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror+countB_u2base])[2]
# print(matrixRating_1[0:10])
binaryMatrixRating_1=[[0]*userNo for i in range(itemNo)]
for element in matrixRating_1:
    binaryMatrixRating_1[int(element[0])-1][int(element[1])-1]=1
# print (len(binaryMatrixB_u2base[0]))

#计算rating2矩阵
row = countRating_2
matrixRating_2 = [[0]*colomn for i in range(row)]
for i in range(countRating_2):
    matrixRating_2[i][0]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror+countB_u2base+countRating_1])[1]
    matrixRating_2[i][1]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror+countB_u2base+countRating_1])[2]
# print(matrixRating_2[0])
binaryMatrixRating_2=[[0]*userNo for i in range(itemNo)]
for element in matrixRating_2:
    binaryMatrixRating_2[int(element[0])-1][int(element[1])-1]=1
# print (len(binaryMatrixB_u2base[0]))

#计算rating3矩阵
row = countRating_3
matrixRating_3 = [[0]*colomn for i in range(row)]
for i in range(countRating_3):
    matrixRating_3[i][0]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror+countB_u2base+countRating_1+countRating_2])[1]
    matrixRating_3[i][1]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror+countB_u2base+countRating_1+countRating_2])[2]
# print(matrixRating_3[0])
binaryMatrixRating_3=[[0]*userNo for i in range(itemNo)]
for element in matrixRating_3:
    binaryMatrixRating_3[int(element[0])-1][int(element[1])-1]=1
# print (len(binaryMatrixB_u2base[0]))

#计算rating4矩阵
row = countRating_4
matrixRating_4 = [[0]*colomn for i in range(row)]
for i in range(countRating_4):
    matrixRating_4[i][0]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror+countB_u2base+countRating_1+countRating_2+countRating_3])[1]
    matrixRating_4[i][1]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror+countB_u2base+countRating_1+countRating_2+countRating_3])[2]
# print(matrixRating_4[0])
binaryMatrixRating_4=[[0]*userNo for i in range(itemNo)]
for element in matrixRating_4:
    binaryMatrixRating_4[int(element[0])-1][int(element[1])-1]=1
# print (len(binaryMatrixB_u2base[0]))

#计算rating5矩阵
row = countRating_5
matrixRating_5 = [[0]*colomn for i in range(row)]
for i in range(countRating_5):
    matrixRating_5[i][0]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror+countB_u2base+countRating_1+countRating_2+countRating_3+countRating_4])[1]
    matrixRating_5[i][1]=getNumber(arr[i+countUserIDAndAge+countUserIDAndGender+countItemIDAndAction+countItemIDAndDrama+countItemIDAndHorror+countB_u2base+countRating_1+countRating_2+countRating_3+countRating_4])[2]
# print(matrixRating_5[0])
binaryMatrixRating_5=[[0]*userNo for i in range(itemNo)]
for element in matrixRating_5:
    binaryMatrixRating_5[int(element[0])-1][int(element[1])-1]=1
# print (len(binaryMatrixB_u2base[0]))

print(matrixUserIDAndAge) 
# np.save("matrixUserAndAge.npy",matrixUserIDAndAge)
# np.save("matrixUserIDAndGender.npy",matrixUserIDAndGender)
# np.save("matrixItemIDAndAction.npy",matrixItemIDAndAction)
# np.save("matrixItemIDAndDrama.npy",matrixItemIDAndDrama)
# np.save("matrixItemIDAndHorror.npy",matrixItemIDAndHorror)
# np.save("binaryMatrixB_u2base.npy",binaryMatrixB_u2base)
# np.save("binaryMatrixRating_1.npy",binaryMatrixRating_1)
# np.save("binaryMatrixRating_2.npy",binaryMatrixRating_2)
# np.save("binaryMatrixRating_3.npy",binaryMatrixRating_3)
# np.save("binaryMatrixRating_4.npy",binaryMatrixRating_4)
# np.save("binaryMatrixRating_5.npy",binaryMatrixRating_5)


print ("hello")


# print (np.load("matrixUserIDAndAge"))      