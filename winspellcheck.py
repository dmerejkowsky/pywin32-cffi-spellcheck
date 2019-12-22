import sys
from _spellcheck import ffi, lib


class Error(Exception):
    pass


class SpellChecker:
    factory = None

    def __init__(self, lang):
        if self.factory is None:
            new_factory = lib.sc_create_factory()
            if new_factory == ffi.NULL:
                raise Error("Could not create factory")
            SpellChecker.factory = new_factory

        self.checker = lib.sc_create_checker(self.factory, lang)
        if self.checker == ffi.NULL:
            raise Error("Could not create checker for lang: " + lang)

    def check(self, word):
        rc = lib.sc_check(self.checker, word)
        if rc == 0:
            return True
        elif rc == 1:
            return False
        else:
            raise Error("Could not check", word)

    def suggest(self, word):
        suggestions = lib.sc_suggest(self.checker, word)
        if suggestions == ffi.NULL:
            raise Error("Could not suggest for word: " + word)
        res = []
        i = 0

        while True:
            element = suggestions[i]
            if element == ffi.NULL:
                break
            else:
                res.append(ffi.string(element))
            i += 1

        return res


if __name__ == "__main__":
    main()
