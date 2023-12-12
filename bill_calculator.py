#Bill split calculator

print("Welcome to the tip calculator")
total = float(input("What was your total bill? $"))

wrong_tip = True
avaible_tip = [10,12,15]
while(wrong_tip):
    tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
    if(tip in avaible_tip):
        tip = tip / 100
        total = total + (total * tip)
        break
    if(tip not in avaible_tip):
        print("Please, enter a valid tip")

total_people = int(input("How many people would you like to split the bill on? "))

total_payment = "%.2f"%(total / total_people)
print(f"Each person needs to people ${total_payment}")
