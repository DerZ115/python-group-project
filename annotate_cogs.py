#!/usr/bin/env python

import sys
import gzip
from collections import Counter

func_categories_file = sys.argv[1]
func_file = sys.argv[2]
# func_file = sys.stdin
cog_file = sys.argv[3]

# Initialize variables
category2description = {}
cog2category = {}
category2count = Counter()
my_cogs = set()


# Step 1: Read description of functional categories
# Example:
#  [J] Translation, ribosomal structure and biogenesis 
with open(func_categories_file) as fin:
    for line in fin:
        line = line.strip()  # Remove leading whitespace and trailing newlines
        if line.startswith("["):  # Skip headers and empty lines
            cat = line[1]
            desc = line[4:]
            category2description[cat] = desc


# Step 2: Read file with OGs of interest
# Example
# arCOG00029	99.4	98.2	97.6
with open(cog_file) as fin:
    for line in fin:
        if line.startswith("#"):  # Skip header line
            continue
        my_cogs.add(line.split()[0]) # Add first item (cog id) to set


# Step 3: Read file with functional annotations
# and remember those for OGs of interest
# gzip: "rt" required for text mode, see https://docs.python.org/3/library/gzip.html
with gzip.open(func_file, "rt") as fin:
    for line in fin:
        cog, cat = line.split()[1:3]
        if cog in my_cogs:
            cog2category[cog] = cat


# Step 4: Count and output the categories for OGs of interest
for cats in cog2category.values():
    for cat in cats:  # In case a cog has multiple categories
        category2count[cat] += 1

for cat, count in category2count.most_common():
    print(f"{count}\t{category2description[cat]}")
