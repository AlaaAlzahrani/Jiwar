Orthographic Measures
=====================

Orthographic measures are based on the written form of words. Jiwar calculates the following orthographic measures:

Orthographic N (orth_N)
-----------------------
**Full Name:** Orthographic Neighborhood Size

**Description:** Number and forms of words that differ by one letter via substitution only.

**Output Columns:** 
 * ``orth_N``: Number of orthographic neighbors which differ from the target word by one letter via substitution only.
 * ``orth_N_nbr``: A list of the forms of orthographic neighbors identified in 'orth_N'

Orthographic Density (orth_density)
-----------------------------------
**Full Name:** Orthographic Neighborhood Density

**Description:** Number and forms of words which differ from the target word by one letter via substitution, addition, or deletion.

**Output Columns:** 
 * ``orth_density``: Number of orthographic neighbors which differ from the target word by one letter via substitution, addition, or deletion
 * ``orth_density_nbrs``: A list of the forms of orthographic neighbors identified in 'orth_density'

OLD20
-----
**Full Name:** Orthographic Levenshtein Distance-20

**Description:** Average orthographic Levenshtein distance of the 20 closest neighbors.

**Output Column:** ``OLD20``

Orthographic Network
-----------------------
**Full Name:** Orthographic netowrk science measures

**Description:** Measures the interconnectedness of a word's orthographic neighborhood at the near and distant neighbor levels.

**Output Columns:**
 * ``orth_C``: The clustering coefficient C measures the degree to which a word's immediate orthographic neighbors are also orthographic neighbors of each other.
 * ``orth_2hop_density``: The 2-hop density measures the degree to which a word's immediate and distant orthographic neighbors are also orthographic neighbors of each other.

Orthographic Neighbor Frequency
-------------------------------
**Full Name:** Orthographic Neighborhood Frequency

**Description:** Statistics about the frequencies of orthographic neighboring words. In this measure, neighbors are defined as words differing by one letter via substitution, addition, or deletion.

**Output Columns:** 
 * ``orth_nbr_fpm_m``: The mean frequency per million (fpm) of orthographic neighbors.
 * ``orth_nbr_fpm_SD``: The standard deviation of the frequency per million (fpm) of orthographic neighbors.
 * ``orth_nbr_fpm_higher_m``: The mean frequency per million (fpm) of orthographic neighbors that have a higher frequency than the target word.
 * ``orth_nbr_fpm_lower_m``: The mean frequency per million (fpm) of orthographic neighbors that have a lower frequency than the target word.
 * ``orth_nbr_zipf_m``: The mean Zipf value of orthographic neighbors.
 * ``orth_nbr_zipf_SD``: The standard deviation of the Zipf values of orthographic neighbors.
 * ``orth_nbr_zipf_higher_m``: The mean Zipf value of orthographic neighbors that have a higher frequency than the target word.
 * ``orth_nbr_zipf_lower_m``: The mean Zipf value of orthographic neighbors that have a lower frequency than the target word.
