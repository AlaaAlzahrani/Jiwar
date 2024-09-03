import polars as pl
import pandas as pd
import numpy as np
from Levenshtein import distance
from functools import lru_cache
from tqdm import tqdm

@lru_cache(maxsize=10000)
def cached_distance(word1, word2):
    return distance(word1, word2)

def process_words(words, corpus_series, task):
    results = []
    corpus_list = corpus_series.to_list()

    for word in tqdm(words, desc=f"Calculating {task}"):
        if task == 'density':
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
            neighbor_freqs = neighbors['frequency']
            if len(neighbor_freqs) > 0:
                results.append((float(neighbor_freqs.mean()), float(neighbor_freqs.std())))
            else:
                results.append((np.nan, np.nan))
        return results

    chunk_size = 1000
    chunks = [words[i:i+chunk_size] for i in range(0, len(words), chunk_size)]
    
    results = []
    for chunk in tqdm(chunks, desc="Calculating neighborhood frequency"):
        results.extend(process_chunk(chunk))
    
    return pl.Series([r[0] for r in results]), pl.Series([r[1] for r in results])

def calculate_clustering_coefficient(words, corpus):
    corpus_series = pl.Series(corpus)
    results = process_words(words, corpus_series, 'clustering')
    return pl.Series(results)