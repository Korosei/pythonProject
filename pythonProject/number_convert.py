convert_list = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

phone_number = input("Phone: ").strip()
phone_number = phone_number.replace(" ", "")

for num in phone_number:
    print(convert_list[int(num)], end = " ")