import polars as pl
import pandas as pd
import numpy as np
from Levenshtein import distance
from functools import lru_cache
from tqdm import tqdm


@lru_cache(maxsize=10000)
def cached_distance(word1, word2):
    return distance(word1, word2)

def is_substitution(word1, word2):
    if len(word1) != len(word2):
        return False
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1

def process_words(words, corpus_series, task):
    results = []
    corpus_list = corpus_series.to_list()

    for word in tqdm(words, desc=f"Calculating {task}"):
        if task == 'N':
            neighbors = [x for x in corpus_list if is_substitution(word, x)]
            results.append((float(len(neighbors)), ", ".join(neighbors)))
        elif task == 'density':
            neighbors = [x for x in corpus_list if cached_distance(word, x) == 1]
            results.append((float(len(neighbors)), ", ".join(neighbors)))
        elif task == 'pld20':
            distances = sorted([cached_distance(word, x) for x in corpus_list if x != word])
            results.append(float(np.mean(distances[:20])) if len(distances) >= 20 else float(np.nan))
        elif task == 'clustering':
            neighbors = [x for x in corpus_list if cached_distance(word, x) == 1]
            if len(neighbors) < 2:
                results.append(0.0)
            else:
                connections = sum(1 for i, n1 in enumerate(neighbors)
                                  for n2 in neighbors[i+1:]
                                  if cached_distance(n1, n2) == 1)
                max_connections = (len(neighbors) * (len(neighbors) - 1)) / 2
                results.append(connections / max_connections if max_connections > 0 else 0.0)

    return results

def calculate_N(words, corpus):
    corpus_series = pl.Series(corpus)
    results = process_words(words, corpus_series, 'N')
    counts = [float(result[0]) for result in results]
    neighbors_strings = [result[1] for result in results]
    return pl.Series(counts), pl.Series(neighbors_strings)

def calculate_density(words, corpus):
    corpus_series = pl.Series(corpus)
    results = process_words(words, corpus_series, 'density')
    counts = [float(result[0]) for result in results]
    neighbors_strings = [result[1] for result in results]
    return pl.Series(counts), pl.Series(neighbors_strings)

def calculate_pld20(words, corpus):
    corpus_series = pl.Series(corpus)
    results = process_words(words, corpus_series, 'pld20')
    return pl.Series(results)


def calculate_neighborhood_frequency(words, corpus, frequencies):
    corpus_df = pd.DataFrame({'word': corpus, 'frequency': frequencies})
    
    def process_chunk(chunk):
        results = []
        for word in chunk:
            neighbors = corpus_df[corpus_df['word'].apply(lambda x: cached_distance(word, x) == 1)]
            word_freq = corpus_df[corpus_df['word'] == word]['frequency'].iloc[0] if word in corpus_df['word'].values else 0
            neighbor_freqs = neighbors['frequency']
            
            if len(neighbor_freqs) > 0:
                mean_freq = float(neighbor_freqs.mean())
                std_freq = float(neighbor_freqs.std())
                higher_freqs = neighbor_freqs[neighbor_freqs > word_freq]
                lower_freqs = neighbor_freqs[neighbor_freqs < word_freq]
                mean_higher = float(higher_freqs.mean()) if len(higher_freqs) > 0 else np.nan
                mean_lower = float(lower_freqs.mean()) if len(lower_freqs) > 0 else np.nan
                results.append((mean_freq, std_freq, mean_higher, mean_lower))
            else:
                results.append((np.nan, np.nan, np.nan, np.nan))
        return results

    chunk_size = 1000
    chunks = [words[i:i+chunk_size] for i in range(0, len(words), chunk_size)]
    
    results = []
    for chunk in tqdm(chunks, desc="Calculating phonological neighborhood frequency"):
        results.extend(process_chunk(chunk))
    
    mean_series = pl.Series([r[0] for r in results])
    std_series = pl.Series([r[1] for r in results])
    mean_higher_series = pl.Series([r[2] for r in results])
    mean_lower_series = pl.Series([r[3] for r in results])

    return mean_series, std_series, mean_higher_series, mean_lower_series

def calculate_clustering_coefficient(words, corpus):
    corpus_series = pl.Series(corpus)
    results = process_words(words, corpus_series, 'clustering')
    return pl.Series(results)