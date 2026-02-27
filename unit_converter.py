def get_number():
    while True:
        try:
            return float(input("Enter Number : "))
        except ValueError:
            print("Enter a Valid Number!\n")

#length
def length_converter():
    print("\n Length Converter")
    print("1. KM to Miles")
    print("2. Miles to KM")
    print("3. Meters → Feet")
    print("4. Feet → Meters")
    print("5. CM → Inches")
    print("6. Inches → CM")

    choice = input("Choose : ")
    value = get_number()

    if choice == "1":
        print(f"{value} KM = {value * 0.621371} Miles\n")
    elif choice == "2":
        print(f"{value} Miles = {value / 0.621371} KM\n")
    elif choice == "3":
        print(f"{value} M = {value * 3.28084:.2f} Feet\n")
    elif choice == "4":
        print(f"{value} Feet = {value / 3.28084:.2f} Meters\n")
    elif choice == "5":
        print(f"{value} CM = {value * 0.393701:.2f} Inches\n")
    elif choice == "6":
        print(f"{value} Inches = {value / 0.393701:.2f} CM\n")
    else:
        print("Invalid Choice\n")

#weight
def weight_converter():
    print("\n Weight Converter")
    print("1. KG to Pounds")
    print("2. Pounds to KG")
    print("3. Grams → Ounces")
    print("4. Ounces → Grams")

    choice = input("Choose : ")
    value = get_number()

    if choice == "1":
        print(f"{value} KG = {value * 2.20462} Pounds\n")
    elif choice == "2":
        print(f"{value} Pounds = {value / 2.2046} KG\n")
    elif choice == "3":
        print(f"{value} Grams = {value * 0.035274:.2f} Ounces\n")
    elif choice == "4":
        print(f"{value} Ounces = {value / 0.035274:.2f} Grams\n")
    else:
        print("Invalid Choice\n")

#temperature
def temp_converter():
    print("\n Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")

    choice = input("Choose : ")
    value = get_number()

    if choice == "1":
        print(f"{value} °C = {(value * 9/5) + 32} °F\n")
    elif choice == "2":
        print(f"{value} °F = {(value - 32) * 5/9} °C\n")
    elif choice == "3":
        print(f"{value}°C = {value + 273.15:.2f}K\n")
    elif choice == "4":
        print(f"{value}K = {value - 273.15:.2f}°C\n")
    else:
        print("Invalid Choice\n")

#currency
def currency_converter():
    print("\nCurrency Converter (LKR)")
    print("1. LKR → USD")
    print("2. LKR → EUR")
    print("3. LKR → INR")
    print("4. LKR → AUD")

    choice = input("Choose: ")
    value = get_number()

    #Static exchange rates
    USD = 0.0033
    EUR = 0.0030
    INR = 0.27
    AUD = 0.0050

    if choice == "1":
        print(f"{value} LKR = {value * USD:.2f} USD\n")

    elif choice == "2":
        print(f"{value} LKR = {value * EUR:.2f} EUR\n")

    elif choice == "3":
        print(f"{value} LKR = {value * INR:.2f} INR\n")

    elif choice == "4":
        print(f"{value} LKR = {value * AUD:.2f} AUD\n")

    else:
        print("Invalid Choice\n")


while True:

    print("-----Unit Converter-----")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Currency (LKR)")
    print("5. Exit")

    mChoice = input("Choose Category : ")

    if mChoice == "1":
        length_converter()
    elif mChoice == "2":
        weight_converter()
    elif mChoice == "3":
        temp_converter()
    elif mChoice == "4":
        currency_converter()
    elif mChoice == "5":
        print("------------------------")
        break
    else:
        print("Invalid Choice!\n")