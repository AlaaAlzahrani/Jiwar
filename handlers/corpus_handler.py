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
        
    def has_built_in_corpus(self, language_code):
        built_in_languages = [
            "af", "ar", "bg", "br", "bs", "ca", "cs", "de", "el",
            "en-gb", "en-us", "eo", "es", "et", "eu", "fa", "fi", "fr", "gl",
            "hr", "hu", "hy", "id", "it", "kk", "ko", "lt", "lv", "mk", "ms",
            "nl", "no", "pl", "pt", "ro", "ru", "sk", "sq", "sr", "sv", "tl",
            "tr", "uk", "ur"
        ]
        return language_code in built_in_languages

    def load_corpus(self, language_input, use_user_corpus=False, corpus_filename=None):
        language_code = get_language_code(language_input)

        if language_code is None:
            raise ValueError(f"Unsupported language: {language_input}")

        self.current_language = LANGUAGE_MAPPING[language_code]

        if language_code == 'ar':
            sample_words = self.file_reader.get_orth_words()[:10]  
            has_diacritics = any('\u064b' <= c <= '\u065f' for word in sample_words for c in word)
            if not has_diacritics:
                print("Detected Arabic words without diacritics. We recommend using diacritics for more accuarte results.")

        if use_user_corpus or not self.has_built_in_corpus(language_code):
            if corpus_filename:
                user_corpus_file = Path(corpus_filename)
                if not user_corpus_file.is_absolute():
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
                    f"{self.user_corpus_dir}\n"
                    f"Or provide the full path to your corpus file."
                )
        else:
            self.corpus_data = self._load_subtitle_corpus(language_code)
            self._select_frequency_columns(use_user_corpus=False)
            
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
                return pl.read_csv(file_path, separator=separator, encoding=encoding)
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
            frequency_columns = [col for col in available_columns if 'frequency' in col.lower() or 'freq' in col.lower()]
            if not frequency_columns:
                print("Warning: No columns containing 'frequency' or 'freq' found in the corpus.")
                print("Available columns:", available_columns)
                print("Frequency-based measures will not be available.")
            self.frequency_columns = frequency_columns[:2] 
        else:
            if 'freq_per_m' in available_columns and 'zipf' in available_columns:
                self.frequency_columns = ['freq_per_m', 'zipf']
            else:
                print("Warning: Required frequency columns 'freq_per_m' and 'zipf' not found in subtitle corpus.")
                print("Available columns:", available_columns)
                print("Frequency-based measures will not be available.")

    def _validate_corpus(self):
        if 'word' not in self.corpus_data.columns:
            raise ValueError("The custom corpus is missing the required 'word' column. "
                             "Please ensure your corpus includes a column named 'word' containing the words in your language.")

        if not self.frequency_columns:
            print("Warning: No valid frequency columns found in the corpus. "
                  "Frequency-based measures will not be available.")
            print("To include frequency information, add columns with names containing 'frequency' or 'freq' to your corpus.")
        else:
            for freq_col in self.frequency_columns:
                if freq_col not in self.corpus_data.columns:
                    raise ValueError(f"The corpus is missing the frequency column: {freq_col}")
                
                self.corpus_data = self.corpus_data.with_columns(
                    pl.col(freq_col).cast(pl.Float64, strict=False)
                )
                if self.corpus_data.filter(pl.col(freq_col).is_null()).height > 0:
                    raise ValueError(f"The '{freq_col}' column contains non-numeric values. "
                                     "Please ensure all frequency values are numeric.")
        if 'IPA' in self.corpus_data.columns:
            self.corpus_data = self.corpus_data.with_columns(
                pl.col('IPA').map_elements(FileReader._remove_accents, return_dtype=pl.Utf8)
            )
        else:
            print("Note: The corpus does not contain an 'IPA' column. "
                  "Phonological and phonographic measures will not be available.")
            
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