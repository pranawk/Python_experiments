def multi_table(a,b):
    for i in range(1,b+1):
        ans= a*i
        print(a," x ",i,"=",ans)

a=int(input("Enter the number you want table of: "))
b=int(input("Enter the number of times you want: "))
multi_table(a,b)