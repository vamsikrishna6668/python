username =input('enter a username:')
password =input('enter a password:')
if len(username)<10and len(password)<8:
    print('user & pwd are correct')
else:
    print('user & pwd are not correct')