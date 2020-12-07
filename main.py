# If the bill was $150.00 , split between 5 people , with 12% tip . 
# Each person should pay (150/5)*1.12 
# Round the result to 2 Decimal places = 33.66 

print("Welcome to the tip calculator") 
bill = float(input("What is the bill amount ? $"))
tip = int(input("What percentage tip you want to give ? "))
people = int(input("Number of people ? "))

total_amount = bill+(bill*tip/100)
each_person = total_amount/people
final_amount= round(each_person,2) 
print(f"Each person should pay: $ {final_amount}") 