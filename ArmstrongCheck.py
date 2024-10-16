def armstrongchk(n):
    a=n
    total=0
    while(a>0):
        r= a%10
        total += r*r*r
        a//=10
    if n == total:
        print("Number is armstrong")
    else:
        print("Number is not armstrong")

a= int(input("Enter the number: "))
armstrongchk(a)
    