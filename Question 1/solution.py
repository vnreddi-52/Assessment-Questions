num = int(input())

# def nthTerm(num):
#     if num==1:
#         return 1
#     elif num==2:
#         return 2
#     elif num==3:
#         return 3
#     elif num==4:
#         return 4
#     else:
#         return(
#             nthTerm(num-1)+
#             nthTerm(num-2)+
#             nthTerm(num-3)+
#             nthTerm(num-4)
#         )

# if num<0:
#     print(num)
# else:
#     print(nthTerm(num))

if num<1:
    print("Invalid")
elif num<=4:
    print(num)
else:
    a,b,c,d=1,2,3,4

    for i in range(5,num+1):
        next=a+b+c+d
        # a=b
        # b=c
        # c=d
        # d=next
        a,b,c,d=b,c,d,next
    print(next)