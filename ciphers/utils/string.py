from collections import Counter
from re import sub

from ciphers.utils.types import LetterCountDict, LetterFrequencyDict

LETTERS_IN_ALPHABET = 26


def sanitize_umlauts(text: str) -> str:
    return text.translate(
        {ord("ä"): "ae", ord("ö"): "oe", ord("ü"): "ue", ord("ß"): "ss"}
    )


def letter_to_shift(key: str | int) -> int:
    return ord(key.upper()) - 65 if isinstance(key, str) else key


def get_every_nth(text: str, n: int) -> list[str]:
    return [text[i::n] for i in range(n)]


def keyword_to_shifts(keyword: str) -> list[int]:
    return [letter_to_shift(letter) for letter in keyword]


def shift_to_letter(shift: int) -> str:
    return chr(shift % 26 + 65)


def get_letter_frequencies(text: str) -> LetterFrequencyDict:
    ascii_letter_extracted_text = drop_none_ascii_letters(text).upper()
    return {
        letter: letter_count / len(ascii_letter_extracted_text)
        for letter, letter_count in get_letter_counts(
            ascii_letter_extracted_text
        ).items()
    }


def get_letter_counts(text: str) -> LetterCountDict:
    ascii_letter_extracted_text = drop_none_ascii_letters(text).upper()
    return Counter(ascii_letter_extracted_text)


def drop_none_ascii_letters(text: str) -> str:
    return sub("[^a-zA-Z]", "", text)
