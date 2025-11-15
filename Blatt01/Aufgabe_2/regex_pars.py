import re

with open("data/zug_schwer.html", "r", encoding="utf-8") as f:
	content = f.read()
	
regex = r'<div class="paragraph ">\s*<p class="text">(.+?)</p>\s*</div>'

find_text = re.findall(regex, content, re.DOTALL)

cleaned = list(re.sub(r'<.*?>|<.*?/>|\n|\xa0|<.*?>.*?<.*?>', "",x) for x in find_text)

print(cleaned)
