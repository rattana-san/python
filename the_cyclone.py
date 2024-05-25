print("What is your height?")
height = int(input("enter height here: "))
print ("How many credits do you have?")
credit = int(input("enter your credit here: "))

if height >= 137 and credit >= 10:
  print("Enjoy the ride!")
elif height < 137 and credit >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and credit < 10:
  print("You do not have enough credits.")
else:
  print("You have not met either requirements.")