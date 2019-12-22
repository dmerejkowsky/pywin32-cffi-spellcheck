typedef struct ISpellCheckerFactory ISpellCheckerFactory;
typedef struct ISpellChecker ISpellChecker;

ISpellCheckerFactory*  sc_create_factory();
ISpellChecker* sc_create_checker(ISpellCheckerFactory* factory, const wchar_t*  const tag);
int sc_check(ISpellChecker* checker, const wchar_t* const word);
wchar_t** sc_suggest(ISpellChecker* checkr, const wchar_t* const word);