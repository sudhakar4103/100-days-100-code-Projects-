print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tipped_bill=bill+bill*(tip/100)
print(tipped_bill)

result=tipped_bill/people

print(f"Split for each is = {round(result)} and uuor total bill withs tip is {tipped_bill}" )

