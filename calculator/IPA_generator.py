import polars as pl
import re
from phonemizer import phonemize
from phonemizer.backend import EspeakBackend
from phonemizer.separator import Separator
import warnings
from functools import lru_cache
from tqdm import tqdm

LANGUAGE_CODE_MAP = {
    'af': 'af', 'ar': 'ar', 'bg': 'bg', 'bn': 'bn', 'bs': 'bs',
    'ca': 'ca', 'cs': 'cs', 'da': 'da', 'de': 'de', 'el': 'el', 
    'en': 'en-us', 'en-us': 'en-us', 'en-gb': 'en-gb', 'eo': 'eo', 'es': 'es', 'et': 'et', 'eu': 'eu', 
    'fa': 'fa', 'fi': 'fi', 'fr': 'fr', 'he': 'he', 'hi': 'hi', 
    'hr': 'hr', 'hu': 'hu', 'hy': 'hy', 'id': 'id', 'is': 'is', 
    'it': 'it', 'ja': 'ja', 'ka': 'ka', 'kk': 'kk', 'ko': 'ko', 
    'lt': 'lt', 'lv': 'lv', 'mk': 'mk', 'ml': 'ml', 'mr': 'mr', 
    'ms': 'ms', 'ne': 'ne', 'nl': 'nl', 'no': 'nb', 'pa': 'pa', 
    'pl': 'pl', 'pt': 'pt', 'ro': 'ro', 'ru': 'ru', 'si': 'si', 
    'sk': 'sk', 'sl': 'sl', 'sq': 'sq', 'sr': 'sr', 'sv': 'sv', 
    'sw': 'sw', 'ta': 'ta', 'te': 'te', 'th': 'th', 'tr': 'tr', 
    'uk': 'uk', 'ur': 'ur', 'vi': 'vi'
}

@lru_cache(maxsize=1)
def get_espeak_language_code(language):
    language = language.lower()
    if language in ['ar', 'ar-tashkeel']:
        return 'ar'
    if language in LANGUAGE_CODE_MAP:
        return LANGUAGE_CODE_MAP[language]
    elif language in LANGUAGE_CODE_MAP.values():
        return language
    elif '-' in language:
        base_language = language.split('-')[0]
        if base_language in LANGUAGE_CODE_MAP:
            return LANGUAGE_CODE_MAP[base_language]
    raise ValueError(f"Unsupported language: {language}")

def clean_ipa(ipa):
    if ipa is None:
        return ""
    ipa = str(ipa)
    ipa = ipa.replace('"', '')
    ipa = re.sub(r'\([a-z]{1,4}\)', '', ipa)
    ipa = ipa.replace('#', '')
    return ipa

def generate_ipa(words, language, preserve_punctuation=False, with_stress=False, batch_size=1000):
    try:
        language_code = get_espeak_language_code(language)
    except ValueError as e:
        warnings.warn(str(e) + " IPA generation will be skipped.")
        return pl.Series([''] * len(words))

    separator = Separator(word=None, syllable=None, phone='')
    
    try:
        phonemizer_backend = EspeakBackend(language_code, preserve_punctuation=preserve_punctuation, with_stress=with_stress)
        
        def process_batch(batch):
            phonemized = phonemize(
                batch,
                language=language_code,
                backend='espeak',
                separator=separator,
                preserve_punctuation=preserve_punctuation,
                with_stress=with_stress
            )
            return [clean_ipa(p.strip()) for p in phonemized]

        words_series = pl.Series(words)
        ipa_transcriptions = []
        
        for i in tqdm(range(0, len(words), batch_size), desc="Generating IPA"):
            batch = words_series[i:i+batch_size].to_list()
            ipa_transcriptions.extend(process_batch(batch))
        
        return pl.Series(ipa_transcriptions)
    except RuntimeError as e:
        warnings.warn(f"Error during phonemization: {str(e)}. IPA generation will be skipped.")
        return pl.Series([''] * len(words))