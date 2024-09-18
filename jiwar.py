import polars as pl
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
from calculator import utils
from handlers.file_handler import FileReader
from handlers.corpus_handler import CorpusHandler
from handlers.output_handler import OutputHandler
from calculator import IPA_generator, orthographic, phonological, phonographic
from handlers.language_mapping import get_language_code, is_supported_language, get_supported_languages_info

def process_chunk(args):
    chunk, corpus_data, selected_measures, frequency_cols, include_ipa = args
    results = {'word': chunk['word']}
    
    if include_ipa:
        results['IPA'] = chunk['IPA']

    # generate word length info
    if 'orth' in selected_measures or 'all' in selected_measures:
        results['num_letters'] = chunk['word'].map_elements(utils.count_letters, return_dtype=pl.UInt32)
    if include_ipa and ('phon' in selected_measures or 'all' in selected_measures):
        results['num_phonemes'] = chunk['IPA'].map_elements(utils.count_phonemes, return_dtype=pl.UInt32)

    # generate main neighborhood measures
    for measure in selected_measures:
        if measure == 'orth_N':
            N, neighbors = orthographic.calculate_N(chunk['word'], corpus_data['word'])
            results['orth_N'] = N
            results['orth_N_nbrs'] = neighbors
        elif measure == 'orth_density':
            density, neighbors = orthographic.calculate_density(chunk['word'], corpus_data['word'])
            results['orth_density'] = density
            results['orth_density_nbrs'] = neighbors
        elif measure == 'OLD20':
            results['OLD20'] = orthographic.calculate_old20(chunk['word'], corpus_data['word'])
        elif measure == 'orth_C':
            results['orth_C'] = orthographic.calculate_clustering_coefficient(chunk['word'], corpus_data['word'])
        elif measure == 'phon_N' and include_ipa:
            N, neighbors = phonological.calculate_N(chunk['IPA'], corpus_data['IPA'])
            results['phon_N'] = N
            results['phon_N_nbrs'] = neighbors
        elif measure == 'phon_density' and include_ipa:
            density, neighbors = phonological.calculate_density(chunk['IPA'], corpus_data['IPA'])
            results['phon_density'] = density
            results['phon_density_nbrs'] = neighbors
        elif measure == 'PLD20' and include_ipa:
            results['PLD20'] = phonological.calculate_pld20(chunk['IPA'], corpus_data['IPA'])
        elif measure == 'phon_C' and include_ipa:
            results['phon_C'] = phonological.calculate_clustering_coefficient(chunk['IPA'], corpus_data['IPA'])
        elif measure == 'pg_N' and include_ipa:
            N, neighbors = phonographic.calculate_N(chunk['word'], chunk['IPA'], corpus_data['word'], corpus_data['IPA'])
            results['pg_N'] = N
            results['pg_N_nbrs'] = neighbors
        elif measure == 'pg_density' and include_ipa:
            density, neighbors = phonographic.calculate_density(chunk['word'], chunk['IPA'], corpus_data['word'], corpus_data['IPA'])
            results['pg_density'] = density
            results['pg_density_nbrs'] = neighbors
        elif measure == 'PGLD20' and include_ipa:
            results['PGLD20'] = phonographic.calculate_pgld20(chunk['word'], chunk['IPA'], corpus_data['word'], corpus_data['IPA'])
        elif measure == 'pg_C' and include_ipa:
            results['pg_C'] = phonographic.calculate_clustering_coefficient(chunk['word'], chunk['IPA'], corpus_data['word'], corpus_data['IPA'])


    # generate frequency info
    for freq_col in frequency_cols:
        if 'orth_nbr_freq' in selected_measures:
            mean, std, mean_higher, mean_lower = orthographic.calculate_neighborhood_frequency(chunk['word'], corpus_data['word'], corpus_data[freq_col])
            if freq_col == 'freq_per_m':
                results['orth_nbr_fpm_m'] = mean
                results['orth_nbr_fpm_SD'] = std
                results['orth_nbr_fpm_higher_m'] = mean_higher
                results['orth_nbr_fpm_lower_m'] = mean_lower
            elif freq_col == 'zipf':
                results['orth_nbr_zipf_m'] = mean
                results['orth_nbr_zipf_SD'] = std
                results['orth_nbr_zipf_higher_m'] = mean_higher
                results['orth_nbr_zipf_lower_m'] = mean_lower
            else:
                results[f'orth_nbr_{freq_col}'] = mean
                results[f'orth_nbr_{freq_col}_SD'] = std
                results[f'orth_nbr_{freq_col}_higher'] = mean_higher
                results[f'orth_nbr_{freq_col}_lower'] = mean_lower
        if 'phon_nbr_freq' in selected_measures and include_ipa:
            mean, std, mean_higher, mean_lower = phonological.calculate_neighborhood_frequency(chunk['IPA'], corpus_data['IPA'], corpus_data[freq_col])
            if freq_col == 'freq_per_m':
                results['phon_nbr_fpm_m'] = mean
                results['phon_nbr_fpm_SD'] = std
                results['phon_nbr_fpm_higher_m'] = mean_higher
                results['phon_nbr_fpm_lower_m'] = mean_lower
            elif freq_col == 'zipf':
                results['phon_nbr_zipf_m'] = mean
                results['phon_nbr_zipf_SD'] = std
                results['phon_nbr_zipf_higher_m'] = mean_higher
                results['phon_nbr_zipf_lower_m'] = mean_lower
            else:
                results[f'phon_nbr_{freq_col}'] = mean
                results[f'phon_nbr_{freq_col}_SD'] = std
                results[f'phon_nbr_{freq_col}_higher'] = mean_higher
                results[f'phon_nbr_{freq_col}_lower'] = mean_lower
        if 'pg_nbr_freq' in selected_measures and include_ipa:
            mean, std, mean_higher, mean_lower = phonographic.calculate_neighborhood_frequency(chunk['word'], chunk['IPA'], corpus_data['word'], corpus_data['IPA'], corpus_data[freq_col])
            if freq_col == 'freq_per_m':
                results['pg_nbr_fpm_m'] = mean
                results['pg_nbr_fpm_SD'] = std
                results['pg_nbr_fpm_higher_m'] = mean_higher
                results['pg_nbr_fpm_lower_m'] = mean_lower
            elif freq_col == 'zipf':
                results['pg_nbr_zipf_m'] = mean
                results['pg_nbr_zipf_SD'] = std
                results['pg_nbr_zipf_higher_m'] = mean_higher
                results['pg_nbr_zipf_lower_m'] = mean_lower
            else:
                results[f'pg_nbr_{freq_col}'] = mean
                results[f'pg_nbr_{freq_col}_SD'] = std
                results[f'pg_nbr_{freq_col}_higher'] = mean_higher
                results[f'pg_nbr_{freq_col}_lower'] = mean_lower
    
    return pl.DataFrame(results)


def main():

    print("Welcome to Jiwar!")
    print()

    corpus_handler = CorpusHandler()

    while True:
        language_input = input("Enter the language for analysis: ")
        language_code = get_language_code(language_input)
        if language_code:
            break
        else:
            print("Unsupported language. Please try again.")
            print(get_supported_languages_info())

    if corpus_handler.has_built_in_corpus(language_code):
        use_built_in = input(f"A built-in corpus is available for {language_input}. Do you want to use it? (y/n): ").lower() == 'y'
    else:
        use_built_in = False
        print(f"\nATTENTION: No built-in corpus is available for {language_input} in Jiwar.")
        print("You must prepare a custom corpus for this language.")
        print("\nCustom Corpus Requirements:")
        print("1. The corpus should be in CSV or Excel format.")
        print("2. It must contain at least a 'word' column with the words in your language.")
        print("3. For frequency-based measures, include columns with names containing 'frequency' or 'freq'.")
        print("4. Place your corpus file in the 'user_loaded' directory within the Jiwar data folder, or provide the full path.")
        print("\nPlease prepare your custom corpus now if you haven't already.")
        input("Press Enter when you're ready to proceed...")

    if not use_built_in:
        while True:
            corpus_filename = input("Enter the filename or full path of your custom corpus, or type 'exit' to quit: ")
            
            if corpus_filename.lower() == 'exit':
                print("Exiting Jiwar.")
                return  
            
            try:
                corpus_data = corpus_handler.load_corpus(language_input, use_user_corpus=True, corpus_filename=corpus_filename)
                print("Corpus loaded successfully.")
                print(f"Corpus info: {corpus_handler.corpus_info()}")
                print(f"Frequency columns found: {corpus_handler.get_frequency_columns()}")
                break
            except FileNotFoundError as e:
                print(e)
                print("Please try again with a valid filename or full path, or type 'exit' to quit.")
            except ValueError as e:
                print(f"Error loading corpus: {e}")
                print("Please ensure your corpus meets the minimum requirements and try again, or type 'exit' to quit.")


    while True:
            input_file = input("Enter the path to your input file:\n"
                            "- Enter just the filename to look in the current directory or Jiwar's input directory\n"
                            "- Or enter the full path to the file\n"
                            "Your input: ")
            if input_file.lower() == 'exit':
                print("Exiting Jiwar.")
                return
            try:
                file_reader = FileReader()
                input_data = file_reader.read_input_file(input_file)
                print(f"Input data columns: {input_data.columns}")
                break
            except FileNotFoundError as e:
                print(f"Error: {e}")
                print("Jiwar looked for the file in the following locations:")
                print(f"1. Current working directory: {Path.cwd()}")
                print(f"2. Jiwar's input directory: {file_reader.input_dir}")
                print("Please make sure you've entered the correct filename or path.")
                print("You can type 'exit' to quit the program.")
            except Exception as e:
                print(f"Error reading input file: {e}")
                print("Please try again or type 'exit' to quit.")
            
            if input_file.lower() == 'exit':
                print("Exiting Jiwar.")
                return

    while True:
        measure_input = input("Enter the type of measures to calculate (all, orth, phon, pg, or a combination separated by commas): ").lower()
        measures = [m.strip() for m in measure_input.split(',')]
        valid_measures = {'all', 'orth', 'phon', 'pg'}
        if set(measures).issubset(valid_measures):
            break
        else:
            print("Invalid input. Please enter 'all', 'orth', 'phon', 'pg', or a combination of these.")

    selected_measures = []
    if 'all' in measures or 'orth' in measures:
        selected_measures.extend(['orth', 'orth_N', 'orth_density', 'OLD20', 'orth_C', 'orth_nbr_freq'])
    if 'all' in measures or 'phon' in measures:
        selected_measures.extend(['phon', 'phon_N', 'phon_density', 'PLD20', 'phon_C', 'phon_nbr_freq'])
    if 'all' in measures or 'pg' in measures:
        selected_measures.extend(['pg', 'pg_N', 'pg_density', 'PGLD20', 'pg_C', 'pg_nbr_freq'])


    include_ipa = 'all' in measures or 'phon' in measures or 'pg' in measures
    if include_ipa and 'IPA' in input_data.columns:
        print("IPA column found in input data. Skipping IPA generation.")
    elif include_ipa:
        print("Generating IPA transcriptions for input data...")
        input_data = input_data.with_columns(pl.Series('IPA', IPA_generator.generate_ipa(input_data['word'].to_list(), language_code)))
    
    if include_ipa and 'IPA' not in corpus_data.columns:
        print("Generating IPA transcriptions for corpus data...")
        corpus_data = corpus_data.with_columns(pl.Series('IPA', IPA_generator.generate_ipa(corpus_data['word'].to_list(), language_code)))

    chunk_size = 1000
    n_jobs = cpu_count()
    chunks = [input_data[i:i+chunk_size] for i in range(0, len(input_data), chunk_size)]

    with Pool(n_jobs) as pool:
        results = list(tqdm(
            pool.imap(process_chunk, [(chunk, corpus_data, selected_measures, corpus_handler.get_frequency_columns(), include_ipa) for chunk in chunks]),
            total=len(chunks),
            desc="Processing chunks"
        ))

    final_results = pl.concat(results)


    output_handler = OutputHandler()
    output_file = output_handler.save_results(final_results, language_code)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()