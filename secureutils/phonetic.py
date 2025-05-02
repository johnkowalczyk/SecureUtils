from commons_codec.language import soundex, metaphone, double_metaphone, refined_soundex

_soundex = soundex.Soundex()
_metaphone = metaphone.Metaphone()
_double = double_metaphone.DoubleMetaphone()
_refined = refined_soundex.RefinedSoundex()

def soundex_encode(word):
    return _soundex.encode(word)

def metaphone_encode(word):
    return _metaphone.encode(word)

def double_metaphone_primary(word):
    return _double.encode(word)

def refined_soundex_encode(word):
    return _refined.encode(word)
