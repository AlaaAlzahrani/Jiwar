Phonographic Measures
=====================

Phonographic measures combine both the written and spoken forms of words. Jiwar calculates the following phonographic measures:

Phonographic N (pg_N)
---------------------
**Full Name:** Phonographic Neighborhood Size

**Description:** Number of words that differ by one letter and one phoneme (substitution only).

**Output Column:** ``pg_N``

Phonographic Density (pg_density)
---------------------------------
**Full Name:** Phonographic Neighborhood Density

**Description:** Number of words within both orthographic and phonological Levenshtein distance of 1 (substitution, addition, or deletion).

**Output Column:** ``pg_density``

PGLD20
------
**Full Name:** Phonographic Levenshtein Distance-20

**Description:** Average combined orthographic and phonological Levenshtein distance of the 20 closest neighbors.

**Output Column:** ``PGLD20``

Phonographic C (pg_C)
---------------------
**Full Name:** Phonographic Clustering Coefficient

**Description:** Measures how interconnected a word's phonographic neighbors are.

**Output Column:** ``pg_C``

Phonographic Neighbor Frequency
-------------------------------
**Full Name:** Phonographic Neighborhood Frequency

**Description:** Statistics about the frequencies of phonographic neighboring words.

**Output Columns:** 
- ``pg_nbr_fpm_m``: Mean frequency per million of phonographic neighbors
- ``pg_nbr_fpm_SD``: Standard deviation of frequency per million of phonographic neighbors
- ``pg_nbr_fpm_higher_m``: Mean frequency per million of higher frequency phonographic neighbors
- ``pg_nbr_fpm_lower_m``: Mean frequency per million of lower frequency phonographic neighbors

Note: Additional frequency columns may be available depending on the corpus used.
