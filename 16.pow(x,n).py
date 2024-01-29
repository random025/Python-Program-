#16)Write a Python class to implement pow(x, n) 

class py_power:
    def power(x,n):
        print("power of given literals:\nx:",x,"\nn:",n,"is:",x**n)
x=float(input("ENTER X(BASE) VALUE:"))
n=float(input("ENTER N(POWER) VALUE:"))
py_power.power(x,n)
