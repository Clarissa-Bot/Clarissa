from mtranslate import translate

def translate_phrase(phrase='Hello', to_lang='ar'):
	return translate(phrase, to_lang)

print(translate_phrase(phrase="Hello", to_lang='fr'))