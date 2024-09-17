# Creating and Using Custom Corpora in Jiwar

For languages without built-in support or if you want to use your own corpus, you can create a custom corpus file for use with Jiwar.

## Custom Corpus Requirements

1. File Format: CSV or Excel (.xlsx)
2. Minimum Required Columns:
   - `word`: The word in the target language
3. Optional Columns for Frequency Information:
   - `frequency_*`: Columns starting with "frequency_" will be used for neighborhood frequency calculations

## Steps to Create a Custom Corpus

1. Prepare your word list in the target language.
2. Create a CSV or Excel file with at least a 'word' column.
3. If available, add frequency information in columns starting with 'frequency_'.
4. Save the file in the `data/corpus/user_loaded/` directory of your Jiwar installation.

Example custom corpus structure:

```
word,frequency_count,frequency_per_million
apple,1000,50.5
banana,800,40.2
cherry,600,30.1
...
```

## Using a Custom Corpus with Jiwar

1. Place your custom corpus file in the `data/corpus/user_loaded/` directory.
2. Run Jiwar as usual: `python jiwar.py`
3. When prompted, enter the name of your custom corpus file.
4. Proceed with your analysis as normal.

Note: If a built-in corpus is available for your chosen language, Jiwar will ask if you want to use it or your custom corpus.

For more detailed usage instructions, please refer to the [USAGE.md file]((https://github.com/AlaaAlzahrani/Jiwar/blob/master/docs/USAGE.md)).