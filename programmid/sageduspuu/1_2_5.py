import json
import os

confolemas=[]
confolemas.append(os.path.isfile("conf.txt"))
if confolemas[0]:
    confolemas.append(open("conf.txt"))
#if confolemas:
#    confolemas.append(open("conf.txt"))
programmvaljund=open("Valjund.txt","w",encoding="utf-8")
programmvaljund2=open("Valjunddict.txt","w",encoding="utf-8")

def start_dictsorteerija(puu):

    sorted(puu["oksad"][sona]["korrad"])

def start_printer( oks, rekusioon=200000, filter=0, taane=0, seerekusioon=0):

    def start_sorter(puu):
        jarjestus=[]
        for lause in puu['oksad']:
            jarjestus.append([lause, puu['oksad'][lause]["korrad"]])


        def sordiabi(paar):
            return(paar[1])

        return(sorted(jarjestus, reverse=True, key=sordiabi))


    if rekusioon==seerekusioon:
        return
    printsrting=""
    seerekusioon+=1
    for sona in start_sorter(oks):
        if filter <= oks["oksad"][sona[0]]["korrad"]:
            for lisatuup in oks["oksad"][sona[0]]["lisatuubid"]:
                lisatuupmas=[]
                for siseminelisatuup in oks["oksad"][sona[0]]["lisatuubid"][lisatuup]:
                    lisatuupmas.append([oks["oksad"][sona[0]]["lisatuubid"][lisatuup][siseminelisatuup], siseminelisatuup])
                lisatuupmas.sort()
                printsrting+=str(lisatuup)+"("
                for lisa in lisatuupmas:
                    printsrting+=" "+str(lisa[1])+" "+str(lisa[0])
                printsrting+=") "

            print(" "*taane, sona[0], oks["oksad"][sona[0]]["korrad"], printsrting, file=programmvaljund)
            printsrting=""
            start_printer(oks["oksad"][sona[0]], rekusioon, filter, taane+4, seerekusioon)


if confolemas[0]:
    kausat_faili_asukoht=confolemas[1].readline().strip()
    if kausat_faili_asukoht=="?":
        kausat_faili_asukoht=input("kausta/teksti faili asukoht: ")
else:
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

if confolemas[0]:
    inpt=confolemas[1].readline().strip()
    if inpt=="?":
        inpt=input("stanza/text : ")
else:
    inpt=input("stanza/text : ")

if inpt == "text":

    for failinimi in failinimed:
        print(failinimi)
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

    import stanza
    start_stanza=stanza.Pipeline(lang="et")

    if confolemas[0]:
        tuupid=str(confolemas[1].readline().strip())
        if tuupid=="?":
            tuupid=input("stanza: text / lemma /  upos / xpos / feats (Näide: text : tekst,lemma) : ").split(",")
        else:
            tuupid=tuupid.split(",")
    else:
        tuupid=input("stanza: text / lemma /  upos / xpos / feats (Näide: text : tekst,lemma) : ").split(",")


    dellist=[]
    for tuup in tuupid:
        if tuup not in ["text", "lemma", "upos", "xpos", "feats"]:
            dellist.append(tuup)
    for kustutamine in dellist:
        tuupid.remove(kustutamine)
        print("varjantidest eemaldatud:", kustutamine)

        
    for failinimi in failinimed:
        print(failinimi)
        if kausat_faili_asukoht=="":
            ava="../../tekstid/"+failinimi
        else:
            ava="../../tekstid/"+kausat_faili_asukoht+"/"+failinimi
        stanzatudfail=start_stanza(open(ava, encoding="utf-8").read())
        for lause in range(len(stanzatudfail.sentences)):
            p_oks=puu
            for sona in range(len(stanzatudfail.sentences[lause].words)):
                if stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0]) in p_oks["oksad"]:
                    p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]["korrad"]+=1
                    for lisatuubid in tuupid[1:]:
                        if stanzatudfail.sentences[lause].words[sona].__getattribute__(lisatuubid) not in p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]["lisatuubid"][lisatuubid]:
                            p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]["lisatuubid"][lisatuubid][stanzatudfail.sentences[lause].words[sona].__getattribute__(lisatuubid)]=1
                        else:
                            p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]["lisatuubid"][lisatuubid][stanzatudfail.sentences[lause].words[sona].__getattribute__(lisatuubid)]+=1
                else:
                    p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]={}
                    p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]["korrad"]=1
                    p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]["lisatuubid"]={}
                    for lisatuubid in tuupid[1:]:
                        p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]["lisatuubid"][lisatuubid]={}
                        p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]["lisatuubid"][lisatuubid][stanzatudfail.sentences[lause].words[sona].__getattribute__(lisatuubid)]=1
                    p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]["oksad"]={}
                p_oks=p_oks["oksad"][stanzatudfail.sentences[lause].words[sona].__getattribute__(tuupid[0])]

else:
    exit("wrong write type")


#print(json.dumps(puu,indent=2)) #alternatiivne trükkimismoodus


if confolemas[0]:
    lspk=int(confolemas[1].readline().strip())
    krk=int(confolemas[1].readline().strip())
    if lspk=="?":
        lspk=input("lause pikkus: ")
    if krk=="?":
        input("min kordusde arv: ")
else:
    lspk=input("lause pikkus")
    krk=input("min kordusde arv: ")
if lspk=="":
    lspk=20000000000000
else:
    lspk=int(lspk)
if krk=="":
    krk=0
else:
    krk=int(krk)

start_printer(puu, lspk, krk) #lause pikkus; sügavus
print(puu, file=programmvaljund2)
programmvaljund.close()
programmvaljund2.close()