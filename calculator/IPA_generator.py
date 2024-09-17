import polars as pl
import re
from phonemizer import phonemize
from phonemizer.backend import EspeakBackend
from phonemizer.separator import Separator
import warnings
from functools import lru_cache
from tqdm import tqdm
from handlers.language_mapping import LANGUAGE_MAPPING

@lru_cache(maxsize=100)
def get_espeak_language_code(language):
    language = language.lower()
    
    if language in LANGUAGE_MAPPING:
        return language
    
    for code, name in LANGUAGE_MAPPING.items():
        if language == name.lower():
            return code
    
    if '-' in language:
        base_language = language.split('-')[0]
        if base_language in LANGUAGE_MAPPING:
            return base_language
    
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