a=int(input("enter first number"))
b=int(input("enter second number"))
c=input("enter operator")
if c=='+':
    sum=a+b
    print("result=",sum)
elif c=='-':
    difference=a-b
    print("result= ", difference)
elif c=='*':
    product=a*b
    print("result= ",product)
elif c=='/':
    quotient=a/b
    print("result= ",quotient)
else:
    print("operator not valid")
def square(num):
    return num*num
print ("to print square input s")
s=input()
if s==s:
    n=int(input("enter number"))
    result= square(n)
    print("result =", result)
