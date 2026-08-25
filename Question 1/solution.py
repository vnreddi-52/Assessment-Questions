num = int(input())

def nthTerm(num):
    if num==1:
        return 1
    elif num==2:
        return 2
    elif num==3:
        return 3
    elif num==4:
        return 4
    else:
        return(
            nthTerm(num-1)+
            nthTerm(num-2)+
            nthTerm(num-3)+
            nthTerm(num-4)
        )

if num<0:
    print(num)
else:
    print(nthTerm(num))