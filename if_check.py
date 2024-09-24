indian = ["Samosa", "Daal-Bati", "Puranpoli", "Naan", "Mishti-dohi"]
chinese = ["Egg role", "Manchurian", "Fried rice", "Noodles"]
italian = ["Pizza", "Pasta", "Rissoto"]

dish = input("Enter a dish name : ")

if dish in indian:
    print("The Dish is Indian")
elif dish in italian:
    print("The Dish is Italian")
elif dish in chinese:
    print("The Dish is Chinese")
else:
    print("The dish is Unknown")       