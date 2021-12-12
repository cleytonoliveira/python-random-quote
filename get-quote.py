import random


def random_quote(last):
    random_quote = random.randint(0, last)
    return random_quote


def primary():
    with open("quotes.txt") as file:
        quotes = file.readlines()
        last = len(quotes) - 1

        for i in range(2):
            print(f'{i + 1} - {quotes[random_quote(last)]}')


if __name__ == "__main__":
    primary()
