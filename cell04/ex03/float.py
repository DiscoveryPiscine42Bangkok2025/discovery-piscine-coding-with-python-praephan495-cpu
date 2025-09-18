num = input("Give me a numbar:")
try:
    val = float(num)
    if val.is_integer():
        print("This number is an integer")
    else:
        print("This number is a decimal.")
except ValueError:
    print("This is not avalid number.")