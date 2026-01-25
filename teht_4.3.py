numbers = []
while True:
    user_input = input("Syötä luku: ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Virheellinen syöte.")

if numbers:
    print(f"Pienin luku: {min(numbers)}")
    print(f"Suurin luku: {max(numbers)}")
