from string import ascii_letters, ascii_lowercase, ascii_uppercase

from ciphers.utils.constants import GERMAN_LETTER_FREQUENCIES
from ciphers.utils.string import (
    get_letter_frequencies,
    letter_to_shift,
    sanitize_umlauts,
    shift_to_letter,
)
from ciphers.utils.types import CipherBreakResult, LetterFrequencyDict, TranslationDict


def encode(text: str, key: int | str) -> str:
    shift = letter_to_shift(key)
    cleaned_text = sanitize_umlauts(text)
    translation_dict = get_caesar_translation_dict(shift)
    return cleaned_text.translate(translation_dict)


def decode(text: str, key: int | str) -> str:
    shift = letter_to_shift(key)
    return encode(text, -shift)


def break_cipher(text: str) -> CipherBreakResult:
    letter_frequencies = get_letter_frequencies(text)
    mean_frequency_diff_by_shift: dict[int, float] = {
        shift: get_mean_frequency_diff(
            letter_frequencies, GERMAN_LETTER_FREQUENCIES, shift
        )
        for shift in range(26)
    }
    guessed_shift = -min(
        mean_frequency_diff_by_shift.items(), key=lambda item: item[1]
    )[0]
    return CipherBreakResult(
        key=shift_to_letter(guessed_shift), decoded_text=decode(text, guessed_shift)
    )


def get_mean_frequency_diff(
    letter_frequencies: LetterFrequencyDict,
    target_letter_frequencies: LetterFrequencyDict,
    shift: int = 0,
) -> float:
    return sum(
        abs(frequency - target_letter_frequencies[caesar_shift_letter(letter, shift)])
        for letter, frequency in letter_frequencies.items()
    )


def get_caesar_translation_dict(shift: int) -> TranslationDict:
    return {
        ord(letter): shifted_letter
        for letter, shifted_letter in zip(ascii_letters, get_shifted_alphabet(shift))
    }


def get_shifted_alphabet(shift: int) -> str:
    return (
        ascii_lowercase[shift:]
        + ascii_lowercase[:shift]
        + ascii_uppercase[shift:]
        + ascii_uppercase[:shift]
    )


def caesar_shift_letter(letter: str, shift: int) -> str:
    return letter.translate(get_caesar_translation_dict(shift))
