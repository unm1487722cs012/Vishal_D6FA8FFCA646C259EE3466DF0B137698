def fact(n):
 if n==1:
  return n
 else:
  return n*fact(n-1)
print('program to print factorial using recursion')
num=int(input ('how manu terms:'))
if num<0:
    print("sorry,factorial does not exist for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    print("the factorial of ",num,"is",fact(num))















    
  