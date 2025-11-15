from bs4 import BeautifulSoup


with open("data/zug_leicht.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")



texts = [p.get_text(" ",strip=True) 
         for p in soup.select("div.paragraph > p.text") 
         if p.get_text(strip=True)]


word_list = [word for text in texts for word in text.split()]

print(word_list)