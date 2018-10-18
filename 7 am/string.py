string =input('enter a string:')
length =len(string)
for i in range(1,length+1):
    for j in  range(i+1):
        print(j,end='')
    print()