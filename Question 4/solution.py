# calculate average load per server 
# = total workload / no of servers 

t = int(input("enter t :"))
i=0
# try:
#     while i<t:
#         num1 = int(input())
#         num2 = int(input())
#         avg = num1 // num2
#         print(avg)
#         i=i+1
# except ZeroDivisionError:
#     print("Error")


# while i<t:
#     num1 = list(map(int, input().split()))
#     i=i+1

while i<t:
    num1 = list(map(int, input().split()))
    # print(num1)
    try:
        avg = num1[0]// num1[1]
        print(avg)
    except ZeroDivisionError:
        print("Error")

    
