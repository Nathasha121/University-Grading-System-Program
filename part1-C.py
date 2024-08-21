Total=0
Progress=0
Trailer=0
Retriver=0
Exclude=0
while True:
    try:
        Pass=int(input("Please enter your credits at pass: "))
        if Pass%20!=0:
           print("out of range")
           continue
        if Pass>=121 :
           print("out of range")
           continue
        Defer=int(input("Please enter your credits at defer: "))
        if Defer%20!=0:
          print("out of range")
          continue
        if Defer>=121:
           print("out of range")
           continue
        Fail=int(input("Please enter your credits at fail: "))
        if Fail%20!=0:
          print("out of range")
          continue
        if Fail>=121:
          print("out of range")
          continue
      
    except ValueError:
        print("Inter required")
        continue
    Total=(Pass +Defer +Fail)
    if Total!=120:
        print("Total incorret")
        continue
    
    if Pass==120:
        print("Progress")
    elif Pass==100:
        print("Progress(module trailer)")
    elif 0<=Pass<=80 and 0<=Defer<=120 and 0<=Fail<=60:
        print("Do not Progress-Module retriever")
    elif 0<=Pass<=40 and 0<=Defer<=40 and 80<=Fail<=120:
        print("Exclude")
    x=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
    if x=="q":
         break
    else: 
         continue
