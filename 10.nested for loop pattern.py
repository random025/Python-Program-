##10)  Write a python program to construct the following pattern using nested for loop:
##*
##**
##***
##****
##*****
##*****
##****
##***
##**
##*

n=int(input("ENTER A VALUE:"))
for x in range(0,n+1,1):
   print(x*'*')
if(x==n):
    for x in range(n,0,-1): 
        print(x*'*')
