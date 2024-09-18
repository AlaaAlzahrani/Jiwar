Phonographic Measures
=====================

Phonographic measures combine both the written and spoken forms of words. Jiwar calculates the following phonographic measures:

Phonographic N (pg_N)
---------------------
**Full Name:** Phonographic Neighborhood Size

**Description:** Number and forms of words that differ by one letter and one phoneme via substitution only.

**Output Columns:** 
- ``pg_N``: Number of phonographic neighbors which differ from the target word by one letter and one phoneme via substitution only.
- ``pg_N_nbrs``: A list of the forms of phonographic neighbors identified in 'pg_N'

Phonographic Density (pg_density)
---------------------------------
**Full Name:** Phonographic Neighborhood Density

**Description:** Number and forms of words which differ from the target word by one letter and one phoneme via substitution, addition, or deletion.

**Output Columns:** 
- ``pg_density``: Number of phonographic neighbors which differ from the target word by one letter and one phoneme via substitution, addition, or deletion
- ``pg_density_nbrs``: A list of the forms of phonographic neighbors identified in 'pg_density'

PGLD20
------
**Full Name:** Phonographic Levenshtein Distance-20

**Description:** Average combined orthographic and phonological Levenshtein distance of the 20 closest neighbors.

**Output Column:** ``PGLD20``

Phonographic C (pg_C)
---------------------
**Full Name:** Phonographic Clustering Coefficient

**Description:** Measures the extent to which a word's phonographic neighbors are also phonographic neighbors of each other.

**Output Column:** ``pg_C``

Phonographic Neighbor Frequency
-------------------------------
**Full Name:** Phonographic Neighborhood Frequency

**Description:** Statistics about the frequencies of phonographic neighboring words. In this measure, neighbors are defined as words differing by one letter and one phoneme via substitution, addition, or deletion.

**Output Columns:** 
- ``pg_nbr_fpm_m``: The mean frequency per million (fpm) of phonographic neighbors.
- ``pg_nbr_fpm_SD``: The standard deviation of the frequency per million (fpm) of phonographic neighbors.
- ``pg_nbr_fpm_higher_m``: The mean frequency per million (fpm) of phonographic neighbors that have a higher frequency than the target word.
- ``pg_nbr_fpm_lower_m``: The mean frequency per million (fpm) of phonographic neighbors that have a lower frequency than the target word.
- ``pg_nbr_zipf_m``: The mean Zipf value of phonographic neighbors.
- ``pg_nbr_zipf_SD``: The standard deviation of the Zipf values of phonographic neighbors.
- ``pg_nbr_zipf_higher_m``: The mean Zipf value of phonographic neighbors that have a higher frequency than the target word.
- ``pg_nbr_zipf_lower_m``: The mean Zipf value of phonographic neighbors that have a lower frequency than the target word.