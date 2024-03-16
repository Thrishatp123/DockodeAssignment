r=4
c=7
for i in range(4):
    print("___",end="")
    print("   ",end="")
print()
for i in range(1,c+2):
    for j in range(4):
        if i%2 !=0:
            print('/  ',end="")
            print('\\__',end="")

        else:
            print('\\__',end="")
            print('/  ',end="")
    print()


