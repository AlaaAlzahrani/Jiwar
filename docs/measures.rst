Measures
========

Jiwar calculates various neighborhood measures for orthographic, phonological, and phonographic dimensions. Here's an overview of the available measures:

Orthographic Measures
---------------------

1. **Orthographic N (orth_N)**
   Number of words that differ by one letter via substitution.

2. **Orthographic Density (orth_density)**
   Number of words that differ by one letter via substitution, addition, or deletion.

3. **OLD20**
   Average Orthographic Levenshtein Distance of the 20 closest neighbors.

4. **Orthographic C (orth_C)**
   Measures how interconnected a word's orthographic neighbors are.

5. **Orthographic Neighbor Frequency**
   Statistics about the frequencies of orthographic neighboring words.

Phonological Measures
---------------------

1. **Phonological N (phon_N)**
   Number of words that differ by one phoneme via substitution.

2. **Phonological Density (phon_density)**
   Number of words that differ by one phoneme via substitution, addition, or deletion.

3. **PLD20**
   Average Phonological Levenshtein Distance of the 20 closest neighbors.

4. **Phonological C (phon_C)**
   Measures how interconnected a word's phonological neighbors are.

5. **Phonological Neighbor Frequency**
   Statistics about the frequencies of phonological neighboring words.

Phonographic Measures
---------------------

1. **Phonographic N (pg_N)**
   Number of words that differ by one letter and one phoneme.

2. **Phonographic Density (pg_density)**
   Number of words that differ by one letter and one phoneme via substitution, addition, or deletion.

3. **PGLD20**
   Average combined Orthographic and Phonological Levenshtein Distance of the 20 closest neighbors.

4. **Phonographic C (pg_C)**
   Measures how interconnected a word's phonographic neighbors are.

5. **Phonographic Neighbor Frequency**
   Statistics about the frequencies of phonographic neighboring words.

For detailed information on how these measures are calculated and interpreted, please refer to the :doc:`measure_details` page.