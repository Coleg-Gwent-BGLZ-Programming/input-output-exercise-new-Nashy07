# Starter file for the Smoothie Shop Calculator exercise 
print("Welcome to the Smoothie Shop!")  
# TODO: Ask the user for their name using input()
name = input("What is your name? ")
# TODO: Ask how many smoothies they want to buy
smoothie_count = input(f"Hello {name}, how many smoothies would you like to buy? ")
# TODO: Convert the number of smoothies to an integer
smoothie_count = int(smoothie_count) 
# TODO: Calculate the total cost (each smoothie costs £3.50)
cost_per_smoothie = 3.50
total_cost = smoothie_count * cost_per_smoothie  
# TODO: Display a message using a formatted string
print(f"Thank you {name}! Your total for {smoothie_count} smoothies is £{total_cost:.2f}.")  
# OPTIONAL CHALLENGE:
# Ask if the customer wants a reusable cup for £1.00 extra
reusable_cup = input("Would you like a reusable cup for an extra £1.00? (yes/no) ")
# Add the cost if they say yes
if reusable_cup.lower() == 'yes':
    total_cost += 1.00  
    print("Great choice! Your reusable cup has been added.")
# Final total cost including the optional cup
print(f"Your final total is £{total_cost:.2f}. Thanks for shopping with us!")
