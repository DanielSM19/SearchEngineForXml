import xml.etree.ElementTree as ET

tree = ET.parse('../verbetesWikipedia.xml')

root = tree.getroot()

print(root.tag)

page_tags = root.findall(".//page")
count = len(page_tags)
print("Número de Tags <page>: ", count)

word = "Computer"
title_count = 0 
text_count = 0 

#QUE OS DEUSES AMALDIÇOEM O PYTHON
'''
for page in root.findall(".//page"):
    title = page.find("title")
    if title is not None and title.text:
        title_words = title.text.lower().split()
        title_occurrences = title_words.count(word.lower())
        title_count += title_occurrences

        if title_occurrences > 0:
            text = page.find("text")
            if text is not None and text.text:
                text_words = text.text.lower().split()
                text_count += text_words.count(word.lower())


print(f"A palavra '{word}' aparece {title_count} vezes nas tags <title>.")
print(f"A palavra '{word}' aparece {text_count} vezes nas tags <text> associadas a títulos contendo '{word}'.")
'''

'''
word = "Computer"
count = 0

for page in root.findall(".//page"):
    title = page.find("title")
    if title is not None and title.text:
        count += title.text.lower().count(word.lower())'''

#print(f"A palavra '{word}' aparece {count} vezes dentro das tags <titles>.")

print("\n")
'''
count = 0
word2 = "bit"

for page in root.findall(".//page"):
    text = page.find("text")
    if text is not None and text.text:
        count += text.text.lower().count(word2.lower())
 
print(f"A palavra '{word2}' aparece {count} vezes dentro das tags <text>.")

print("\n")
'''

word = "Computer"
total_count = 0  
top_texts = [] 
top_title =[]
cont2 = 0
'''
for page in root.findall(".//page"):
    text = page.find("text")  # Localiza a tag <text>
    if text is not None and text.text:  # Verifica se <text> tem conteúdo
        word_count = len(text.text.split())  # Divide o texto em palavras e conta os elementos
        print(f"Número de palavras no texto: {word_count}")

'''
for page in root.findall(".//page"):
    title = page.find("title")  
    if title is not None and title.text: 
        if word.lower() in title.text.lower():  
            text = page.find("text")  
            if text is not None and text.text:  
                count = text.text.lower().count(word.lower())  
                if count > 0:  
                    top_texts.append((count, text.text))

top_texts = sorted(top_texts, key=lambda x: x[0], reverse=True)
top_3_texts = top_texts[:5]


print("\n")
print("As 3 tags <text> com mais ocorrências da palavra 'Computer' em títulos:")
for rank, (count, text) in enumerate(top_3_texts, start=1):
    print(f"{rank}º lugar - Ocorrências: {count}\nTexto: {text[:100]}...\n")

    