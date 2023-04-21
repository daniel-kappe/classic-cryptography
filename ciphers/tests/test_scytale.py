import pytest

from ciphers.scytale import break_cipher as scytale_break_cipher
from ciphers.scytale import decode as scytale_decode
from ciphers.scytale import encode as scytale_encode
from ciphers.utils.examples import ENCRYPTED_SCYTALE_GERMAN, UNENCRYPTED_GERMAN


@pytest.mark.parametrize("key", list(range(2, 22)))
def test_scytale_encode(key):
    # given
    text = UNENCRYPTED_GERMAN

    # when
    encrypted_text = scytale_encode(text, key)

    # then
    assert encrypted_text == ENCRYPTED_SCYTALE_GERMAN[key]


@pytest.mark.parametrize("key", list(range(2, 22)))
def test_scytale_decode(key):
    # given
    encrypted_text = ENCRYPTED_SCYTALE_GERMAN[key]

    # when
    decrypted_text = scytale_decode(encrypted_text, key)

    # then
    assert decrypted_text.strip() == UNENCRYPTED_GERMAN


@pytest.mark.parametrize("unknown_key", list(range(2, 22)))
def test_scytale_break_cipher(unknown_key):
    # given
    encrypted_text = ENCRYPTED_SCYTALE_GERMAN[unknown_key]

    # when
    key, decrypted_text = scytale_break_cipher(encrypted_text)

    # then
    assert key == unknown_key
    assert decrypted_text.strip() == UNENCRYPTED_GERMAN
