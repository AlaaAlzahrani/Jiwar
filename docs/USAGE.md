# Using Jiwar

This guide provides detailed instructions on how to use Jiwar for various scenarios.

## Basic Usage

1. Prepare your input file (csv, xlsx, txt, tsv) with at least a 'word' column.
2. Open a terminal and navigate to the Jiwar directory.
3. Run the command: `python jiwar.py`
4. Follow the prompts to select your language, input file, and desired measures.

## Example Scenarios

### Scenario 1: Calculating All Measures for English Words

1. Prepare an input file named `english_words.csv` with a 'word' column.
2. Run: `python jiwar.py`
3. When prompted, enter:
   - Language: `English` or `en-us`
   - Input file: `english_words.csv`
   - Measures: `all`

### Scenario 2: Calculating Only Orthographic Measures for Spanish Words

1. Prepare an input file named `spanish_words.csv` with a 'word' column.
2. Run: `python jiwar.py`
3. When prompted, enter:
   - Language: `Spanish` or `es`
   - Input file: `spanish_words.csv`
   - Measures: `orth`

### Scenario 3: Using a Custom Corpus for Hindi

1. Prepare your custom Hindi corpus and save it as `hindi_corpus.csv` in the `data/corpus/user_loaded/` directory. The [custum corpus](https://github.com/AlaaAlzahrani/Jiwar/blob/master/docs/CUSTOM_CORPUS.md) must include a 'word' column.
2. Prepare your input file named `hindi_words.csv` with a 'word' column.
3. Run: `python jiwar.py`
4. When prompted, enter:
   - Language: `Hindi` or `hi`
   - Use built-in corpus: `n` (since Hindi doesn't have a built-in corpus)
   - Custom corpus filename: `hindi_corpus.csv`
   - Input file: `hindi_words.csv`
   - Measures: Choose your desired measures (e.g., `all`, `orth,phon`, etc.)

## Tips

- If you're unsure about the supported languages or measures, type `help` at any prompt for more information.
- To exit the program at any time, type `exit` at any prompt.
- For languages without built-in IPA support, consider adding an 'IPA' column to your input file for phonological and phonographic measures.


## Note for Google Colab Users

When using Jiwar in Google Colab, you might encounter package version conflicts. If this happens, try the following steps:

1. Install pip-ignore-conflicts:
   ```
   !pip install pip-ignore-conflicts
   ```

2. Install Jiwar requirements ignoring conflicts:
   ```
   !pip install --ignore-conflicts -r requirements.txt
   ```

3. If issues persist, manually install compatible versions:
   ```
   !pip install pandas==2.0.3 numpy==1.23.5 pyarrow==14.0.1
   ```

>Note: Remember to restart your runtime after installing packages.

## More information

For more information on specific measures, refer to the [MEASURES.md file](https://github.com/AlaaAlzahrani/Jiwar/blob/master/docs/MEASURES.md). For language support details, see the [LANGUAGES.md file](https://github.com/AlaaAlzahrani/Jiwar/blob/master/docs/LANGUAGES.md).