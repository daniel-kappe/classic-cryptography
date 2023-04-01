from string import ascii_uppercase

import pytest

from ciphers.caesar import break_cipher as caesar_break_cipher
from ciphers.caesar import decode as caesar_decode
from ciphers.caesar import encode as caesar_encode
from ciphers.utils.examples import ENCRYPTED_CAESAR_GERMAN, UNENCRYPTED_GERMAN
from ciphers.utils.string import sanitize_umlauts


@pytest.mark.parametrize("key", ascii_uppercase)
def test_caesar_encode(key):
    # given
    text = UNENCRYPTED_GERMAN

    # when
    encrypted_text = caesar_encode(text, key)

    # then
    assert encrypted_text == ENCRYPTED_CAESAR_GERMAN[key]


@pytest.mark.parametrize("key", ascii_uppercase)
def test_caesar_decode(key):
    # given
    encrypted_text = ENCRYPTED_CAESAR_GERMAN[key]

    # when
    decrypted_text = caesar_decode(encrypted_text, key)

    # then
    assert decrypted_text == sanitize_umlauts(UNENCRYPTED_GERMAN)


@pytest.mark.parametrize("unknown_key", ascii_uppercase)
def test_caesar_break_cipher(unknown_key):
    # given
    encrypted_text = ENCRYPTED_CAESAR_GERMAN[unknown_key]

    # when
    key, decoded_text = caesar_break_cipher(encrypted_text)

    # then
    assert key == unknown_key
    assert decoded_text == sanitize_umlauts(UNENCRYPTED_GERMAN)
