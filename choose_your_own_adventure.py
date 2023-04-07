name = input("Type ypur name: ")
print("welcome",name, "to this adventure!")

answer = input("You're at Tom Mboya street turn right orleft and move straight😁! ")

if answer == "right":
   answer = input("You're on your way to Gikomba market ,you can now shop or stare")  
   if answer == "shop":
     print("Yass!! your christmas eve is sorted")
   elif answer == "stare ":
     print("You look confused maam do something but do not steal")
   else:
        print("It looks something is wrong perharps you're lost!")

elif answer == "left":
    answer = input ("You come to a junction,it is congested,you can wait or cross it")
    if answer == "wait":
        print("Be patient it will be clear soon")
    elif answer == "cross":
       print("You're really risking")
    else:   
       print("you're lost brother Abas")
else:
    print("No no!! go back you're lost")

