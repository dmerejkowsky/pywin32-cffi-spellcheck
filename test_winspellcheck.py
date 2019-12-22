from winspellcheck import SpellChecker


def test_supports_en_us():
    SpellChecker("en-US")


def test_check():
    checker = SpellChecker("en-US")
    assert not checker.check("helo")
    assert checker.check("hello")


def test_non_ascii():
    checker = SpellChecker("fr-FR")
    assert checker.check("café")
    suggestions = checker.suggest("cafe")
    print(suggestions)


def test_suggest():
    checker = SpellChecker("en-US")
    suggestions = checker.suggest("helo")
    n = len(suggestions)
    assert n >= 1
    assert "hello" in suggestions
