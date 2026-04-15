import json
import os

import stanza
start_stanza=stanza.Pipeline(lang="et")

programmvaljund=open("Valjund.txt","w",encoding="utf-8")

def start_printer( oks, rekusioon=1, filter=0, taane=0, seerekusioon=0):
    if rekusioon==seerekusioon:
        return
    
    seerekusioon+=1
    for sona in oks["oksad"]:
        if filter <= oks["oksad"][sona]["korrad"]:
            print(" "*taane, sona, oks["oksad"][sona]["korrad"],file=programmvaljund)
            print(" "*taane, sona, oks["oksad"][sona]["korrad"])
            start_printer(oks["oksad"][sona], rekusioon, filter, taane+4, seerekusioon)

kausat_faili_asukoht=input("kausta/teksti faili asukoht: ")

if os.path.isdir("../../tekstid/"+kausat_faili_asukoht):

    failinimed=os.listdir("../../tekstid/"+kausat_faili_asukoht)

else:
    failinimed=[kausat_faili_asukoht.split("/")[-1]]

    if len(kausat_faili_asukoht.split("/"))>1:
        kausat_faili_asukoht=("/".join(kausat_faili_asukoht.split("/")[0:-1]))+"/"
    else:
        kausat_faili_asukoht=""

    kaust=("mitte kaust")

puu={"korrad":0, "oksad":{}}

inpt=input("stanza/text : ")

if inpt == "text":

    for failinimi in failinimed:

        if kausat_faili_asukoht=="":
            ava="../../tekstid/"+failinimi
        else:
            ava="../../tekstid/"+kausat_faili_asukoht+"/"+failinimi

        tekst=open(ava,encoding="utf-8").read().strip().split(".")

        if len(tekst[-1])<1:
            del tekst[-1]

        for lause in range(len(tekst)):
            tekst[lause]=tekst[lause].strip().split(" ")

        count=0
        for lause in tekst:
            p_oks=puu
            for sona in lause:
                count+=1
                if sona in p_oks["oksad"]:
                    p_oks["oksad"][sona]["korrad"]+=1
                else:
                    p_oks["oksad"][sona]={}
                    p_oks["oksad"][sona]["korrad"]=1
                    p_oks["oksad"][sona]["oksad"]={}
                p_oks=p_oks["oksad"][sona]

elif inpt == "stanza" :


        for failinimi in failinimed:

            if kausat_faili_asukoht=="":
                ava="../../tekstid/"+failinimi

            else:
                ava="../../tekstid/"+kausat_faili_asukoht+"/"+failinimi

            stanzatudfail=start_stanza(open(ava, encoding="utf-8").read())

            for lause in range(len(stanzatudfail.sentences)):

                p_oks=puu

                for sona in range(len(stanzatudfail.sentences[lause].words)):
                    if stanzatudfail.sentences[lause].words[sona].upos in p_oks["oksad"]:
                        p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].upos]["korrad"]+=1
                    else:
                        p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].upos]={}
                        p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].upos]["korrad"]=1
                        p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].upos]["oksad"]={}
                    p_oks=p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].upos]

else:
    exit("wrong write type")


#print(json.dumps(puu,indent=2)) #alternatiivne trükkimismoodus

start_printer(puu, int(input("lause pikkus: ")), int(input("min kordusde arv: "))) #lause pikkus; sügavus

programmvaljund.close()