print ("Welcome to complex calculator")
print ("Developed by Bhomit Patiye")
print ("Chose your objective from the following")
print ("1.Simple operations of mathamatical operators")
print ("2.Square")
print ("3.Cube")
print ("4.Perimeter")
print ("5.Area")
print ("6.Volume")

ch=int(input("Enter Choice(1-6): "))

if ch==1:
    print ("Choose your objective from the following")
    print ("1.Add")
    print ("2.Subtract")
    print ("3.Multiply")
    print ("4.Divide")

    so=int(input("Enter Choice(1-4): "))

    if so==1:
        a=float(input("Enter Your First Number: "))
        b=float(input("Enter Your Second Number: "))
        c=a+b
        print("The sum of",a,"and",b,"=",c)
    elif so==2:
        a=float(input("Enter Your First Number: "))
        b=float(input("Enter Your Second Number: "))
        c=a-b
        print("The difference of",a,"and",b,"=",c)
    elif so==3:
        a=float(input("Enter Your First Number: "))
        b=float(input("Enter Your Second Number: "))
        c=a*b
        print("The multiplication of",a,"and",b,"=",c)
    elif so==4:
        a=float(input("Enter Your First Number: "))
        b=float(input("Enter Your Second Number: "))
        c=a/b
        print("The quotient of",a,"and",b,"=",c)
    else :("Invalid Argument")

elif ch==2:
    a=float(input("Enter Your Number: "))
    b=a**2
    print ("The square of number",a,"=",b)

elif ch==3:
    a=float(input("Enter Your Number: "))
    b=a**3
    print ("The cube of number",a,"=",b)

elif ch==4:
    print ("Choose your objective from the following")
    print ("1.Square")
    print ("2.Rectangle")
    print ("3.Triangle")
    print ("4.Circle")

    p=int(input("Enter Choice(1-4): "))

    if p==1:
        a=float(input("Enter the side of square : "))
        b=4*a
        print ("The perimeter is",b)
    elif p==2:
        a=float(input("Enter the length of rectangle : "))
        b=float(input("Enter the breadth of rectangle : "))
        c=2*(a+b)
        print ("The perimeter is",c)
    elif p==3:
        a=float(input("Enter the first side of triangle : "))
        b=float(input("Enter the second side of triangle : "))
        c=float(input("Enter the third side of triangle : "))
        d=a+b+c
        print ("The perimeter is",d)
    elif p==4:
        a=float(input("Enter the radius of circle : "))
        b=2*(22/7)*a
        print ("The circumference is : ",b)
    else:("Invalid Argument")

elif ch==5:
    print ("Choose your objective from the following")
    print ("1.Square")
    print ("2.Rectangle")
    print ("3.Triangle")
    print ("4.Circle")

    ar=int(input("Enter Choice(1-4): "))

    if ar==1:
        a=float(input("Enter the side of square : "))
        b=a**2
        print ("The area is",b)
    elif ar==2:
        a=float(input("Enter the length of rectangle : "))
        b=float(input("Enter the breadth of rectangle : "))
        c=a*b
        print ("The area is",c)
    elif ar==3:
        a=float(input("Enter the height of triangle : "))
        b=float(input("Enter the base of triangle : "))
        c=0.5*a*b
        print ("The are is",c)
    elif ar==4:
        a=float(input("Enter the radius of circle : "))
        b=(22/7)*(a**2)
        print ("The area is : ",b)
    else:("Invalid Argument")

elif ch==6:
    print ("Choose your objective from the following")
    print ("1.Cube")
    print ("2.Cuboid")
    print ("3.Cylinder")
    print ("4.Sphere")

    v=int(input("Enter Choice(1-4): "))

    if v==1:
        a=float(input("Enter the side of cube : "))
        b=a**3
        print ("The volume is",b)
    elif v==2:
        a=float(input("Enter the length of cuboid : "))
        b=float(input("Enter the breadth of cuboid : "))
        c=float(input("Enter height of cuboid : "))
        d=a*b*c
        print ("The volume is",d)
    elif v==3:
        a=float(input("Enter the height of cylinder : "))
        b=float(input("Enter the radius of cylinder : "))
        c=(22/7)*(b**2)*a
        print ("The volume is",c)
    elif v==4:
        a=float(input("Enter the radius of circle : "))
        b=(4/3)*(22/7)*(a**3)
        print ("The volume is : ",b)
    else:("Invalid Argument")

else:("Invalid Argument")
print ("Thank You for using this code")
print ("If you have time,it would be appreciated if you visit the following site for more")
print ("https://youtu.be/41iWg91yFv0")