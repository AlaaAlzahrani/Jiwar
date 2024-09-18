import re

def split_list(input_list, n_splits):
    """Splits a list into n nearly equal parts."""
    avg_len = len(input_list) / float(n_splits)
    splits = []
    last = 0.0

    while last < len(input_list):
        splits.append(input_list[int(last):int(last + avg_len)])
        last += avg_len

    return splits

def count_letters(word):
    """Count the number of letters in a word."""
    return len(word)

def count_phonemes(ipa):
    """Count the number of phonemes in an IPA transcription, ignoring None values."""
    if ipa is None:
        return 0
    cleaned_ipa = re.sub(r'[ˈˌ.]', '', ipa)
    return len(cleaned_ipa)