def fibb_check(n):
    if n==0 or n==1:
        print(n,"is valid")
    elif n<0:
        print(n,"is not valid")
    else:
        fibb=[0,1,1]
        a=0
        while n>a:
            a = fibb[-1] + fibb[-2]
            fibb.append(a)
            if n>a:
                continue
            elif n==a:
                print(n,"is valid")
                break
            else:
                print(n,"is not valid")
                break
p=""
q=int(input("Enter the number of turns:-"))
for i in range(q):
    n=int(input("Enter the number:-"))
    fibb_check(n)