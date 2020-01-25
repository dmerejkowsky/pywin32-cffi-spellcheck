typedef struct ISpellCheckerFactory ISpellCheckerFactory;
typedef struct ISpellChecker ISpellChecker;

// TODO: figure out a good error handling
ISpellCheckerFactory* sc_create_factory();
ISpellChecker* sc_create_checker(ISpellCheckerFactory* factory, const wchar_t* const tag);
int sc_check(ISpellChecker* checker, const wchar_t* const word);
wchar_t** sc_suggest(ISpellChecker* checker, const wchar_t* const word);
long sc_add(ISpellChecker* checker, const wchar_t* const word);
bool sc_remove(ISpellChecker* checker, const wchar_t* const word);
