Progress=[]
Trailer=[]
Retriver=[]
Exclude=[]

while True:
    try:
        Pass=int(input("Please enter your credits at pass: "))
        if Pass %20!=0:
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
        print("Integer required")
        continue
    Total=(Pass +Defer +Fail)
    if Total!=120:
        print("Total incorret")
        continue
    Credits= Pass,Defer,Fail
    if Pass==120:
            print("Progress")
            Progress.append(Credits)
            len(Progress)
            
    elif Pass==100:
            print("Progress(module trailer)")
            Trailer.append(Credits)
            len(Trailer)
            
    elif 0<=Pass<=80 and 0<=Defer<=120 and 0<=Fail<=60:
            print("Module retrieve")
            Retriver.append(Credits)
            len(Retriver)
            
    elif 0<=Pass<=40 and 0<=Defer<=40 and 80<=Fail<=120:
            print("Exclude")
            Exclude.append(Credits)
            len(Exclude)
            
    print("\v")
    x=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
    if x=="q":
     break
    else:
      print("\v")
      continue
      

print("\v")
print(65*"-")
print("Histogram")
print("Progress",len(Progress),":",len(Progress)*"*")
print("Trailer",len(Trailer),":",len(Trailer)*"*")
print("Retriver",len(Retriver),":",len(Retriver)*"*")
print("Exclude",len(Exclude),":",len(Exclude)*"*")
total_outcomes=(len(Progress) + len(Trailer) +len(Retriver) +len(Exclude))
print(total_outcomes,"outcomes in total")
print(65*"-")


print("Part 2")
for Credits in Progress:
    print("Progress - ",str(Credits)[1:-1])
for Credits in Trailer:
    print("Progress(module trailer) - ",str(Credits)[1:-1])
for Credits in Retriver:
    print("Module retrieve - ",str(Credits)[1:-1])
for Credits in Exclude:
    print("Exclude - ",str(Credits)[1:-1])

print("\v")


with open("output.txt","w") as external_file:
   print("Part3:",file=external_file)
   for Credits in Progress:
     print("Progress - "+str(Credits)[1:-1], file=external_file)
   for Credits in Trailer:
     print("Progress(module trailer) - "+str(Credits)[1:-1], file=external_file)
   for Credits in Retriver:
     print("Module retrieve - ",str(Credits)[1:-1],file=external_file)
   for Credits in Exclude:
     print("Exclude - "+str(Credits)[1:-1],file=external_file)
external_file.close()
