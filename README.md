# Classic Cryptography
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

This is a group exercise for the course "Programmiersprachen zur Datenanalyse" at FH Bielefeld University of Applied Sciences.
The exercises are meant to practise and deepen the understanding of the python language on interesting, small projects.

## Scope
The exercise is to pick at least one of the following classic cryptography ciphers
* [the scytale](https://en.wikipedia.org/wiki/Scytale)
* [Caesar's cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
* [the Vignère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

and implement
* a function to encrypt a text
* a function to decrypt a text with a known key
* a function to break the cipher and decrypt a text without a key

## This solution
I do not claim to have found the best solution, but I tried my best to come up with one that works well and follows Python coding best practises.
I always welcome questions and hints to improve this solution.

## How to run it
The code has no dependencies. For development and package management, I use poetry with the listed dev dependencies.

`pytest` is used to test the functionality of each solution. To run the tests use
```shell
poetry install --with=dev
poetry run pytest
```