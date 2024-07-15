import random

GUESSED_LETTERS = []


def get_wordlist_from_file():
    with open("words.txt", "rt", encoding="utf-8") as file:
        return file.readlines()


def choose_word(words: list[str]) -> str:
    """Choose a random word from the words list.

    As a default (if list is empty), "Python" is
    returned.

    :param words: list of words
    :return: random word from list of words
    """
    if len(words) == 0:
        return "Python"
    word = random.choice(words)
    return word.strip()


def show_hidden_word(word: str) -> str:
    hidden_string = ""
    for letter in word:
        if letter.lower() in GUESSED_LETTERS:
            hidden_string += letter
        else:
            hidden_string += "_"
    return hidden_string


def guess_letter(word: str) -> bool:
    guess = input("Welcher Buchstabe soll es sein? ")
    if len(guess) == 1 and guess.isalpha():
        if guess.lower() in word.lower():
            GUESSED_LETTERS.append(guess.lower())
            return True
        return False


if __name__ == "__main__":
    wordlist = get_wordlist_from_file()
    chosen_word = choose_word(wordlist)

    n = 10
    while n > 0:
        hidden_word = show_hidden_word(chosen_word)
        print(hidden_word)
        if "_" not in hidden_word:
            print("Super! Du hast einen Preis gewonnen!")
            break
        if not guess_letter(chosen_word):
            n -= 1
        print(f"Du hast noch {n} Versuche.")
