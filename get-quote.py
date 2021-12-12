import random


def primary():
    file = open("quotes.txt")
    quotes = file.readlines()
    last = len(quotes) - 1
    random_quote = random.randint(0, last)
    file.close()

    print(quotes[random_quote])


if __name__ == "__main__":
    primary()
