#12. Write a python program to find factorial of a number using Recursion. 

def recursion(n):
 if(n<1):
      print("FACTORIAL NOT POSSIBLE!!")
 elif(n>1):
     return n*recursion(n-1)
 else:
    return 1
n=int(input("enter a number:"))
print("factorial of",n,"is:",recursion(n))
