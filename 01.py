import sys
import fileinput
# import expense report from txt file
expenses_file = open("01.txt", "r")
expensereportlist = []
for line in expenses_file:
    expensereportlist.append(int(line.strip()))
expensereportlist.sort()
# print(expensereportlist)
# exit()
# #Part One
# SecNum = 2020
# for num in expensereportlist:
#     SecNum -= num
#     if SecNum in expensereportlist:
#         print("the number is:" + str(num)  + " & " + str(SecNum))
#         print('The total is:' + str(num*SecNum))
#         break
#     SecNum = 2020

# #Part Two
# for num in expensereportlist:

#     break



#online solution optimized from my code


X = [int(line) for line in fileinput.input()]
n = len(X)
for i in range(n):
    for j in range(i+1, n):
        if X[i]+X[j]==2020:
            print('Part 1:', X[i]*X[j])
        for k in range(j+1, n):
            if X[i]+X[j]+X[k]==2020:
                print('Part 2:', X[i]*X[j]*X[k])