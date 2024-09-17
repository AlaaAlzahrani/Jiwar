import polars as pl
from pathlib import Path
import io
import re
import unicodedata 

def strip_white_spaces(s):
    """Strip leading and trailing whitespace and replace multiple spaces with a single space."""
    return ' '.join(s.split())

class FileReader:
    def __init__(self, max_input=100000):
        self.max_input = max_input
        self.input_data = None
        self.base_dir = Path(__file__).parent.parent
        self.input_dir = self.base_dir / "data" / "input"
        self.output_dir = self.base_dir / "data" / "processed"

    def read_input_file(self, filename):
        file_path = self.input_dir / filename
        raw_data = self._read_file_as_text(file_path)
        cleaned_data = self._clean_white_spaces(raw_data)
        self.input_data = self._convert_to_polars(cleaned_data)
        self._clean_input()
        self._save_as_tsv(self.input_data, self.output_dir / f"{Path(filename).stem}_processed.tsv")
        return self.input_data

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
            print(f"DataFrame info: {df.schema}")
            return df
        except Exception as e:
            print(f"Error converting to Polars DataFrame: {str(e)}")
            raise ValueError("Could not parse the input file. Please check your file format.")

    def _clean_input(self):
        if len(self.input_data) == 0:
            raise ValueError("The input file contains no data.")

        # Clean column names
        clean_col_names = [
            re.sub(r'[^\w\s]', '', col).strip().replace(' ', '_').lower()
            for col in self.input_data.columns
        ]
        self.input_data = self.input_data.rename(dict(zip(self.input_data.columns, clean_col_names)))

        # Ensure 'word' column exists
        if 'word' not in self.input_data.columns:
            raise ValueError("The input file must contain a 'word' column.")

        # Remove rows with empty words
        initial_row_count = len(self.input_data)
        self.input_data = self.input_data.filter(pl.col('word').is_not_null() & (pl.col('word') != ""))
        rows_removed = initial_row_count - len(self.input_data)

        if len(self.input_data) == 0:
            raise ValueError("All rows were removed during cleaning. Please check your input file.")

        print(f"Cleaned input data. Removed {rows_removed} rows with empty words.")
        print(f"Final row count: {len(self.input_data)}")


    def _save_as_tsv(self, dataframe, output_path):
        dataframe.write_csv(output_path, separator='\t')