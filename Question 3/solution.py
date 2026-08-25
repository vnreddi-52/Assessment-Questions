a = input()
b = input()

binary_a = bin(int(a))[2:]
binary_b = bin(int(b))[2:]

for i in range(int(a)+1,int(b)):
    binary = bin(int(i))[2:]

    if len(binary)>=4 and "000" not in binary:
        print(binary, end=" ")





# def getBinary(num):









# for i in a:
#     binary = 
#     print(binary)