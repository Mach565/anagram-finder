import sys


def count_letters(word: str) -> dict[str, int]:
    char_dict: dict[str, int] = {}
    for char in word:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def is_anagram(word: dict[str, int], match: dict[str, int]) -> bool:
    for char in word:
        if char not in match:
            return False
        if word[char] != match[char]:
            return False
    for char in match:
        if char not in word:
            return False
    return True


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print("Enter word to find anagram of as an argument")
        exit()
    source_word = args[1]
    match_count = count_letters(source_word)
    words_file = "words_alpha.txt"
    with open(words_file) as f:
        words_list = f.read().splitlines()
    anagram_candiates: list[str] = []
    for word in words_list:
        if is_anagram(count_letters(word), match_count):
            anagram_candiates.append(word)
    print(anagram_candiates)
