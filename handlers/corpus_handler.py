import polars as pl
from pathlib import Path
from .file_handler import FileReader
from .language_mapping import get_language_code, LANGUAGE_MAPPING
import openpyxl

class CorpusHandler:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.subtitle_corpus_dir = self.base_dir / "data" / "corpus" / "subtitles"
        self.user_corpus_dir = self.base_dir / "data" / "corpus" / "user_loaded"
        self.corpus_data = None
        self.current_language = None
        self.frequency_columns = None
        self.file_reader = FileReader()

    def load_corpus(self, language_input, use_user_corpus=False, corpus_filename=None):
        language_code = get_language_code(language_input)


        if language_code is None:
            raise ValueError(f"Unsupported language: {language_input}")

        self.current_language = LANGUAGE_MAPPING[language_code]

        if language_code == 'ar':
            sample_words = self.file_reader.get_orth_words()[:10]  
            has_diacritics = any('\u064b' <= c <= '\u065f' for word in sample_words for c in word)
            if has_diacritics:
                language_code = 'ar-tashkeel'
                print("Detected Arabic words with diacritics. Using the corpus with diacritics.")
            else:
                print("Detected Arabic words without diacritics. Using the corpus without diacritics.")

        if use_user_corpus:
            if corpus_filename:
                user_corpus_file = self.user_corpus_dir / corpus_filename
            else:
                user_corpus_file = self.user_corpus_dir / f"{language_code}_user_corpus.csv"
            
            if user_corpus_file.exists():
                file_extension = user_corpus_file.suffix.lower()
                if file_extension == '.csv':
                    self.corpus_data = self._load_csv(user_corpus_file)
                elif file_extension == '.xlsx':
                    self.corpus_data = self._load_excel(user_corpus_file)
                else:
                    raise ValueError(f"Unsupported file format: {file_extension}")
                self._select_frequency_columns(use_user_corpus=True)
            else:
                raise FileNotFoundError(
                    f"User corpus file not found: {user_corpus_file}\n"
                    f"Please ensure your corpus file is located in the following directory:\n"
                    f"{self.user_corpus_dir}"
                )
        else:
            self.corpus_data = self._load_subtitle_corpus(language_code)
            self._select_frequency_columns(use_user_corpus=False)
            
        # some language corpora have "null" IPA transcriptions
        if 'IPA' in self.corpus_data.columns:
            original_size = len(self.corpus_data)
            self.corpus_data = self.corpus_data.filter(pl.col('IPA').is_not_null())
            filtered_size = len(self.corpus_data)
        
        self._validate_corpus()
        return self.corpus_data

    def _load_subtitle_corpus(self, language_code):
        corpus_file = self.subtitle_corpus_dir / f"{language_code}_subs.tsv"
        if corpus_file.exists():
            return self._load_csv(corpus_file, separator='\t')
        else:
            raise FileNotFoundError(f"Subtitle corpus file not found for language code: {language_code}")

    def _load_csv(self, file_path, separator=','):
        encodings = ['utf-8', 'utf-8-sig', 'iso-8859-1', 'cp1252']
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    sample = f.read(1024)
                    f.seek(0)                    
                    return pl.read_csv(f, separator=separator)
            except UnicodeDecodeError:
                continue
        
        raise IOError(f"Unable to determine the correct encoding for file {file_path}")

    def _load_excel(self, file_path):
        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            data = list(sheet.values)
            columns = data[0]
            rows = data[1:]
            
            data_dict = {col: [row[i] for row in rows] for i, col in enumerate(columns)}        
            df = pl.DataFrame(data_dict)
            return df
        except Exception as e:
            raise IOError(f"Error reading Excel file {file_path}: {str(e)}")

    def _select_frequency_columns(self, use_user_corpus):
        available_columns = self.corpus_data.columns
        if use_user_corpus:
            frequency_columns = [col for col in available_columns if col.startswith('frequency_')]
            if not frequency_columns:
                raise ValueError("User corpus does not contain any columns starting with 'frequency_'.")
            self.frequency_columns = frequency_columns[:2]  
        else:
            if 'relative_frequency' in available_columns and 'zipf' in available_columns:
                self.frequency_columns = ['relative_frequency', 'zipf']
            else:
                raise ValueError("Subtitle corpus is missing required frequency columns.")

    def _validate_corpus(self):
        if 'word' not in self.corpus_data.columns:
            raise ValueError("Corpus is missing the required 'word' column.")

        if not self.frequency_columns:
            raise ValueError("No valid frequency columns found in the corpus.")

        for freq_col in self.frequency_columns:
            if freq_col not in self.corpus_data.columns:
                raise ValueError(f"Corpus is missing the required frequency column: {freq_col}")
            
            self.corpus_data = self.corpus_data.with_columns(
                pl.col(freq_col).cast(pl.Float64, strict=False)
            )
            if self.corpus_data.filter(pl.col(freq_col).is_null()).height > 0:
                raise ValueError(f"The '{freq_col}' column contains non-numeric values.")
        
        if 'IPA' in self.corpus_data.columns:
            self.corpus_data = self.corpus_data.with_columns(
                pl.col('IPA').map_elements(FileReader._remove_accents, return_dtype=pl.Utf8)
            )

    def get_word_frequencies(self):
        if self.corpus_data is None or self.corpus_data.is_empty():
            raise ValueError("Corpus not loaded or empty. Call load_corpus() first.")
        return self.corpus_data.groupby('word').count().sort('count', descending=True).to_dict(as_series=False)

    def corpus_info(self):
        if self.corpus_data is None or self.corpus_data.is_empty():
            return "No corpus loaded or corpus is empty."
        return f"Corpus loaded for {self.current_language}: {self.corpus_data.height} entries, {self.corpus_data['word'].n_unique()} unique words"

    def get_frequency_columns(self):
        if self.frequency_columns is None:
            raise ValueError("Frequency columns not set. Ensure corpus is loaded and validated.")
        return self.frequency_columns