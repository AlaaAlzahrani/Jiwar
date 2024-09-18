Creating and Using Custom Corpora
=================================

For languages without built-in support or if you want to use your own corpus, you can create a custom corpus file for use with Jiwar.

Custom Corpus Requirements
--------------------------

1. **File Format**: CSV or Excel (.xlsx)
2. **Minimum Required Columns**:
   - ``word``: The word in the target language
3. **Optional Columns for Frequency Information**:
   - ``frequency_*``: Columns starting with "frequency_" will be used for neighborhood frequency calculations

Steps to Create a Custom Corpus
-------------------------------

1. Prepare your word list in the target language.
2. Create a CSV or Excel file with at least a 'word' column.
3. If available, add frequency information in columns starting with 'frequency_'.
4. Save the file in the ``data/corpus/user_loaded/`` directory of your Jiwar installation.

Example Custom Corpus Structure
-------------------------------

.. code-block:: none

   word,frequency_count,frequency_per_million
   apple,1000,50.5
   banana,800,40.2
   cherry,600,30.1
   ...

Using a Custom Corpus with Jiwar
--------------------------------

1. Place your custom corpus file in the ``data/corpus/user_loaded/`` directory.
2. Run Jiwar as usual: ``python jiwar.py``
3. When prompted, enter the name of your custom corpus file.
4. Proceed with your analysis as normal.

Note: If a built-in corpus is available for your chosen language, Jiwar will ask if you want to use it or your custom corpus.

Tips for Custom Corpora
-----------------------

- Ensure your corpus is representative of the language or specific domain you're studying.
- The larger the corpus, the more accurate the neighborhood measures will be.
- If you're using a custom corpus for a language with a built-in corpus, consider comparing results to validate your custom corpus.
- For languages without built-in IPA support, you may need to provide IPA transcriptions in your custom corpus for phonological and phonographic measures.