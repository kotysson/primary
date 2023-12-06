import spacy

class NERExtractor:
  def __init__(self):
    self.nlp = spacy.load("en_core_web_sm")
    self.named_entities = []

  def extract_named_entities(self, text):
    doc = self.nlp(text)
    self.named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    return self.named_entities

  def display_named_entities(self):
    print(f'Named Entities:')
    for i in self.named_entities:
      print(f'{i[0]} ({i[1]})')

test = NERExtractor()
test.extract_named_entities('Apple Inc. is a technology company. Amazon not so much.')
test.display_named_entities()