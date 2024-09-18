<h1 align="center">Jiwar: A neighborhood calculator for 40+ languages</h1>

<p align="center">
  <a href="https://www.gnu.org/licenses/gpl-3.0">
    <img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg" alt="License: GPL v3">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252" alt="Google Colab">
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python">
</p>



## Overview

Jiwar is an open-source Python tool for generating orthographic, phonological, and phonographic measures across 40+ languages. 

## Features

- Supports 40+ languages
- Calculates orthographic, phonological, and phonographic neighborhood measures
- User-friendly command-line interface
- Includes built-in and custom corpus files


##  Get Started  

![alt text](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)

   - Click [HERE](https://colab.research.google.com/drive/1f_n7uuimT8MReaOW4U4LP8dAUVtY2hAq) to use an interactive Google colab notebook.
   - This online notebook helps users start using Jiwar without installing it on their devices. 


## Quick Start

1. Clone the repository:
   ```
   git clone https://github.com/AlaaAlzahrani/Jiwar.git
   cd Jiwar
   ```

2. Create and activate a virtual environment:

- _For Windows:_
   ```
   virtualenv -p python3 venv
   .\venv\Scripts\activate.ps1
   ```

- _For macOS and Linux:_
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Run Jiwar:
   ```
   python jiwar.py
   ```

## Usage

1. Prepare your input file (csv, xlsx, txt, tsv) with a 'word' column.
2. Run `python jiwar.py` and follow the prompts.
3. Select your desired language and measures.
4. Jiwar will process your input and save the results.


## Supported Measures

| Measure | Description |
|---------|-------------|
| N (Neighborhood Size) | Number of words that differ by one letter/phoneme via substitution |
| Density | Number of words that that differ by one letter/phoneme via substitution, addition, or deletion |
| OLD20/PLD20/PGLD20 | Average Levenshtein distance of the 20 closest neighbors |
| C (Clustering Coefficient) | Measures how interconnected a word's neighbors are |
| Neighborhood Frequency | Statistics about the frequencies of neighboring words |

## Supported Language 

- Jiwar supports 40 languages with built-in corpus, and around 90 language varieties with custom corpus.
- For languages without a built-in corpus, you'll need to provide a [custom corpus](https://github.com/AlaaAlzahrani/Jiwar/blob/master/docs/CUSTOM_CORPUS.md) to use Jiwar.




## Documentation

For more detailed instructions and examples, check the following:
- [Supported Measures](https://github.com/AlaaAlzahrani/Jiwar/blob/master/docs/MEASURES.md)
- [Supported Languages](https://github.com/AlaaAlzahrani/Jiwar/blob/master/docs/LANGUAGES.md)
- [Creating Custom Corpora](https://github.com/AlaaAlzahrani/Jiwar/blob/master/docs/CUSTOM_CORPUS.md)
- [Detailed Usage Instructions](https://github.com/AlaaAlzahrani/Jiwar/blob/master/docs/USAGE.md)


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