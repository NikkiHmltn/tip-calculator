# get total price, ask how many people they want to split it with, charge 15% tip
# (total * 0.15) / split = each_price

total_bill = float(input("What is the total bill?\n"))
split = float(input("How many people are you splitting the bill with?\n"))


gratuity = round(total_bill * 0.15, 2) 
print(gratuity)
each_price = ((total_bill + gratuity) / split)

print(f"The bill is ${total_bill}, there are(is) {int(split)} people splitting the bill, gratuity of 15% of the total bill, so each person will pay ${round(each_price, 2)}!")