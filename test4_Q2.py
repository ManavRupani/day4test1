RED="red"
BLUE="blue"
YELLOW="yellow"

def algo(color1,color2):
    if color1=="red":
        if color2=="blue":
            print("purple")
        elif color2=="yellow":
            print("orange")
        else:
            pass
    elif color1=="blue":
        if color2=="red":
            print("purple")
        elif color2=="yellow":
            print("green")
        else:
            pass
    elif color1=="yellow":
        if color2=="red":
            print("orange")
        elif color2=="blue":
            print("green")
        else:
            pass
    else:
        pass

a=str(input("Enter first primary color in lower case letters: "))
b=str(input("Enter second primary color in lower case letters: "))

if a=="red" or a=="blue" or a==YELLOW :
    if b==RED or b==BLUE or b==YELLOW :
        algo(a,b)        
elif a==b:
    print("Two color entered are equal")
else:
    print("error")



