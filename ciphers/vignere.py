from itertools import zip_longest
from statistics import mean

from ciphers.caesar import break_cipher as caesar_break_cipher
from ciphers.caesar import encode as caesar_encode
from ciphers.utils.examples import LONGER_GERMAN_TEXT
from ciphers.utils.string import (
    drop_none_ascii_letters,
    get_every_nth,
    get_letter_counts,
    letter_to_shift,
    sanitize_umlauts,
    shift_to_letter,
)
from ciphers.utils.types import CipherBreakResult


def encode(text: str, keyword: str) -> str:
    cleaned_text = sanitize_umlauts(text)
    text_grouped_every_nth = get_every_nth(cleaned_text, len(keyword))
    encoded_groups = [
        caesar_encode(group, key) for group, key in zip(text_grouped_every_nth, keyword)
    ]
    return "".join(
        "".join(letters) for letters in zip_longest(*encoded_groups, fillvalue="")
    )


def decode(text: str, keyword: str) -> str:
    return encode(text, invert_keyword(keyword))


def break_cipher(text: str, threshold: float = 1.75) -> CipherBreakResult:
    current_index_of_coincidence = get_index_of_coincidence(text)
    text_grouped_every_nth = [text]
    n = 1
    while current_index_of_coincidence < threshold and n < len(text) / 52:
        n += 1
        text_grouped_every_nth = get_every_nth(text, n)
        current_index_of_coincidence = get_index_of_coincidence_mean(
            text_grouped_every_nth
        )
    keys = [caesar_break_cipher(group).key for group in text_grouped_every_nth]
    keyword = "".join(map(str, keys))
    return CipherBreakResult(key=keyword, decoded_text=decode(text, keyword))


def get_index_of_coincidence(text: str) -> float:
    text_length = len(drop_none_ascii_letters(text))
    letter_counts = get_letter_counts(text)
    return sum(
        letter_count * (letter_count - 1) for letter_count in letter_counts.values()
    ) / (text_length * (text_length - 1) / 26)


def get_index_of_coincidence_mean(text_groups: list[str]) -> float:
    return mean([get_index_of_coincidence(text) for text in text_groups])


def invert_keyword(keyword: str) -> str:
    return "".join(
        shift_to_letter((-letter_to_shift(letter)) % 26) for letter in keyword
    )


if __name__ == "__main__":
    print(encode(LONGER_GERMAN_TEXT, "geheim"))
