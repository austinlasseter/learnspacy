import spacy

from spacy.tokens import Doc
from spacy.vocab import Vocab
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
for token in doc:
    print(token.text, token.pos_, token.dep_)

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

tokens = nlp(u'rotweiller dog bus')

def cosine_list(tokens):
    cos_dict={}
    for prime_token in tokens:
        temp_d={}
        for compare_token in tokens:
            temp_d[str(compare_token)]=(prime_token.similarity(compare_token))
            cos_dict[str(prime_token)]=temp_d
    return cos_dict

dict_sim_scores = cosine_list(tokens)
dict_sim_scores.keys()

dict_sim_scores['dog']['rotweiller']
dict_sim_scores['dog']['bus']
dict_sim_scores['bus']['rotweiller']
