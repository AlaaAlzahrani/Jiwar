Phonological Measures
=====================

Phonological measures are based on the pronunciation of words. Jiwar calculates the following phonological measures:

Phonological N (phon_N)
-----------------------
**Full Name:** Phonological Neighborhood Size

**Description:** Number and forms of words that differ by one phoneme via substitution only.

**Output Columns:** 
 *  ``phon_N``: Number of phonological neighbors which differ from the target word by one phoneme via substitution only.
 *  ``phon_N_nbrs``: A list of the forms of phonological neighbors identified in 'phon_N'

Phonological Density (phon_density)
-----------------------------------
**Full Name:** Phonological Neighborhood Density

**Description:** Number and forms of words which differ from the target word by one phoneme via substitution, addition, or deletion.

**Output Columns:** 
 *  ``phon_density``: Number of phonological neighbors which differ from the target word by one phoneme via substitution, addition, or deletion
 *  ``phon_density_nbrs``: A list of the forms of phonological neighbors identified in 'phon_density'

PLD20
-----
**Full Name:** Phonological Levenshtein Distance-20

**Description:** Average phonological Levenshtein distance of the 20 closest neighbors.

**Output Column:** ``PLD20``

Phonological Network
-----------------------
**Full Name:** Phonological netowrk science measures

**Description:** Measures the interconnectedness of a word's phonological neighborhood at the near and distant neighbor levels.

**Output Columns:**
 * ``phon_C``: The clustering coefficient C measures the degree to which a word's immediate phonological neighbors are also phonological neighbors of each other.
 * ``phon_2hop_density``: The 2-hop density measures the degree to which a word's immediate and distant phonological neighbors are also phonological neighbors of each other.

Phonological Neighbor Frequency
-------------------------------
**Full Name:** Phonological Neighborhood Frequency

**Description:** Statistics about the frequencies of phonological neighboring words. In this measure, neighbors are defined as words differing by one phoneme via substitution, addition, or deletion.

**Output Columns:** 
 *  ``phon_nbr_fpm_m``: The mean frequency per million (fpm) of phonological neighbors.
 *  ``phon_nbr_fpm_SD``: The standard deviation of the frequency per million (fpm) of phonological neighbors.
 *  ``phon_nbr_fpm_higher_m``: The mean frequency per million (fpm) of phonological neighbors that have a higher frequency than the target word.
 *  ``phon_nbr_fpm_lower_m``: The mean frequency per million (fpm) of phonological neighbors that have a lower frequency than the target word.
 *  ``phon_nbr_zipf_m``: The mean Zipf value of phonological neighbors.
 *  ``phon_nbr_zipf_SD``: The standard deviation of the Zipf values of phonological neighbors.
 *  ``phon_nbr_zipf_higher_m``: The mean Zipf value of phonological neighbors that have a higher frequency than the target word.
 *  ``phon_nbr_zipf_lower_m``: The mean Zipf value of phonological neighbors that have a lower frequency than the target word.
