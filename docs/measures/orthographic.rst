Orthographic Measures
=====================

Orthographic measures are based on the written form of words. Jiwar calculates the following orthographic measures:

Orthographic N (orth_N)
-----------------------
**Full Name:** Orthographic Neighborhood Size

**Description:** Number of words that differ by one letter (substitution only).

**Output Column:** ``orth_N``

Orthographic Density (orth_density)
-----------------------------------
**Full Name:** Orthographic Neighborhood Density

**Description:** Number of words within an orthographic Levenshtein distance of 1 (substitution, addition, or deletion).

**Output Column:** ``orth_density``

OLD20
-----
**Full Name:** Orthographic Levenshtein Distance-20

**Description:** Average orthographic Levenshtein distance of the 20 closest neighbors.

**Output Column:** ``OLD20``

Orthographic C (orth_C)
-----------------------
**Full Name:** Orthographic Clustering Coefficient

**Description:** Measures how interconnected a word's orthographic neighbors are.

**Output Column:** ``orth_C``

Orthographic Neighbor Frequency
-------------------------------
**Full Name:** Orthographic Neighborhood Frequency

**Description:** Statistics about the frequencies of orthographic neighboring words.

**Output Columns:** 
- ``orth_nbr_fpm_m``: Mean frequency per million of orthographic neighbors
- ``orth_nbr_fpm_SD``: Standard deviation of frequency per million of orthographic neighbors
- ``orth_nbr_fpm_higher_m``: Mean frequency per million of higher frequency orthographic neighbors
- ``orth_nbr_fpm_lower_m``: Mean frequency per million of lower frequency orthographic neighbors

Note: Additional frequency columns may be available depending on the corpus used.
