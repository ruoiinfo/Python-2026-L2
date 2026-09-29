import math


# 1. Calculate the area of a circle
def exercise_1():
    radius = float(input("Enter circle radius? "))
    area = math.pi * radius ** 2
    print("Circle area =", round(area, 1))


# 2. Convert Celsius to Fahrenheit
def exercise_2():
    celsius = float(input("Enter the temperature in Celsius? "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:g} (C) = {fahrenheit:g} (F)")


# 3. Check whether a number is prime
def exercise_3():
    n = int(input("Enter a number? "))

    if n < 2:
        print(n, "is a NOT prime number")
        return

    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is a NOT prime number")


# 4. Check whether a number is perfect
def exercise_4():
    n = int(input("Enter a number? "))

    if n <= 0:
        print(n, "is a NOT perfect number")
        return

    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i

    if total == n:
        print(n, "is a perfect number")
    else:
        print(n, "is a NOT perfect number")


# 5. Find favorite color in a list
def exercise_5():
    colors = ["Blue", "Yellow", "Black", "Red", "White"]

    color = input("What is your favorite color? ")

    if color in colors:
        print("Your color is at index", colors.index(color), "in my list")
    else:
        print("Sorry, I could not find your color")


# 6. Using range() to create sequences
def exercise_6():
    range1 = range(0, 7)
    range2 = range(1, 11, 3)
    range3 = range(5, 0, -1)
    range4 = range(6, -3, -2)

    print("range1:", *range1)
    print("range2:", *range2)
    print("range3:", *range3)
    print("range4:", *range4)


# 7. Remove dollar signs from a string
def remove_dollar_sign(s):
    return s.replace("$", "")


def exercise_7():
    s = input("Enter a string containing $: ")
    print("Result:", remove_dollar_sign(s))


# 8. Extract even numbers from a list
def extract_even(l):
    return [x for x in l if x % 2 == 0]


def exercise_8():
    numbers = [1, 4, 5, -1, 10]
    print("Original list:", numbers)
    print("Even numbers:", extract_even(numbers))


# 9. Calculate factorial
def factorial(n):
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def exercise_9():
    n = int(input("Enter a non-negative integer: "))

    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"{n}! =", factorial(n))


# 10. Get all divisors of a number
def get_divisors(n):
    if n == 0:
        return []

    n_abs = abs(n)
    return [i for i in range(1, n_abs + 1) if n_abs % i == 0]


def exercise_10():
    n = int(input("Enter a number: "))

    if n == 0:
        print("0 has infinitely many divisors.")
    else:
        print("Divisors:", get_divisors(n))


# 11. Calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def exercise_11():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    print("Distance =", distance(x1, y1, x2, y2))


# 12. Print a pattern of size m x n
def print_pattern(m, n):
    for i in range(m):
        print("* " * n)


def exercise_12():
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))
    print_pattern(m, n)


# Main menu
def main():
    while True:
        print("\n========== LABWORK 1 ==========")
        print("1. Circle area")
        print("2. Celsius to Fahrenheit")
        print("3. Prime number")
        print("4. Perfect number")
        print("5. Favorite color")
        print("6. Range sequences")
        print("7. Remove dollar sign")
        print("8. Extract even numbers")
        print("9. Factorial")
        print("10. Divisors")
        print("11. Distance between two points")
        print("12. Print pattern")
        print("0. Exit")

        choice = input("Choose an exercise (0-12): ")

        if choice == "1":
            exercise_1()
        elif choice == "2":
            exercise_2()
        elif choice == "3":
            exercise_3()
        elif choice == "4":
            exercise_4()
        elif choice == "5":
            exercise_5()
        elif choice == "6":
            exercise_6()
        elif choice == "7":
            exercise_7()
        elif choice == "8":
            exercise_8()
        elif choice == "9":
            exercise_9()
        elif choice == "10":
            exercise_10()
        elif choice == "11":
            exercise_11()
        elif choice == "12":
            exercise_12()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0-12.")


if __name__ == "__main__":
    main()
