ps=0.91
usd=1.18
inr=56
cr=4847.38

uk=35423
usa=56516
ca=64000
cs=5649856
def convertSalary(a,b):
    if b=="UK":
        return a
    elif b=="Canada":
        count1=a/0.91
        return count1
    elif b=="USA":
        count2=(a*1.18)/0.91
        return count2
    elif b=="Cambodia":
        count3=(a*cr)/0.91
        return count3
    
a=float(input("Enter your salary in Germany "))
b=input("Enter the country you want to migrate to: ")
count=convertSalary(a,b)

if b=="Canada":
    if count>=ca:
        print(f"You will be rich in {b} with salary of {count} CAD")
    else: 
        print(f"You will be poor in {b} with salary of {count} CAD")
elif b=="USA":
    if count>=usa:
        print(f"You will be rich in {b} with salary of {count} USD")
    else:
        print(f"You will be poor in {b} with salary of {count} USD")
elif b=="UK":
    if count>=uk:
        print(f"You will be rich in {b} with salary of {count} Pounds")
    else:
        print(f"You will be poor in {b} with salary of {count} Pounds")
elif b=="Cambodia":
    if count>=cs:
        print(f"You will be rich in {b} with salary of {count} Cambodian riel")
    else:
        print(f"You will be poor in {b} with salary of {count} Cambodian riel")
