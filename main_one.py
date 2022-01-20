# Activities & Practices

# 1st Activity "Magic 8-Ball"
# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
# We’ll be using the following 9 possible answers for our Magic 8-Ball:
# [Yes - definitely] | [It is decidedly so] | [Without a doubt] | [Reply hazy, try again] | [Ask again later] | [Better not tell you now] | [My sources say no] | [Outlook not so good] | [Very doubtful]
# The output of the program will have the following format:
# [Name] asks: [Question] | Magic 8-Ball’s answer: [Answer]
import random

#name = "Gomba"
name = ""
question = "Are you awake??"
#question = ""
answer = ""

random_number = random.randint(1, 9)
#print(random_number)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Better not tell you now"
elif random_number == 4:
    answer = "My sources say no"
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else:
    answer = "Error"  


if question == "":
    print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
elif name == "":
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)        

#print(name + " asks: " + question)
#print("Magic 8-Ball's answer: " + answer)  

# if name == "":
#     print("Question: " + question)
# else:
#     print(name + " asks: " + question)                         




print("-----------------------------------------------------")




# 2nd Activity "Sal's Shipping"

# In this activit, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.
# Sal’s Shippers has several different options for a customer to ship their package:
# Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
# Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
# Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

# Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

weight = 24
# Ground Shipping
if weight <= 2:
    cost_ground = weight * 1.5 + 20
elif weight <= 6:
    cost_ground = weight * 3.00 + 20
elif weight <= 10:
    cost_ground = weight * 4.00 + 20
else:
    cost_ground = weight * 4.75 + 20

print("Ground Shipping $" + str(cost_ground))

# Ground Shipping Premium
cost_ground_premium = 125.00

print("Ground Shipping Premium $" + str(cost_ground_premium))

# Drone Shipping
if weight <= 2:
    cost_drone = weight * 4.5
elif weight <= 6:
    cost_drone = weight * 9.00
elif weight <= 10:
    cost_drone = weight * 12.00
else:
    cost_drone = weight * 14.25

print("Drone Shipping: $" + str(cost_drone))                    

