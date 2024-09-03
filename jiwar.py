import argparse
import polars as pl
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
from pathlib import Path
from handlers.file_handler import FileReader
from handlers.corpus_handler import CorpusHandler
from handlers.output_handler import OutputHandler
from calculator import IPA_generator, orthographic, phonological, phonographic
from handlers.language_mapping import is_supported_language, get_supported_languages_info

def process_chunk(args):
    chunk, corpus_data, selected_measures, frequency_cols, include_ipa = args
    results = {'word': chunk['word']}
    
    if include_ipa:
        results['IPA'] = chunk['IPA']
    
    for measure in selected_measures:
        if measure == 'orthographic_density':
            density, neighbors = orthographic.calculate_density(chunk['word'], corpus_data['word'])
            results['orthographic_density'] = density
            results['orthographic_neighbors'] = neighbors
        elif measure == 'OLD20':
            results['OLD20'] = orthographic.calculate_old20(chunk['word'], corpus_data['word'])
        elif measure == 'orthographic_clustering_coefficient':
            results['orthographic_clustering_coefficient'] = orthographic.calculate_clustering_coefficient(chunk['word'], corpus_data['word'])
        elif measure == 'phonological_density' and include_ipa:
            density, neighbors = phonological.calculate_density(chunk['IPA'], corpus_data['IPA'])
            results['phonological_density'] = density
            results['phonological_neighbors'] = neighbors
        elif measure == 'PLD20' and include_ipa:
            results['PLD20'] = phonological.calculate_pld20(chunk['IPA'], corpus_data['IPA'])
        elif measure == 'phonological_clustering_coefficient' and include_ipa:
            results['phonological_clustering_coefficient'] = phonological.calculate_clustering_coefficient(chunk['IPA'], corpus_data['IPA'])
        elif measure == 'phonographic_density' and include_ipa:
            density, neighbors = phonographic.calculate_density(chunk['word'], chunk['IPA'], corpus_data['word'], corpus_data['IPA'])
            results['phonographic_density'] = density
            results['phonographic_neighbors'] = neighbors
        elif measure == 'PGLD20' and include_ipa:
            results['PGLD20'] = phonographic.calculate_pgld20(chunk['word'], chunk['IPA'], corpus_data['word'], corpus_data['IPA'])
        elif measure == 'phonographic_clustering_coefficient' and include_ipa:
            results['phonographic_clustering_coefficient'] = phonographic.calculate_clustering_coefficient(chunk['word'], chunk['IPA'], corpus_data['word'], corpus_data['IPA'])
    
    for freq_col in frequency_cols:
        if 'orthographic_neighborhood_frequency' in selected_measures:
            mean, std = orthographic.calculate_neighborhood_frequency(chunk['word'], corpus_data['word'], corpus_data[freq_col])
            results[f'orthographic_neighborhood_frequency_{freq_col}'] = mean
            results[f'orthographic_neighborhood_frequency_{freq_col}_SD'] = std
        if 'phonological_neighborhood_frequency' in selected_measures and include_ipa:
            mean, std = phonological.calculate_neighborhood_frequency(chunk['IPA'], corpus_data['IPA'], corpus_data[freq_col])
            results[f'phonological_neighborhood_frequency_{freq_col}'] = mean
            results[f'phonological_neighborhood_frequency_{freq_col}_SD'] = std
        if 'phonographic_neighborhood_frequency' in selected_measures and include_ipa:
            mean, std = phonographic.calculate_neighborhood_frequency(chunk['word'], chunk['IPA'], corpus_data['word'], corpus_data['IPA'], corpus_data[freq_col])
            results[f'phonographic_neighborhood_frequency_{freq_col}'] = mean
            results[f'phonographic_neighborhood_frequency_{freq_col}_SD'] = std
    
    return pl.DataFrame(results)

def main():
    parser = argparse.ArgumentParser(
        description="Jiwar: A Word Neighborhood Calculator",
        epilog="For more details on each option, run with --help."
    )
    parser.add_argument("input_file", help="Name and extension of your input file (e.g., input_file.csv).", type=str, nargs='?')
    parser.add_argument("language", help="Language code (e.g., 'fr' for French, 'en-us' for American English).", type=str, nargs='?')    
    parser.add_argument("--corpus_file", help="Filename of the custom corpus file (optional, must be located in data/corpus/user_loaded/).", type=str)
    parser.add_argument("--frequency_count", type=int, default=1, help="Number of frequency measures in the custom corpus (optional, defaults to 1).")
    parser.add_argument("--all", action="store_true", help="Calculate all available measures.")
    parser.add_argument("--orth", action="store_true", help="Calculate all orthographic measures.")
    parser.add_argument("--phon", action="store_true", help="Calculate all phonological measures.")
    parser.add_argument("--pg", action="store_true", help="Calculate all phonographic measures.")
    parser.add_argument("--generate_ipa", action="store_true", help="Generate IPA transcriptions.")
    parser.add_argument("--help_all", action="store_true", help="Display all help messages and exit.")
    
    args = parser.parse_args()

    if args.help_all:
        parser.print_help()
        print("\nMore detailed help messages:")
        print("\nInput File: The input file must be a CSV file that includes at least a 'word' column. "
              "If an 'IPA' column is present, it will be used for phonological and phonographic analyses. "
              "If not, the --generate_ipa option can be used to create IPA transcriptions automatically.\n")
        print("Language: The language code should correspond to the language of the words in the input file. "
              "Supported language codes can be found in the documentation.\n")
        print("Custom Corpus File: If you want to use a specific corpus for your calculations, you can provide the "
              "filename with this option. It must be located in the 'data/corpus/user_loaded/' directory.\n")
        print("Frequency Count: This option defines how many frequency columns are present in your custom corpus file. "
              "The default is 1. You can adjust it based on your corpus structure.\n")
        print("--all: Use this option to calculate all available measures, including orthographic, phonological, and phonographic.\n")
        print("--orth: This option is used to calculate only orthographic measures, such as orthographic density, OLD20, and clustering coefficient.\n")
        print("--phon: This option is used to calculate only phonological measures, such as phonological density, PLD20, and clustering coefficient.\n")
        print("--pg: This option is used to calculate only phonographic measures, such as phonographic density, PGLD20, and clustering coefficient.\n")
        print("--generate_ipa: If your input file doesn't have an IPA column, use this option to generate IPA transcriptions automatically.\n")
        return

    # check language support
    if not is_supported_language(args.language):
        print(f"Unsupported language: {args.language}")
        print(get_supported_languages_info())
        return

    unsupported_ipa_languages = ['br', 'gl', 'no', 'tl']
    if args.language in unsupported_ipa_languages:
        print(f"Note: The language '{args.language}' is not supported by the automatic IPA transcription tool.")
        print("Only orthographic analysis can be conducted for this language.")
        if args.phon or args.pg:
            print("Phonological and phonographic analyses will be skipped.")
            args.phon = False
            args.pg = False

    # load files/corpus
    file_reader = FileReader()
    try:
        input_data = file_reader.read_input_file(args.input_file)
        print(f"Input data columns: {input_data.columns}")
    except ValueError as e:
        print(f"Error with input file: {e}")
        return
    except IOError as e:
        print(f"Error reading input file: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    if len(input_data) == 0:
        print("No valid data found in the input file after cleaning. Please check your input file.")
        return

    corpus_handler = CorpusHandler()
    try:
        if args.corpus_file:
            corpus_data = corpus_handler.load_corpus(args.language, use_user_corpus=True, corpus_filename=args.corpus_file)
        else:
            corpus_data = corpus_handler.load_corpus(args.language)
        frequency_cols = corpus_handler.get_frequency_columns()
    except ValueError as e:
        print(f"Error loading corpus: {e}")
        return
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # check if IPA is needed/already in the input data
    include_ipa = args.all or args.phon or args.pg or args.generate_ipa

    if include_ipa and 'IPA' in input_data.columns:
        print("IPA column found in input data. Skipping IPA generation.")
    elif include_ipa:
        print("Generating IPA transcriptions for input data...")
        input_data = input_data.with_columns(pl.Series('IPA', IPA_generator.generate_ipa(input_data['word'].to_list(), args.language)))
    
    if include_ipa and 'IPA' not in corpus_data.columns:
        print("Generating IPA transcriptions for corpus data...")
        corpus_data = corpus_data.with_columns(pl.Series('IPA', IPA_generator.generate_ipa(corpus_data['word'].to_list(), args.language)))

    # get measures to calculate
    selected_measures = []
    if args.all or args.orth:
        selected_measures.extend(['orthographic_density', 'OLD20', 'orthographic_clustering_coefficient', 'orthographic_neighborhood_frequency'])
    if args.all or args.phon:
        selected_measures.extend(['phonological_density', 'PLD20', 'phonological_clustering_coefficient', 'phonological_neighborhood_frequency'])
    if args.all or args.pg:
        selected_measures.extend(['phonographic_density', 'PGLD20', 'phonographic_clustering_coefficient', 'phonographic_neighborhood_frequency'])


    chunk_size = 1000
    n_jobs = cpu_count()
    chunks = [input_data[i:i+chunk_size] for i in range(0, len(input_data), chunk_size)]

    with Pool(n_jobs) as pool:
        results = list(tqdm(
            pool.imap(process_chunk, [(chunk, corpus_data, selected_measures, frequency_cols, include_ipa) for chunk in chunks]),
            total=len(chunks),
            desc="Processing chunks"
        ))


    final_results = pl.concat(results)

    column_order = ['word']
    if include_ipa:
        column_order.append('IPA')
    column_order += [col for col in final_results.columns if col not in column_order]
    
    final_results = final_results.select(column_order)

    output_handler = OutputHandler()
    output_file = output_handler.save_results(final_results, args.language)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()