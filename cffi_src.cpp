#include "stdio.h"
#include "windows.h"
#include <iostream>

#include <Spellcheck.h>


ISpellCheckerFactory* sc_create_factory() {
	HRESULT hr;
	hr = CoInitializeEx(nullptr, COINIT_MULTITHREADED);
	if (FAILED(hr)) {
		std::cout << "Could not run CoInit, hr:" << hr << std::endl;
		return nullptr;
	}
			
	ISpellCheckerFactory *factory;

	hr = CoCreateInstance (__uuidof(SpellCheckerFactory), nullptr,
				CLSCTX_INPROC_SERVER, IID_PPV_ARGS (&factory));
	switch(hr) {
		case S_OK:
			return factory;
		case REGDB_E_CLASSNOTREG:
			std::cout << "class not registered" << std::endl;
			return nullptr;
		case CLASS_E_NOAGGREGATION:
			std::cout << "no aggregation" << std::endl;
			return nullptr;
		case E_NOINTERFACE:
			std::cout << "no interface" << std::endl;
			return nullptr;
		case E_POINTER:
			std::cout << "ppv is null" << std::endl;
			return nullptr;
		default:
			std::cout << "unknown hresult:" << hr << std::endl;
			return nullptr;
	}
    return nullptr;
}

ISpellChecker* sc_create_checker(ISpellCheckerFactory* factory, const wchar_t* const wtag) {
	ISpellChecker *checker;
		
	HRESULT hr;
	hr = factory->CreateSpellChecker (wtag, &checker);
		if (FAILED(hr)) {
		return nullptr;
	}
	
	return checker;
}


int sc_check(ISpellChecker* checker, const wchar_t *const word)
{
	IEnumSpellingError *errors;
	ISpellingError *error = nullptr;
	HRESULT hr;

	hr = checker->Check (word, &errors);

	if (FAILED (hr))
		return -1; /* Error */

	if (errors->Next (&error) == S_OK)
	{
		error->Release ();
		errors->Release ();
		return 1; /* Spelling Issue */
	}
	else
	{
		errors->Release ();
		return 0; /* Correct */
	}
}

wchar_t** sc_suggest(ISpellChecker* checker, const wchar_t *const word) {
	IEnumString *suggestions;
	HRESULT hr;

	hr = checker->Suggest(word, &suggestions);

	if (FAILED (hr))
	{
		return nullptr;
	}

	wchar_t** res = (wchar_t**) malloc(256 * sizeof(wchar_t*));
	
	LPOLESTR wstr = nullptr;
	size_t i = 0;

	while (SUCCEEDED (suggestions->Next (1, &wstr, nullptr)) && i < 256 && wstr)
	{
		if (wstr)
		{
			res[i] = _wcsdup(wstr);
			i++;
		}
		CoTaskMemFree (wstr);
	}
	res[i] = nullptr;
	suggestions->Release ();

	return res;
}