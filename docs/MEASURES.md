# Jiwar Measures

This document provides details on all measures calculated by Jiwar.

| Measure | Output Column | Full Name | Description |
|---------|---------------|-----------|-------------|
| Orthographic N | orth_N | Orthographic Neighborhood Size | Number of words that differ by one letter |
| Orthographic Density | orth_density | Orthographic Neighborhood Density | Number of words within an orthographic Levenshtein distance of 1 |
| OLD20 | OLD20 | Orthographic Levenshtein Distance-20 | Average orthographic Levenshtein distance of the 20 closest neighbors |
| Orthographic C | orth_C | Orthographic Clustering Coefficient | Measures how interconnected a word's orthographic neighbors are |
| Orthographic Neighbor Frequency | orth_nbr_fpm_m, orth_nbr_fpm_SD, etc. | Orthographic Neighborhood Frequency | Statistics about the frequencies of orthographic neighboring words |
| Phonological N | phon_N | Phonological Neighborhood Size | Number of words that differ by one phoneme |
| Phonological Density | phon_density | Phonological Neighborhood Density | Number of words within a phonological Levenshtein distance of 1 |
| PLD20 | PLD20 | Phonological Levenshtein Distance-20 | Average phonological Levenshtein distance of the 20 closest neighbors |
| Phonological C | phon_C | Phonological Clustering Coefficient | Measures how interconnected a word's phonological neighbors are |
| Phonological Neighbor Frequency | phon_nbr_fpm_m, phon_nbr_fpm_SD, etc. | Phonological Neighborhood Frequency | Statistics about the frequencies of phonological neighboring words |
| Phonographic N | pg_N | Phonographic Neighborhood Size | Number of words that differ by one letter and one phoneme |
| Phonographic Density | pg_density | Phonographic Neighborhood Density | Number of words within both orthographic and phonological Levenshtein distance of 1 |
| PGLD20 | PGLD20 | Phonographic Levenshtein Distance-20 | Average combined orthographic and phonological Levenshtein distance of the 20 closest neighbors |
| Phonographic C | pg_C | Phonographic Clustering Coefficient | Measures how interconnected a word's phonographic neighbors are |
| Phonographic Neighbor Frequency | pg_nbr_fpm_m, pg_nbr_fpm_SD, etc. | Phonographic Neighborhood Frequency | Statistics about the frequencies of phonographic neighboring words |

Note: For frequency measures, 'fpm' stands for 'frequency per million', and additional columns may be available depending on the corpus used.