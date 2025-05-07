def age(a):
    try:
        a=int(a)
        if a<0:
           raise ValueError
        if a%2 == 0:
           print("Your age is even")
        else:
            print("Your age is odd")
    except ValueError as e:
        print("ValueError:",e)
i=input("Enter your age:")
age(i)
