Pass=int(input("Please enter your creadits at pass: "))
Defer=int(input("Please enter your creadits at defer: "))
Fail=int(input("Please enter your creadits at fail: "))

if Pass==120:
    print("Progress")
elif Pass==100:
    print("Progress(module trailer)")
elif 0<=Pass<=80 and 0<=Defer<=120 and 0<=Fail<=60:
    print("Do not Progress-Module retriever")
elif 0<=Pass<=40 and 0<=Defer<=40 and 80<=Fail<=120:
    print("Exclude")
else:
    print("Invalid data set")
