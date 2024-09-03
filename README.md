# Jiwar: A Database and Calculator for Orthographic and Phonological Neighborhood Metrics for 55 Languages


## Overview

Jiwar is an open-source Python-based computational tool designed to analyze orthographic/phonological neighbors in 55 languages. It automattically measures orthographic, phonological, and phonographic metrics using a user-friendly Python CLI tool.


## How to use the tool

- Prepare Your Input File: Provide a CSV or Excel file containing at least one column titled "word" with a list of words in any of the supported languages.

- Run the Tool: Use the jiwar.py CLI tool to compute and return the desired metrics, including orthographic, phonological, and phonographic measures.

## Jiwar Measures

### Orthographic

| **Measure**                       | **Definition**                                                                                                 |
|----------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Neighbourhood Density**         | Generates the number and forms of orthographic neighbors of the target word based on  single letter substitution, addition, and deletion. |
| **Neighbourhood Frequency**       | Generates the mean word frequency and standard deviation of the target word’s orthographic neighbors based on single letter substitution, addition, and deletion. |
| **Orthographic Levenshtein Distance-20** | Generates the mean Levenshtein edit distance and standard deviation of the target word’s 20 closest orthographic neighbors based on single letter substitution, addition, or deletion. |

### Phonological

| **Measure**                       | **Definition**                                                                                                 |
|----------------------------------|----------------------------------------------------------------------------------------------------------------|
| **IPA Transcription**                | Automatically generates IPA for 51 languages using the Python library "phonemizer" with "espeak" as the backend. |
| **Neighbourhood Density**         | Generates the number and forms of phonological neighbors of the target word based on single phoneme substitution, addition, and deletion. |
| **Neighbourhood Frequency**       | Generates the mean word frequency and standard deviation of the target word’s phonological neighbors based on single phoneme substitution, addition, and deletion. |
| **Phonological Levenshtein Distance-20** | Generates the mean Levenshtein edit distance and standard deviation of the target word’s 20 closest phonological neighbors based on single phoneme substitution, addition, or deletion. |
| **Clustering Coefficient (C coefficient)** | Generates the proportion of phonological neighbors of a target word that are also phonological neighbors of each other, based on single phoneme substitution, addition, or deletion. |

### Phonographic

| **Measure**                       | **Definition**                                                                                                 |
|----------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Neighbourhood Density**         | Generates the number and forms of phonographic neighbors of the target word based on single letter and phoneme substitution, addition, and deletion. |
| **Neighbourhood Frequency**       | Generates the mean word frequency and standard deviation of the target word’s phonographic neighbors based on single letter and phoneme substitution, addition, and deletion. |
| **Phonographic Levenshtein Distance-20** | Generates the mean Levenshtein edit distance and standard deviation of the target word’s 20 closest phonographic neighbors based on single letter and phoneme substitution, addition, and deletion. |
| **Clustering Coefficient (C coefficient)** | Generates the proportion of phonographic neighbors of a target word that are also phonographic neighbors of each other, based on single letter and phoneme substitution, addition, or deletion. |

## Jiwar Supported Languages


| Code    | Language                              |
|---------|---------------------------------------|
| af      | Afrikaans                             |
| ar      | Arabic (non-diacriticized words)       |
| ar-tashkeel | Arabic (diacriticized words)       |
| bg      | Bulgarian                             |
| bn      | Bengali                               |
| br      | Breton                                |
| bs      | Bosnian                               |
| ca      | Catalan                               |
| cs      | Czech                                 |
| da      | Danish                                |
| de      | German                                |
| el      | Greek                                 |
| en-gb   | English (GB)                          |
| en-us   | English (US)                          |
| eo      | Esperanto                             |
| es      | Spanish                               |
| et      | Estonian                              |
| eu      | Basque                                |
| fa      | Persian (Farsi)                       |
| fi      | Finnish                               |
| fr      | French                                |
| gl      | Galician                              |
| he      | Hebrew                                |
| hi      | Hindi                                 |
| hr      | Croatian                              |
| hu      | Hungarian                             |
| hy      | Armenian                              |
| id      | Indonesian                            |
| is      | Icelandic                             |
| it      | Italian                               |
| ka      | Georgian                              |
| kk      | Kazakh                                |
| ko      | Korean                                |
| lt      | Lithuanian                            |
| lv      | Latvian                               |
| mk      | Macedonian                            |
| ml      | Malayalam                             |
| ms      | Malay                                 |
| nl      | Dutch                                 |
| no      | Norwegian                             |
| pl      | Polish                                |
| pt      | Portuguese                            |
| ro      | Romanian                              |
| ru      | Russian                               |
| si      | Sinhala                               |
| sk      | Slovak                                |
| sl      | Slovenian                             |
| sq      | Albanian                              |
| sr      | Serbian                               |
| sv      | Swedish                               |
| ta      | Tamil                                 |
| te      | Telugu                                |
| tl      | Tagalog (Filipino)                    |
| tr      | Turkish                               |
| uk      | Ukrainian                             |
| ur      | Urdu                                  |
| vi      | Vietnamese                            |


## Jiwar Installation

1. Clone the repository:

```bash
   git clone https://github.com/AlaaAlzahrani/jiwar.git
   cd jiwar
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install additional dependencies: 

Ensure that you have the "espeak" backend installed, which is required for the phonemizer library. Follow the instructions provided in the [Phonemizer documentation](https://bootphon.github.io/phonemizer/install.html) to install it properly.


## Examples

### Calculate All Available Measures

To calculate all available measures (orthographic, phonological, and phonographic) for a specific input file and language, use:

```bash
python jiwar.py input_file.csv en-us --all
```

### Calculate Only Orthographic Measures
To calculate only orthographic measures for a specific input file and language, use:

```bash
python jiwar.py input_file.csv en-us --orth
```


### Calculate Only Phonological Measures

To calculate only phonological measures for a specific input file and language, use:

```bash
python jiwar.py input_file.csv en-us --phon
```

### Calculate Only Phonographic Measures

To calculate only phonographic measures for a specific input file and language, use:

```bash
python jiwar.py input_file.csv en-us --pg
```

### Generate IPA Transcriptions

To generate IPA transcriptions for a specific input file and language, use:

```bash
python jiwar.py input_file.csv en-us --generate_ipa
```

###  Use a Custom Corpus File

To use a custom corpus file located in data/corpus/user_loaded/, specify the corpus file and calculate all measures:

```bash
python jiwar.py input_file.csv en-us --corpus_file custom_corpus.csv --all
```

### Help Messages

To display detailed help messages, use:

```bash
python jiwar.py --help_all
```

## License

This project is licensed under the MIT License. See the [LICENSE file](https://github.com/AlaaAlzahrani/jiwar/blob/main/LICENSE) for details.

## Citation

If you use Jiwar in your research, please cite it as follows:

```bibtex
@preprint{Alzahrani:2024:jiwar,
    title = "{Jiwar: A Database and Calculator for Orthographic and Phonological Neighborhood Metrics for 55 Languages}",
    author = {Alaa Alzahrani},
    year = "2024",
    note = "Preprint"
}
```