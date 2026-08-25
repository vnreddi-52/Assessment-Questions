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

while i<t:
    try:
        num1 = int(input("enter total_workload :"))
        num2 = int(input("enter no of servers :"))
        avg = num1 // num2
        print(avg)
    except ZeroDivisionError:
        print("Error")
    i=i+1


    
