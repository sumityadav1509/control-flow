# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_days=(90*365)-int(age)
# print(total_days) 
total_weeks=(52*90)-int(age)
# print(total_weeks)
total_month=(90*12)-int(age)
# print(total_month) 

print(f"You have {total_days} days , {total_weeks} weeks , {total_month} months remaining ")