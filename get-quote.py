import random


def random_quote(last):
    random_quote = random.randint(0, last)
    return random_quote


def add_new_quote(quote):
    with open("quotes.txt", "a") as file:
        file.write(f"{quote}\n")


def main():
    try:
        response = input("Do you want to add a new quote? ")
        if response == "yes":
            quote = input("Type your new quote: ")
            add_new_quote(quote)

    except KeyboardInterrupt:
        print("\nCTRL + C exception. Please run again!")

    else:
        with open("quotes.txt") as file:
            quotes = file.readlines()
            last = len(quotes) - 1

            for i in range(2):
                print(f"{i + 1} - {quotes[random_quote(last)].strip()}")


if __name__ == "__main__":
    main()
