#Print Even order alphabet using ASCII values


for x in range(65,91):
    if x%2==0:
        print(chr(x),"=",x)
        