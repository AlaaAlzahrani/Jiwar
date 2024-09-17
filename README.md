# Jiwar: Word Neighborhood Calculator for 40+ Languages

## Overview

Jiwar is an open-source Python tool for analyzing orthographic, phonological, and phonographic neighbors across 40+ languages. It offers a user-friendly command-line interface for calculating various neighborhood measures.

## Features

- Supports 40+ languages
- Calculates orthographic, phonological, and phonographic measures
- User-friendly command-line interface
- Supports custom corpus files

## Quick Start

1. Clone the repository:
   ```
   git clone https://github.com/AlaaAlzahrani/Jiwar.git
   cd Jiwar
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run Jiwar:
   ```
   python jiwar.py
   ```

## Supported Measures

| Measure | Description |
|---------|-------------|
| N (Neighborhood Size) | Number of words that differ by one letter/phoneme |
| Density | Number of words within a Levenshtein distance of 1 |
| OLD20/PLD20/PGLD20 | Average Levenshtein distance of the 20 closest neighbors |
| C (Clustering Coefficient) | Measures how interconnected a word's neighbors are |
| Neighborhood Frequency | Statistics about the frequencies of neighboring words |

## Language Support

- Jiwar supports [127 languages](https://github.com/AlaaAlzahrani/Jiwar/docs/LANGUAGES.md). 
- Jiwar includes built-in corpora for 40 languages. 
- For languages without a built-in corpus, you'll need to provide a [custom corpus](https://github.com/AlaaAlzahrani/Jiwar/docs/CUSTOM_CORPUS.md).


## Usage

1. Prepare your input file (CSV or Excel) with a 'word' column.
2. Run `python jiwar.py` and follow the prompts.
3. Select your desired language and measures.
4. Jiwar will process your input and save the results.

## Documentation

For more detailed instructions and examples, check the following:
- [Supported Measures](https://github.com/AlaaAlzahrani/Jiwar/docs/MEASURES.md)
- [Supported Languages](https://github.com/AlaaAlzahrani/Jiwar/docs/LANGUAGES.md)
- [Creating Custom Corpora](https://github.com/AlaaAlzahrani/Jiwar/docs/CUSTOM_CORPUS.md)
- [Detailed Usage Instructions](https://github.com/AlaaAlzahrani/Jiwar/docs/USAGE.md)


## License

Jiwar is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Citation

If you use Jiwar in your research, please cite:

```bibtex
@preprint{Alzahrani:2024:jiwar,
    title = "{Jiwar: A Database and Calculator for Orthographic and Phonological Neighborhood Measures for 40 Languages}",
    author = {Alaa Alzahrani},
    year = "2024",
    note = "Preprint"
}
```