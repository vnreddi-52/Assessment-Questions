string = input()
res=""

# res=sorted(string)
# print(res)

for i in string:
    if i =="#":
        res+=i

for i in string:
    if i != "#":
        res+=i

print(res)