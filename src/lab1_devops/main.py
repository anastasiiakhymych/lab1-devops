from lib import add_numbers, multiply_numbers, subtract_numbers


def main():
    a = 5
    b = 13

    print("Сума:", add_numbers(a, b))
    print("Добуток:", multiply_numbers(a, b))
    print("Різниця:", subtract_numbers(a, b))


if __name__ == "__main__":
    main()