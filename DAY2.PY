print("WELCOME TO TIP CALCULATOR")

bill = float(input("what was the total bill"))

tip = int(input("what percentage tip would u like to give? 10 , 12 or 15"))

people  = int(input("how many people to split bill in ?"))

calculation = (bill + (bill * (tip / 100))) / people

print("each person should pay = " ,calculation )


