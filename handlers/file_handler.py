import re
import unicodedata 
import polars as pl
from pathlib import Path

def strip_white_spaces(s):
    """Strip leading and trailing whitespace and replace multiple spaces with a single space."""
    return ' '.join(s.split())

class FileReader:
    def __init__(self, max_input=100000):
        self.max_input = max_input
        self.input_data = None
        self.base_dir = Path(__file__).parent.parent.resolve()
        self.input_dir = self.base_dir / "data" / "input"
        self.output_dir = self.base_dir / "data" / "processed"

    def read_input_file(self, filename):
        file_path = self.get_file_path(filename)
        if not file_path:
            return None
                
        raw_data = self._read_file_as_text(file_path)
        cleaned_data = self._clean_white_spaces(raw_data)
        self.input_data = self._convert_to_polars(cleaned_data)
        self._clean_input()
        self._save_as_tsv(self.input_data, self.output_dir / f"{file_path.stem}_processed.tsv")
        return self.input_data

    def get_file_path(self, filename):
        if Path(filename).is_absolute():
            return Path(filename) if Path(filename).exists() else None
        
        cwd_path = Path.cwd() / filename
        if cwd_path.exists():
            return cwd_path
        
        input_path = self.input_dir / filename
        if input_path.exists():
            return input_path
        
        return None

    def _read_file_as_text(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as file:
                return file.read()
        except UnicodeDecodeError:
            for encoding in ['iso-8859-1', 'cp1252']:
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        return file.read()
                except UnicodeDecodeError:
                    continue
            raise IOError(f"Unable to determine the correct encoding for file {file_path}")
        except Exception as e:
            raise IOError(f"Error reading file {file_path}: {str(e)}")
    
    def _clean_white_spaces(self, data):
        return '\n'.join(strip_white_spaces(line) for line in data.split('\n') if line.strip())

    def _convert_to_polars(self, raw_data):
        try:
            df = pl.read_csv(io.StringIO(raw_data))
            return df
        except Exception as e:
            print(f"Error converting to Polars DataFrame: {str(e)}")
            raise ValueError("Could not parse the input file. Please check your file format.")
        
    def _clean_input(self):
        if len(self.input_data) == 0:
            raise ValueError("The input file contains no data.")

        clean_col_names = [
            re.sub(r'[^\w\s]', '', col).strip().replace(' ', '_').lower()
            for col in self.input_data.columns
        ]
        self.input_data = self.input_data.rename(dict(zip(self.input_data.columns, clean_col_names)))

        if 'word' not in self.input_data.columns:
            raise ValueError("The input file must contain a 'word' column.")

        initial_row_count = len(self.input_data)
        self.input_data = self.input_data.filter(pl.col('word').is_not_null() & (pl.col('word') != ""))
        rows_removed = initial_row_count - len(self.input_data)

        if len(self.input_data) == 0:
            raise ValueError("All rows were removed during cleaning. Please check your input file.")

        print(f"Cleaned input data. Removed {rows_removed} rows with empty words.")

    def _save_as_tsv(self, dataframe, output_path):
        dataframe.write_csv(output_path, separator='\t')

    def get_words(self, col):
        if self.input_data is None:
            return []
        words = (
            self.input_data
            .select(pl.col(col))
            .filter(pl.col(col) != "")
            .limit(self.max_input)
            .to_series()
            .to_list()
        )
        return words

    def get_orth_words(self):
        return [word.lower() for word in self.get_words(col='word')]

    def get_phon_words(self, input_is_phon_only=False):
        col = 'word' if input_is_phon_only else 'IPA'
        return self.get_words(col=col)

    def get_pg_words(self):
        orth_words = self.get_orth_words()
        phon_words = self.get_phon_words()
        return list(zip(orth_words, phon_words)) if orth_words and phon_words else []

    @staticmethod
    def _remove_accents(input_str):
        if input_str is None:
            return input_str
        if not isinstance(input_str, str):
            return str(input_str)
        nfkd_form = unicodedata.normalize('NFKD', str(input_str))
        return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])