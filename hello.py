def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to your Python program."


def main() -> None:
    user_name = input("What is your name? ")
    print(greet(user_name))


if __name__ == "__main__":
    main()
