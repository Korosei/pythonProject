def weight_convert(weight, type):
    if type == 'lbs':
        return weight * .45
    else:
        return weight * 2.2

if __name__ == '__main__':
    weight, type = input().split()
    if type == "lbs":
        print(f"Your weight is {weight_convert(int(weight), type)} kilograms.")
    else:
        print(f"Your weight is {weight_convert(int(weight), type)} lbs.")