import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

lines = open("vornamenstatistik_24.csv", "r", encoding="utf-8").read().splitlines()
names = list(set([n.split(",")[1] for n in lines][1:]))

sorted_names = sorted(names, key=lambda x: len(x))
count_chars = {}
for w in sorted_names:
    chars = ["<s>"] + list(w) + ["<e>"]
    for c1 in chars:
        count_chars[c1.lower()] = count_chars.get(c1.lower(), 0) + 1
all_chars = list(count_chars.keys())
sorted_chars = sorted(count_chars.items(), key=lambda x: x[1])
frequent_chars = [i for i in all_chars if count_chars[i] >= 10]

xs = []
ys = [] 

for w in names[2:3]:
    print(w)
    chars = ["<s>"] + list(w) + ["<e>"]
    for c1, c2 in zip(chars, chars[1:]):
        id_x = frequent_chars.index(c1.lower())
        id_y = frequent_chars.index(c2.lower())
        xs.append(id_x)
        ys.append(id_y)



# Die Listen konvertieren wir noch zu Tensoren
xs = torch.tensor(xs)
ys = torch.tensor(ys)
xs, ys


xenc = F.one_hot(xs, num_classes=len(frequent_chars)).float()  # float conversion ist elementar für Input in NN
xenc.shape
xenc
""" plt.imshow(xenc)
plt.show() """


g = torch.Generator().manual_seed(41)
W = torch.randn((len(frequent_chars), len(frequent_chars)), generator=g) 

y_pred = xenc @ W
y_pred


print(W)

