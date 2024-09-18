Phonological Measures
=====================

Phonological measures are based on the pronunciation of words. Jiwar calculates the following phonological measures:

Phonological N (phon_N)
-----------------------
**Full Name:** Phonological Neighborhood Size

**Description:** Number of words that differ by one phoneme (substitution only).

**Output Column:** ``phon_N``

Phonological Density (phon_density)
-----------------------------------
**Full Name:** Phonological Neighborhood Density

**Description:** Number of words within a phonological Levenshtein distance of 1 (substitution, addition, or deletion).

**Output Column:** ``phon_density``

PLD20
-----
**Full Name:** Phonological Levenshtein Distance-20

**Description:** Average phonological Levenshtein distance of the 20 closest neighbors.

**Output Column:** ``PLD20``

Phonological C (phon_C)
-----------------------
**Full Name:** Phonological Clustering Coefficient

**Description:** Measures how interconnected a word's phonological neighbors are.

**Output Column:** ``phon_C``

Phonological Neighbor Frequency
-------------------------------
**Full Name:** Phonological Neighborhood Frequency

**Description:** Statistics about the frequencies of phonological neighboring words.

**Output Columns:** 
- ``phon_nbr_fpm_m``: Mean frequency per million of phonological neighbors
- ``phon_nbr_fpm_SD``: Standard deviation of frequency per million of phonological neighbors
- ``phon_nbr_fpm_higher_m``: Mean frequency per million of higher frequency phonological neighbors
- ``phon_nbr_fpm_lower_m``: Mean frequency per million of lower frequency phonological neighbors

Note: Additional frequency columns may be available depending on the corpus used.
