# ask for car type (electric, hybrid, gas)
carType = int(
    (input("Is your car type: gas (type 1) hybrid (type 2) electric (type 3)")))

# if car type is gas or hybrid
if carType == 1 or 2:
    # determine cost of each gallon (varies by state)
    state = input("Are you from CA (enter 1) or OR (enter 2)? ")
    if state == 1:
        gasCost = 5.92
    else:
        gasCost = 4.72
    # determine miles per gallon
    mpg = int(input("What is your MPG?"))
    # determine yearly gallons used
    galUsed = int(input("What is your yearly gallons of gas used? "))
    yearlyCost = str(gasCost * galUsed)
    yearlyMiles = str(galUsed * mpg)
    print("You spend " + yearlyCost +
          " a year on driving " + yearlyMiles + " miles")

# if car type is electric
elif carType == 3:
    # determine cost of each gallon (varies by state)
    location = input(
        "Are you from Corvallis (enter 1) or anywhere else (enter 2)? ")
    if location == 1:
        powerCost = 0.1116
    else:
        powerCost = 0.3
    # determine miles per gallon
    mpg = int(input("What is your MPG? "))
    # determine yearly gallons used
    galUsed = int(input("What is your yearly gallons of gas used? "))
    yearlyCost = str(powerCost * galUsed)
    yearlyMiles = str(galUsed * mpg)
    print("You spend " + yearlyCost +
          " a year on " + yearlyMiles + " of miles")
