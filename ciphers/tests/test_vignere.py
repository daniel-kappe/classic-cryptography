from ciphers.utils.examples import (
    LONGER_GERMAN_TEXT,
    LONGER_GERMAN_TEXT_ENCRYPTED_WITH_GEHEIM,
)
from ciphers.utils.string import sanitize_umlauts
from ciphers.vignere import break_cipher as vignere_break_cipher
from ciphers.vignere import decode as vignere_decode
from ciphers.vignere import encode as vignere_encode


def test_caesar_encode():
    # given
    text = LONGER_GERMAN_TEXT

    # when
    encrypted_text = vignere_encode(text, "GEHEIM")

    # then
    assert encrypted_text == LONGER_GERMAN_TEXT_ENCRYPTED_WITH_GEHEIM


def test_caesar_decode():
    # given
    encrypted_text = LONGER_GERMAN_TEXT_ENCRYPTED_WITH_GEHEIM

    # when
    decrypted_text = vignere_decode(encrypted_text, "GEHEIM")

    # then
    assert decrypted_text == sanitize_umlauts(LONGER_GERMAN_TEXT)


def test_caesar_break_cipher():
    # given
    encrypted_text = LONGER_GERMAN_TEXT_ENCRYPTED_WITH_GEHEIM

    # when
    key, decoded_text = vignere_break_cipher(encrypted_text)

    # then
    assert key == "GEHEIM"
    assert decoded_text == sanitize_umlauts(LONGER_GERMAN_TEXT)
