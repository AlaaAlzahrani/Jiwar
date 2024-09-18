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

   - Click [HERE](https://colab.research.google.com/drive/1f_n7uuimT8MReaOW4U4LP8dAUVtY2hAq?usp=sharing) to use an interactive Google colab notebook.
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
| N (Neighborhood Size) | Number and forms of words that differ from the target word by one letter/phoneme via substitution only |
| Density | Number and forms of words that that differ from the target word by one letter/phoneme via substitution, addition, or deletion |
| OLD20/PLD20/PGLD20 | Average Levenshtein distance of the 20 closest neighbors to the target word |
| C (Clustering Coefficient) | Measures the extent to which a given word's neighbors are also neighbors of each other |
| Neighborhood Frequency | Descriptive statistics (Mean, SD) about the frequencies of neighboring words |

## Supported Languages

- Jiwar supports 40 languages with built-in corpus, and around 90 language varieties with custom corpus.
- For languages without a built-in corpus, you'll need to provide a [custom corpus](https://jiwar.readthedocs.io/en/latest/languages/custom_corpus.html) to use Jiwar.



## Documentation 

For more detailed instructions and examples, check out our fully documented guide here:

👉 [Jiwar Documentation](https://jiwar.readthedocs.io/en/latest/index.html)


## License

Jiwar is licensed under the GNU General Public [License](LICENSE) v3.0. 

Copyright 2024 Alaa Alzahrani

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

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