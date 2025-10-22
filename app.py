def is_positive(num: int) -> bool:
    return num > 0


def is_negative(num: int) -> bool:
    return num < 0


def main():
    print(f"is_positive(1): {is_positive(1)}")
    print(f"is_positive(-1): {is_positive(-1)}")
    print(f"is_positive(0): {is_positive(0)}")
    print(f"is_negative(-2): {is_negative(-2)}")
    print(f"is_negative(2): {is_negative(2)}")
    print(f"is_negative(0): {is_negative(0)}")


if __name__ == "__main__":
    main()
