#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
input("How many people to split the bill? ")
final_tip = float(total_bill) / 100 * 12
final_bill = float(total_bill) + float(final_tip)
individual_bill = final_bill / 5
final_individual_bill = "{:.2f}".format(individual_bill)
print(f"Each person should pay: ${final_individual_bill}")