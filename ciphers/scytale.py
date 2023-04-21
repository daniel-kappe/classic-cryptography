from math import ceil

from ciphers.utils.constants import GERMAN_MOST_COMMON_WORDS
from ciphers.utils.iterators import grouper, transpose
from ciphers.utils.types import CipherBreakResult


def encode(text: str, key: int, fill: str = " ") -> str:
    chunked_text = grouper(text, key, fillvalue=fill)
    transposed_chunks = transpose(chunked_text)
    return "".join("".join(chunk) for chunk in transposed_chunks)


def decode(text: str, key: int) -> str:
    number_of_chunks = ceil(len(text) / key)
    return encode(text, number_of_chunks)


def break_cipher(text: str) -> CipherBreakResult:
    block_size = 2
    decode_candidate = decode(text, block_size)
    while block_size < len(text) and not has_enough_real_words(decode_candidate):
        block_size += 1
        decode_candidate = decode(text, block_size)
    return CipherBreakResult(key=block_size, decoded_text=decode_candidate)


def has_enough_real_words(text: str) -> bool:
    """
    The word list `GERMAN_MOST_COMMON_WORDS` covers more than 54% of words used in written texts.
    Futhermore a typical german word has about 6 letters
    (https://www.duden.de/sprachwissen/sprachratgeber/Durchschnittliche-Lange-eines-deutschen-Wortes)
    """
    words_per_letter = get_real_words_per_letter(text) * 6
    return (
        words_per_letter > 0.4
    )  # have some leeway, because texts could use a lot of uncommon, long words


def get_real_words_per_letter(text: str) -> float:
    found_words = 0
    for word in GERMAN_MOST_COMMON_WORDS:
        found_words += text.count(word)
    return found_words / len(text)
