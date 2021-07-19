class A:
    def __init__(self):
        self.i = None


class B(A):
    def __init__(self):
        self.j = None

    def display(self):
        print(self.i)


obj = B()
obj.j = 2
obj.display()


class XPTO:
    def __init__(self, ctx):
        self.__msg = "Echo"
        if (ctx):
            self.__var1 = 3
            self.__var2 = 0.0
        else:
            self.__var1 = 3
            self.__var2 = 2.0

    def get_var1(self):
        return self.__var1

    def get_var2(self):
        return self.__var2

    def susp(self, par):
        val = 1
        if (par % 3 != 0):
            val += par % 2
        else:
            val += par * 2
        return val


my_obj = XPTO(True)
print(my_obj.susp(4))

number = 5.0
try:
    r = 10 / number
    print(r)
except:
    print("Oops! Error ocurred.")

