def length_converter():
    print("\n Length Converter")
    print("1. KM to Miles")
    print("2. Miles to KM")

    choice = input("Choose : ")
    value = float(input("Input Value : "))

    if choice == "1":
        print(f"{value} KM = {value * 0.621371} Miles\n")
    elif choice == "2":
        print(f"{value} Miles = {value / 0.621371} KM")


def weight_converter():
    print("\n Weight Converter")
    print("1. KG to Pounds")
    print("2. Pounds to KG")

    choice = input("Choose : ")
    value = float(input("Input Value : "))

    if choice == "1":
        print(f"{value} KG = {value * 2.20462} Pounds\n")
    elif choice == "2":
        print(f"{value} Pounds = {value / 2.2046} KG")


weight_converter()