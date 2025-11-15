import torch
import matplotlib.pyplot as plt

allowed = set("abcdefghijklmnopqrstuvwxyz")

lines = open("data/vornamenstatistik_24.csv", "r", encoding="utf-8").read().splitlines()


# Extract names from the lines
just_names = [line.split(",")[1] for line in lines][1:]

cleaned_names = [name for name in just_names if set(name).issubset(allowed)]

# Add Affixes and Suffixes to get word beginnings and endings, also make all names lower case
modified_names = [("$" + name.lower() + "%") for name in cleaned_names]




print(cleaned_names)

# Extract bigrams from Names
bigram_dict = {}
for name in cleaned_names:
    for index in range(len(name)-1):
        if not((name[index], name[index+1]) in bigram_dict):
            bigram_dict[(name[index], name[index+1])] = 1
        else:
            bigram_dict[(name[index], name[index+1])] += 1

print(bigram_dict)