gallons=float(input("enter the num of gallons of gasoline : "))

liters=(gallons*3.7854)

barrel=(gallons/19.5)

co2=(gallons*20)

ethanol_gallons=((gallons*115000)/75700)

price=(gallons*4.00)

print("Gallons of gasoline: ", gallons)
print("Equivalent liters: ", liters)
print("Barrels of oil required: ", barrel)
print("Pounds of CO2 produced: ", co2)
print("Equivalent energy in gallons of ethanol: ", ethanol_gallons)
print("Cost in US dollars: $", price)
