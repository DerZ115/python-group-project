Answers to questions

1) A study of conserved genes using the eggNOG database
    1. Which genes are universally required for an organism to survive
        1. How many per domain?
            Archaea: 175
            Bacteria: 123
            Eukaryota: 273
        2. Provide the results as three files listing the OGs in sorted order (by name)
            cogs_archaea_o99.txt
            cogs_bacteria_o99.txt
            cogs_eukaryota_o99.txt

    2. Which common bacterial genes occur almost exclusively as single-copy genes?
        1. Provide the results as a sorted text file.
            cogs_bacteria_o50_u99.txt
        2. How many of these OGs were also identified as universal bacterial OGs?
            73

    3. Identify all OGs that occur as single-copy in at least 97 % of all archaea?
        1. How many such OGs did you identify? Provide the results as a sorted text file.
            121
            cogs_archaea_os97.txt
        2. Are there archaea which lack 4 or more of these universal OGs? Which organism lacks the most?
            Pyrococcus horikoshii OT3                   missing 7 OGs
            Candidatus Korarchaeum cryptofilum OPF8     missing 6 OGs
            Candidatus Nitrosopumilus sediminis         missing 5 OGs
            Thermosphaera aggregans DSM 11486           missing 4 OGs
            Halobiforma nitratireducens JCM 10879       missing 4 OGs
            Halobellus rufus                            missing 4 OGs
        3. What is the preferred growing temperature/environment?
            Pyrococcus horikoshii:
                optimal temperature: 98 °C
                environment: hydrothermal vents
                https://pubmed.ncbi.nlm.nih.gov/9672687/

            Candidatus Korarchaeum cryptofilum:
                enrichment temperature: 85 °C
                environment: hot springs (Yellowstone National Park)
                https://pubmed.ncbi.nlm.nih.gov/18535141/

            Candidatus Nitrosopumilus sediminis:
                temperature: unknown
                environment: arctic marine sediment
                https://pubmed.ncbi.nlm.nih.gov/23209211/

            Thermosphaera aggregans:
                temperature: 85 °C
                environment: hot springs
                https://pubmed.ncbi.nlm.nih.gov/9542073/

            Halobiforma nitratireducens:
                temperature: 36-41 °C
                salt concentration: 3.5 M
                pH: 8.5
                environment: clay form soda lakes
                https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-51-5-1825

            Halobellus rufus:
                temperature: 37 °C
                salt concentration: 15 %(w/v) -> 2,5 M
                environment: solar salt
                https://pubmed.ncbi.nlm.nih.gov/24609529/

    4. Compile an overview of the functional categories of these 121 archaeal OGs.
        cogs_archaea_os97_categories.txt     

2) ASCII cat
    SEE ASCIIcat.py
