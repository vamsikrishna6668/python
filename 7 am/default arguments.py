def show(idno,name='ismail',salary=3000000):  #idno - positional arguments , name,salary(default argumets)
    print('IDNO = ',idno)
    print('NAME = ',name)
    print('SALARY =',salary)
#calling block or fuction calling
show(143) # passing the argumets for idno
print('-------------------')
show(idno=6668,name='ismail basha',salary =25000000)
print('-------------------')
show(salary=340000000,name='anjali',idno=7677)
print('---------------------')
show(idno  = 'none',salary = 'none',name  = 'none')