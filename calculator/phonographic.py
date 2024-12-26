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

def process_words(words, ipa_words, corpus_words, corpus_ipa, task):
    results = []
    corpus_words_list = corpus_words.to_list()
    corpus_ipa_list = corpus_ipa.to_list()

    for word, ipa in tqdm(zip(words, ipa_words), total=len(words), desc=f"Calculating {task}"):
        if task == 'N':
            neighbors = [(w, i) for w, i in zip(corpus_words_list, corpus_ipa_list)
                         if is_substitution(word, w) and is_substitution(ipa, i)]
            results.append((float(len(neighbors)), ", ".join([f"{w}({i})" for w, i in neighbors])))
        elif task == 'density':
            neighbors = [(w, i) for w, i in zip(corpus_words_list, corpus_ipa_list)
                         if cached_distance(word, w) == 1 and cached_distance(ipa, i) == 1]
            results.append((float(len(neighbors)), ", ".join([f"{w}({i})" for w, i in neighbors])))
        elif task == 'pgld20':
            distances = sorted([max(cached_distance(word, w), cached_distance(ipa, i))
                                for w, i in zip(corpus_words_list, corpus_ipa_list)
                                if word != w or ipa != i])
            results.append(float(np.mean(distances[:20])) if len(distances) >= 20 else float(np.nan))

        elif task == 'clustering':
            neighbors_1hop = [(w, i) for w, i in zip(corpus_words_list, corpus_ipa_list)
                            if cached_distance(word, w) == 1 and cached_distance(ipa, i) == 1]
            
            if len(neighbors_1hop) < 2:
                C = 0.0
            else:
                connections_1hop = sum(1 for i, (n1_w, n1_i) in enumerate(neighbors_1hop)
                                    for n2_w, n2_i in neighbors_1hop[i+1:]
                                    if cached_distance(n1_w, n2_w) == 1 and cached_distance(n1_i, n2_i) == 1)
                max_connections_1hop = (len(neighbors_1hop) * (len(neighbors_1hop) - 1)) / 2
                C = connections_1hop / max_connections_1hop if max_connections_1hop > 0 else 0.0

            neighbors_2hop = []
            for n1_w, n1_i in neighbors_1hop:
                second_neighbors = [(w, i) for w, i in zip(corpus_words_list, corpus_ipa_list)
                                  if cached_distance(n1_w, w) == 1 and cached_distance(n1_i, i) == 1
                                  and (w != word or i != ipa)
                                  and (w, i) not in neighbors_1hop]
                neighbors_2hop.extend(second_neighbors)
            
            neighbors_2hop = list(set(neighbors_2hop))
            
            all_neighbors = neighbors_1hop + neighbors_2hop
            if len(all_neighbors) < 2:
                two_hop_density = 0.0
            else:
                total_connections = sum(1 for i, (n1_w, n1_i) in enumerate(all_neighbors)
                                    for n2_w, n2_i in all_neighbors[i+1:]
                                    if cached_distance(n1_w, n2_w) == 1 and cached_distance(n1_i, n2_i) == 1)
                max_possible_connections = (len(all_neighbors) * (len(all_neighbors) - 1)) / 2
                two_hop_density = total_connections / max_possible_connections if max_possible_connections > 0 else 0.0
            
            results.append((float(C), float(two_hop_density)))
    return results

def calculate_N(words, ipa_words, corpus_words, corpus_ipa):
    results = process_words(words, ipa_words, corpus_words, corpus_ipa, 'N')
    counts = [float(result[0]) for result in results]
    neighbors_strings = [result[1] for result in results]
    return pl.Series(counts), pl.Series(neighbors_strings)

def calculate_density(words, ipa_words, corpus_words, corpus_ipa):
    results = process_words(words, ipa_words, corpus_words, corpus_ipa, 'density')
    counts = [float(result[0]) for result in results]
    neighbors_strings = [result[1] for result in results]
    return pl.Series(counts), pl.Series(neighbors_strings)

def calculate_pgld20(words, ipa_words, corpus_words, corpus_ipa):
    results = process_words(words, ipa_words, corpus_words, corpus_ipa, 'pgld20')
    return pl.Series(results)

def calculate_neighborhood_frequency(words, ipa_words, corpus_words, corpus_ipa, frequencies):
    corpus_df = pd.DataFrame({
        'word': corpus_words,
        'ipa': corpus_ipa,
        'frequency': frequencies
    })
    
    def process_chunk(chunk):
        results = []
        for word, ipa in chunk:
            neighbors = corpus_df[
                (corpus_df['word'].apply(lambda x: cached_distance(word, x) == 1)) &
                (corpus_df['ipa'].apply(lambda x: cached_distance(ipa, x) == 1))
            ]
            word_freq = corpus_df[(corpus_df['word'] == word) & (corpus_df['ipa'] == ipa)]['frequency'].iloc[0] if word in corpus_df['word'].values and ipa in corpus_df['ipa'].values else 0
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
    word_ipa_pairs = list(zip(words, ipa_words))
    chunks = [word_ipa_pairs[i:i+chunk_size] for i in range(0, len(word_ipa_pairs), chunk_size)]
    
    results = []
    for chunk in tqdm(chunks, desc="Calculating phonographic neighborhood frequency"):
        results.extend(process_chunk(chunk))
    
    mean_series = pl.Series([r[0] for r in results])
    std_series = pl.Series([r[1] for r in results])
    mean_higher_series = pl.Series([r[2] for r in results])
    mean_lower_series = pl.Series([r[3] for r in results])
    
    return mean_series, std_series, mean_higher_series, mean_lower_series

def calculate_network_metrics(words, ipa_words, corpus_words, corpus_ipa):
    results = process_words(words, ipa_words, corpus_words, corpus_ipa, 'clustering')
    C_values = pl.Series([result[0] for result in results])
    two_hop_values = pl.Series([result[1] for result in results])
    return C_values, two_hop_values