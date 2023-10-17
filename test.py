# # # n=int(input())
# # # a=0
# # # b=1
# # # c=0
# # # if n==0:
# # #     print('the fibanocci series sum is',0)
# # # if n==1:
# # #     print('the fibanocci series sum is',0)
# # # if n==2:
# # #     print('the fibanocci series sum is',1)
# # # if n>2:
# # #     for i in range(0,n-1):
# # #         c=a+b
# # #         a=b
# # #         b=c
# # #     print('the fibanocci series sum is',c)
# # def factorial(k):
# #     lis=[]
# #     for i in k:
# #         fact=1
# #         for j in range(1,i+1):
# #             fact=fact*j
# #         lis.append(fact)
# #     return lis
# # n=int(input('Enter the size of List'))
# # li=[]
# # for i in range(n):
# #     a=int(input('Enter Element:'))
# #     li.append(a)
# # list2=factorial(li)
# # print(list2)
# def factorial(k):
#     fact=1
#     for i in range(1,k+1):
#         fact=fact*i
#     return fact
# n=int(input('Enter the number: '))
# a=factorial(n)
# print(a)
