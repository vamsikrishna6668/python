s =int(input('enter a number:'))
count =0
for i in  range(1,s+1):
    if s%i ==0:
        count+=1
if count==2:
    print('It is a prime number')
else:
    print('it is not a prime number')


