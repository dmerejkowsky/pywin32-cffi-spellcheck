win32 cffi spellchecker
========================

This is a thin wrapper on top of the `Spellcheck.h <https://docs.microsoft.com/en-us/windows/win32/api/spellcheck/>`_ 
win32 API.

It is used as a backend of `PyEnchant <https://github.com/pyenchant/pyenchant>`_ on Windows.

Usage
-----

.. code-block:: python

    checker = SpellChecker("en-US")
    ok = checker.check("helo")
    assert not ok
    suggestions = checker.suggest("helo")
    print(suggestions)
    
    # outputs:
    # ['hello', 'halo', 'helot', 'hele', 'help', 'hell', 'held', 'hellos', 'hero', 'helm']
