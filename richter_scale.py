print("calculation based on richters scale")

pre_richter_value=[1.0,5.0,9.1,9.2,9.5]

#convertion factor from joules to TNT
tnt_conversion=4.184*(10**9)

#calculate energy and tnt
def calculate_energy(richter):
    energy=10**((1.5*richter)+4.8)
    tnt_equiv=energy/tnt_conversion
    return energy,tnt_equiv

#show pred_values
for values in pre_richter_value:
    energy,tnt=calculate_energy(values)
    print(f"Richter:{values},energy:{energy:.2e}joules, tnt:{tnt:.2f}tons")

#get user input
richter_input=float(input("\nEnter Richter value: "))  
energy_input,tnt_input=calculate_energy(richter_input)  
print(f"Richter:{richter_input}\nenergy:{energy_input:.2e}joules\ntnt:{tnt_input:.2f}tons\n")