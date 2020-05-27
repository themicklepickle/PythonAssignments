from random_word import RandomWords
r = RandomWords()

word = r.get_random_word(hasDictionaryDef="true", minLength=3, maxLength=10, minDictionaryCount=8, includePartOfSpeech="noun,verb,adjective")
print(word)

