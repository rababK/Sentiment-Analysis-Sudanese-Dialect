import stanza
stanza.download('en')
stanza.download('ar')
nlp = stanza.Pipeline('en')
doc = nlp('the cat drink milk.')
for sentence in doc.sentences:
    print(sentence.ents)
    print(sentence.dependencies)

stanza.download('ar')

nlp2 = stanza.Pipeline('ar')
doc = nlp2('.ولد الرئيس اوباما في هاواي')
for sentence in doc.sentences:
    print(sentence.ents)
    print(sentence.dependencies)