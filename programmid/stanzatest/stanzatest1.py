import stanza

waf=stanza.Pipeline(lang="et")

doc=waf("juku tuli kooli. kool oli tore.")

print(doc)

print(doc.sentences[0].words[2].upos)

#    {
#      "id": 3,
#      "text": "tore",
#      "lemma": "tore",
#      "upos": "ADJ",
#      "xpos": "A",
#      "feats": "Case=Nom|Degree=Pos|Number=Sing",
#      "head": 0,
#      "deprel": "root",
#      "start_char": 26,
#      "end_char": 30,
#      "misc": "SpaceAfter=No"
#    }
