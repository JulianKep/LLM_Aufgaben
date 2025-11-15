from bs4 import BeautifulSoup

with open("data/weihnachtsmarkt_leicht.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

with open("german_words.txt", encoding="utf-8") as i:
    reference_words = i.read().split()

texts = [p.get_text(" ",strip=True) 
         for p in soup.select("div.paragraph > p.text") 
         if p.get_text(strip=True)]


word_list = [word for text in texts for word in text.split()]

print(word_list)

word_lengths = [len(word) for word in word_list]

average_word_length = sum(word_lengths) / len(word_lengths)



print(f'average word length: {average_word_length}')
print(f'intersection with most common words: {len(set(reference_words) & set(word_list)) / len(word_list)}')
