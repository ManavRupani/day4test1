mm=int(input("Enter the month in the numeric form: "))
dd=int(input("Enter the day of the month: "))
yy=int(input("Enter the year in two digit format: "))

if mm<=0 or mm>=13:
    print("Error: Invalid Month Input")
elif dd<=0 or dd>=32:
    print("Error: Invalid Day Input")
elif yy<=9 or yy>=100:
    print("Invalid Year Input")
else:
    print(f"The date is {mm}/{dd}/{yy}")
    print("Success: Congratulations! you entered the correct date")