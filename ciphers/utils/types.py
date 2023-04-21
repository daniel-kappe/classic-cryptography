from typing import NamedTuple

TranslationDict = dict[int, str]
LetterFrequencyDict = dict[str, float]
LetterCountDict = dict[str, int]
WordCounts = dict[str, int]


class CipherBreakResult(NamedTuple):
    key: int | str
    decoded_text: str
