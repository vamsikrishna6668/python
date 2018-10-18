class q:
    def __init__(self):
        print("Iam q's")
        super().__init__()
class p(q):
    def __init__(self):
        print("Iam p's")
        super().__init__()
class r:
    def __init__(self):
        print("r's")
        super().__init__()
class x(p,r):
    def __init__(self):
        print("x's")
        super().__init__()
class s:
    def __init__(self):
        print("s's")
        super().__init__()
class t:
    def __init__(self):
        print("t's")
        super().__init__()

class u(s,t):
    def __init__(self):
        print("u's")
        super().__init__()
class y(u):
    def __init__(self):
        print("y's")
        super().__init__()
class z(x,y):
    def __init__(self):
        print("z's")
        super().__init__()
#calling block
p =z()
print(z.mro())






