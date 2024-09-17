# Jiwar: A database and calculator for word neighborhood measures across 40+ languages


## Overview

The Jiwar calulator is an open-source Python-based computational tool designed to analyze orthographic, phonological and phonographic neighbors in 40+ languages. It automattically calulates these neighborhood measures using a user-friendly Python CLI tool.


## How to use the tool

- Prepare Your Input File: Provide a CSV or Excel file containing at least one column titled "word" with a list of words in any of the supported languages.

- Run the Tool: Use the jiwar.py CLI tool to compute and return the desired metrics, including orthographic, phonological, and phonographic measures.

## Jiwar Measures

| **Category**    | **Measure**                              |
|-----------------|-----------------------------------------|
| Orthographic    | Neighbourhood Density                    |
| Orthographic    | Neighbourhood Frequency                  |
| Orthographic    | Orthographic Levenshtein Distance-20     |
| Phonological    | IPA Transcription                        |
| Phonological    | Neighbourhood Density                    |
| Phonological    | Neighbourhood Frequency                  |
| Phonological    | Phonological Levenshtein Distance-20     |
| Phonological    | Clustering Coefficient (C coefficient)    |
| Phonographic    | Neighbourhood Density                    |
| Phonographic    | Neighbourhood Frequency                  |
| Phonographic    | Phonographic Levenshtein Distance-20     |
| Phonographic    | Clustering Coefficient (C coefficient)    |

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
   git clone https://github.com/AlaaAlzahrani/Jiwar.git
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

Copyright 2024 Alaa Alzahrani

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

## Citation

If you use Jiwar in your research, please cite it as follows:

```bibtex
@preprint{Alzahrani:2024:jiwar,
    title = "{Jiwar: A Database and Calculator for Orthographic and Phonological Neighborhood Metrics for 40+ Languages}",
    author = {Alaa Alzahrani},
    year = "2024",
    note = "Preprint"
}
```