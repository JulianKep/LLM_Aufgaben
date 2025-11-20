import torch
import matplotlib.pyplot as plt



lines = open("vornamenstatistik_24.csv", "r", encoding="utf-8").read().splitlines()
names = [n.split(",")[1].lower() for n in lines][1:]


allowed = "§€abcdefghijklmnopqrstuvwxyzäöüß-"

allowed_names = []
for name in names:

    count = 0
    for i in range (0, len(name)):
        if name[i] in set(allowed):
            count += 1
    if count == len(name):
        allowed_names.append(name)


annotated_names = ["§"+ n + "€" for n in allowed_names]

bigram_dict = {}

for name in annotated_names:
    for i in range(0, len(name)-1):
        bigram_dict[(name[i], name[i+1])] = bigram_dict.get((name[i], name[i+1]), 0) + 1 


xs = []
xy = []







print(bigram_dict)
""" print(annotated_names) """
