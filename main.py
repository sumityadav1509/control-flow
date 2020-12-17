print("welcome to the rollercoaster ! ") 
height = int(input("What is your height in cm ? "))

if height>=120: 
  print("You can ride the rollercaoster ! ")
  age=int(input("Please enter your age !"))
  bill = 0
  if age<12:
    bill=5
    print("Child Ticket price is $5.")
 
  elif age<=18:
    bill=7
    print("Youth Ticket price is $7.")
  else:
   bill=12
   print("Adult Ticket price is $12.")
  
  wants_pic = input("Do you want to take a photo ? Y or N ")
  if wants_pic=="Y": 
    bill+=3 

  print(f"Your final bill is ${bill}")

else:
  print("Sorry , you have to grow taller before you ride !") 

