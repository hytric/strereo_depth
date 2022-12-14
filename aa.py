import time
import cv2
import numpy as np


# f = open('10.txt', 'r')
# lines = f.readlines()
# temp1 = []
# b = []
# for line in lines:
#         line = line.strip(' \n')
#         if line[len(line)-1] == ']':
#             tmp = line.split('   ')
#             for i in tmp:
#                 b.append(i.strip('[]- \n'))
#             temp1.append(b)
#             b = []
#         else:
#             tmp = line.split('   ')
#             for i in tmp:
#                 b.append(i.strip('[]- \n'))
# f.close()
#
# f = open('10_1.txt','w')
# for i in temp1:
#     tmp = ''
#     for j in i:
#         tmp = tmp + j + '\t'
#         time.sleep(0.01)
#     print(tmp)
#     f.write(tmp)
# f.close()
#
# f = open('20.txt', 'r')
# lines = f.readlines()
# temp2 = []
# b = []
# for line in lines:
#     line = line.strip(' \n')
#     if line[len(line)-1] == ']':
#         tmp = line.split('   ')
#         for i in tmp:
#             b.append(i.strip('[]- \n'))
#         temp2.append(b)
#         b = []
#     else:
#         tmp = line.split('   ')
#         for i in tmp:
#             b.append(i.strip('[]- \n'))
# f.close()
#
# f = open('30.txt', 'r')
# lines = f.readlines()
# temp3 = []
# b = []
# for line in lines:
#     line = line.strip(' \n')
#     if line[len(line)-1] == ']':
#         tmp = line.split('   ')
#         for i in tmp:
#             b.append(i.strip('[]- \n'))
#         temp3.append(b)
#         b = []
#     else:
#         tmp = line.split('   ')
#         for i in tmp:
#             b.append(i.strip('[]- \n'))
# f.close()

f = open('right.txt', 'r')
lines = f.readlines()
temp4 = []
b = []
for line in lines:
    line = line.strip(' \n')
    if line[len(line)-1] == ']':
        tmp = line.split('   ')
        for i in tmp:
            b.append(i.strip('[]- \n'))
        temp4.append(b)
        b = []
    else:
        tmp = line.split('   ')
        for i in tmp:
            b.append(i.strip('[]- \n'))
f.close()

f = open('left.txt', 'r')
lines = f.readlines()
temp5 = []
b = []
for line in lines:
    line = line.strip(' \n')
    if line[len(line)-1] == ']':
        tmp = line.split('   ')
        for i in tmp:
            b.append(i.strip('[]- \n'))
        temp5.append(b)
        b = []
    else:
        tmp = line.split('   ')
        for i in tmp:
            b.append(i.strip('[]- \n'))
f.close()

# for i in temp4:
#     print(len(i))
for i in temp4:
    dis = np.asanyarray(i[:100])

cv2.imshow('disparity',dis)
# import numpy as np
# arr1 = np.array(temp4)
# arr2 = np.array(temp5)
#
# print(arr1 - arr2)

# print(len(temp1))
# print(len(temp1[0]))
# print(len(temp2))
# print(len(temp2[0]))
# print(len(temp3))
# print(len(temp3[0]))
# print(len(temp4))
# print(len(temp4[0]))
# print(len(temp5))
# print(len(temp5[0]))