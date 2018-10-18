user=input('enter user name:')
pwd=input('enter password name:')
if len(user)>=8 and len(pwd)<=9:
    print('user details are correct')
else:
    print('user details are not correct')
