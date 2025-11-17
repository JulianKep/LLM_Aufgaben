from bs4 import BeautifulSoup

# Read html
with open("data/zug_schwer.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Read Wordlist
with open("german_words.txt", encoding="utf-8") as i:
    reference_words = i.read().split()

# extract Text from html by only including text that is between <p class="text"> tags which are between <div class="paragraph"> tags
texts = [p.get_text(" ",strip=True) 
         for p in soup.select("div.paragraph > p.text") 
         if p.get_text(strip=True)]

# atomize the text, extract only words in one long list
word_list = [word for text in texts for word in text.split()]

# get all word lengths
word_lengths = [len(word) for word in word_list]

# METRIK: ARTIKEL LÄNGE
article_length = sum(word_lengths)

# METRIK: ANZAHL DER ZAHLEN
num_of_numbers = 0
for word in word_list:
    if word.isdigit():
        num_of_numbers += 1

# METRIK: DURCHSCHNITTLICHE WORTLÄNGE
average_word_length = sum(word_lengths) / len(word_lengths)

# METRIK: SCHNITT MIT DER LISTE DER 1000 HÄUFIGSTEN WORTE
deckung = len(set(reference_words) & set(word_list)) / len(word_list)


print(f'article length: {article_length}')
print(f'number of numbers: {num_of_numbers}')
print(f'average word length: {average_word_length}')
print(f'intersection with most common words: {deckung}')


