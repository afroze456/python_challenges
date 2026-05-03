a=int(input("enter a value: "))
b=int(input("enter value 2: "))
c=int(input("enter value 3: "))
            
avg=(a+b+c)/3

print("avg=",avg)


if avg>a and avg>b and avg>c :
    print("average is greatest")
elif avg>a and avg>b:
    print("average is greater than a and b")
elif avg>a and avg>c:
    print("average is greater then a and c")
elif avg>b and avg>c:
    print("average is greater then b and c")
elif avg>a:
    print("average is greater then a")
elif avg>b:
    print("average is greater then b")
elif avg>c:
    print("average is greater then c")
else:
    print("invaid")