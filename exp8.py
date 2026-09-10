import spacy
nlp = spacy.load("en_core_web_sm")
text = input("Enter a sentence: ")
doc = nlp(text)

doc = nlp(text)
print("\nNamed Entities")
print("-" * 40)
for ent in doc.ents:
    print(f"Entity : {ent.text}")
    print(f"Lable : {ent.label_}")
    print("-" * 40)
