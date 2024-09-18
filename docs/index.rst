# Jiwar Documentation

## Calculator

Welcome to Jiwar's documentation!
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   supported_languages
   measures
   CUSTOM_CORPUS
   LANGUAGES
   MEASURES
   USAGE

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


### IPA_generator.py

This module provides functions for generating International Phonetic Alphabet (IPA) transcriptions.

#### Main Functions:
- `get_espeak_language_code(language)`: Retrieves the eSpeak language code for a given language.
- `clean_ipa(ipa)`: Cleans and formats IPA transcriptions.
- `generate_ipa(words, language, preserve_punctuation=False, with_stress=False, batch_size=1000)`: Generates IPA transcriptions for a list of words.

### orthographic.py

This module calculates orthographic neighborhood measures.

#### Main Functions:
- `calculate_N(words, corpus)`: Calculates orthographic neighborhood size.
- `calculate_density(words, corpus)`: Calculates orthographic neighborhood density.
- `calculate_old20(words, corpus)`: Calculates Orthographic Levenshtein Distance-20.
- `calculate_clustering_coefficient(words, corpus)`: Calculates orthographic clustering coefficient.
- `calculate_neighborhood_frequency(words, corpus, frequencies)`: Calculates orthographic neighborhood frequency measures.

### phonological.py

This module calculates phonological neighborhood measures.

#### Main Functions:
- `calculate_N(words, corpus)`: Calculates phonological neighborhood size.
- `calculate_density(words, corpus)`: Calculates phonological neighborhood density.
- `calculate_pld20(words, corpus)`: Calculates Phonological Levenshtein Distance-20.
- `calculate_clustering_coefficient(words, corpus)`: Calculates phonological clustering coefficient.
- `calculate_neighborhood_frequency(words, corpus, frequencies)`: Calculates phonological neighborhood frequency measures.

### phonographic.py

This module calculates phonographic neighborhood measures.

#### Main Functions:
- `calculate_N(words, ipa_words, corpus_words, corpus_ipa)`: Calculates phonographic neighborhood size.
- `calculate_density(words, ipa_words, corpus_words, corpus_ipa)`: Calculates phonographic neighborhood density.
- `calculate_pgld20(words, ipa_words, corpus_words, corpus_ipa)`: Calculates Phonographic Levenshtein Distance-20.
- `calculate_clustering_coefficient(words, ipa_words, corpus_words, corpus_ipa)`: Calculates phonographic clustering coefficient.
- `calculate_neighborhood_frequency(words, ipa_words, corpus_words, corpus_ipa, frequencies)`: Calculates phonographic neighborhood frequency measures.

### utils.py

This module provides utility functions for the calculator.

#### Main Functions:
- `split_list(input_list, n_splits)`: Splits a list into nearly equal parts.
- `count_letters(word)`: Counts the number of letters in a word.
- `count_phonemes(ipa)`: Counts the number of phonemes in an IPA transcription.

## Handlers

### corpus_handler.py

This module handles corpus loading and processing.

#### Main Class: `CorpusHandler`
- `load_corpus(language_input, use_user_corpus=False, corpus_filename=None)`: Loads the appropriate corpus for a given language.
- `get_word_frequencies()`: Returns word frequencies from the loaded corpus.
- `corpus_info()`: Provides information about the loaded corpus.
- `get_frequency_columns()`: Returns the frequency columns from the corpus.

### file_handler.py

This module handles file reading and processing.

#### Main Class: `FileReader`
- `read_input_file(filename)`: Reads and processes the input file.
- `get_words(col)`: Retrieves words from a specific column.
- `get_orth_words()`: Retrieves orthographic words.
- `get_phon_words(input_is_phon_only=False)`: Retrieves phonological words.
- `get_pg_words()`: Retrieves phonographic word pairs.

### language_mapping.py

This module provides language mapping and validation functions.

#### Main Functions:
- `get_language_code(language_input)`: Returns the language code for a given language input.
- `is_supported_language(language_input)`: Checks if a language is supported.
- `get_supported_languages_info()`: Returns information about supported languages.

### output_handler.py

This module handles the output of results.

#### Main Class: `OutputHandler`
- `save_results(results, language)`: Saves the calculation results to a CSV file.