#-1 to -10 using while Loop

a=-10
while a<=-1:
    print(a)
    a=a+1
    
print()
# -10 to -1 using while loop

b=-1
while b>=-10:
    print(b)
    b=b-1
    
# printing 1 t0 5 tables using while loop


i=1
while i<=5:
    print("table of",i)
    j=1
    while j<=10:
        print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1
    print()
    
#printing alphabets using while loop

ch=ord('A')
while ch<=ord("Z"):
    print(chr(ch),end="")
    ch=ch+1
    print()
    
#sum of prime numbers in a number

num=int(input("enter a number:"))
sum=0
while num>0:
    digit=num%10
    num=num//10
    if digit==2 or digit==3 or digit==5 or digit==7:
        sum=sum+digit
print("sum of prime digits is",sum)

#automorphic number

num = int(input("Enter a number: ")
square = num * num
temp = num
count = 0
while temp > 0:
    count += 1
    temp //= 10
last_digits = square % (10 ** count)
if last_digits == num:
    print(num, "is an Automorphic number")
else:
    print(num, "is NOT an Automorphic number")
    
#smallest number

num=int(input("enter a number:"))
smallest=9
while num>0:
    digit=num%10
    if digit<smallest:
        smallest=digit
    num=num//10
print("smallest digit is",smallest)

    
    
    
    

