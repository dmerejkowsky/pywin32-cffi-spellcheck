import random
import string
from winspellcheck import SpellChecker, Error


def random_string():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(20))


def test_supports_en_us():
    SpellChecker("en-US")


def test_check():
    checker = SpellChecker("en-US")
    assert not checker.check("helo")
    assert checker.check("hello")


def test_non_ascii():
    try:
        # Need the French language pack to be installed
        checker = SpellChecker("fr-FR")
    except Error:
        return
    assert checker.check("café")
    suggestions = checker.suggest("cafe")
    print(suggestions)


def test_suggest():
    checker = SpellChecker("en-US")
    suggestions = checker.suggest("helo")
    n = len(suggestions)
    assert n >= 1
    assert "hello" in suggestions


def test_add():
    checker = SpellChecker("en-US")
    bad_word = random_string()
    assert not checker.check(bad_word)
    checker.add(bad_word)
    assert checker.check(bad_word)


def test_remove():
    checker = SpellChecker("en-US")
    bad_word = random_string()
    checker.add(bad_word)
    assert checker.check(bad_word)
    checker.remove(bad_word)
    assert not checker.check(bad_word)