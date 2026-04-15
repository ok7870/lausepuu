import os

lausearv=0

confolemas=[os.path.isfile("conf.txt")]
if confolemas[0]:
    confolemas.append(open("conf.txt", encoding="utf-8"))


    if input("kasutatakse conf.txt faili? (jah/ei) : ") in ["jah", "j", "yes", "y", "JAH", "YES"]:
        confolemas[0]=True
    else:
        confolemas[0]=False
else:
    print("kirjuta ise")
#if confolemas:
#    confolemas.append(open("conf.txt"))
programmvaljund=open("Valjund.txt","w",encoding="utf-8")
programmvaljund2=open("Valjunddict.txt","w",encoding="utf-8")

def start_dictsorteerija(puu):

    sorted(puu["oksad"][sona]["korrad"])

def start_printer( oks, rekusioon=200000, protsent=False, filter=0, taane=0, seerekusioon=0):

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
            if "lisatuubid" in oks["oksad"][sona[0]]:
                for lisatuup in oks["oksad"][sona[0]]["lisatuubid"]:
                    lisatuupmas=[]
                    for siseminelisatuup in oks["oksad"][sona[0]]["lisatuubid"][lisatuup]:
                        lisatuupmas.append([oks["oksad"][sona[0]]["lisatuubid"][lisatuup][siseminelisatuup], siseminelisatuup])
                    lisatuupmas.sort()
                    lisatuupmas.reverse()
                    printsrting+=str(lisatuup)+"("
                    for lisa in lisatuupmas:
                        printsrting+=" "+str(lisa[1])+" "+str(lisa[0])
                    printsrting+=") "
            if protsent==True:
                print(" "*taane + str(sona[0]), oks["oksad"][sona[0]]["korrad"], oks["oksad"][sona[0]]["korrad"]/lausearv, printsrting, file=programmvaljund)
            else:
                print(" "*taane + str(sona[0]), oks["oksad"][sona[0]]["korrad"], printsrting, file=programmvaljund)

            printsrting=""
            start_printer(oks["oksad"][sona[0]], rekusioon, protsent, filter, taane+4, seerekusioon)

avtxt=False

def dictfailinimekirjutaja(kausat_faili_asukoht, failinimed1=""):
    print(os.listdir("../../tekstid/"+kausat_faili_asukoht))
    for _ in os.listdir("../../tekstid/"+kausat_faili_asukoht):

        if os.path.isfile("../../tekstid/"+kausat_faili_asukoht+"/"+_):
            failinimed=(open("../../tekstid/"+kausat_faili_asukoht+"/"+_).read().strip().split("\n"))
            for files in range(len(failinimed)):
                if failinimed!=[]:
                    failinimed1+=failinimed[files]+" "

        else:
            return(dictfailinimekirjutaja(kausat_faili_asukoht+"/"+_, failinimed1))

    return failinimed1.strip()

if confolemas[0]:
    kausat_faili_asukoht=confolemas[1].readline().strip()

    if kausat_faili_asukoht=="-":
        confolemas[0]=False

    elif kausat_faili_asukoht=="avtxt":
        kausat_faili_asukoht=confolemas[1].readline().strip()
        if kausat_faili_asukoht=="?":
            kausat_faili_asukoht=input("teksti failide kausta/teksti faili asukoht/ ava tekstifail (avtxt): ")
        if os.path.isfile("../../tekstid/"+kausat_faili_asukoht):
            failinimed=open("../../tekstid/"+kausat_faili_asukoht).read().strip().split("\n")
        elif os.path.isdir("../../tekstid/"+kausat_faili_asukoht):
            failinimed=dictfailinimekirjutaja(kausat_faili_asukoht)

        kausat_faili_asukoht=confolemas[1].readline().strip()
        if kausat_faili_asukoht=="?":
            kausat_faili_asukoht=input("kausta/teksti faili asukoht/ ava tekstifail (avtxt): ")

    elif kausat_faili_asukoht=="?":
        kausat_faili_asukoht=input("kausta/teksti faili asukoht/ ava tekstifail (avtxt): ")
        if kausat_faili_asukoht=="avtxt":
            kausat_faili_asukoht=confolemas[1].readline().strip()
            if kausat_faili_asukoht=="?":
                kausat_faili_asukoht=input("teksti failide kausta/teksti faili asukoht/ ava tekstifail (avtxt): ")

            if os.path.isfile("../../tekstid/"+kausat_faili_asukoht):
                failinimed=open("../../tekstid/"+kausat_faili_asukoht).read().strip().split("\n")
            elif os.path.isdir("../../tekstid/"+kausat_faili_asukoht):
                failinimed=dictfailinimekirjutaja(kausat_faili_asukoht)

            kausat_faili_asukoht=confolemas[1].readline().strip()
            if kausat_faili_asukoht=="?":
                kausat_faili_asukoht=input("kausta/teksti faili asukoht/ ava tekstifail (avtxt): ")
        else:
            if os.path.isdir("../../tekstid/"+kausat_faili_asukoht):
                failinimed=os.listdir("../../tekstid/"+kausat_faili_asukoht)
            else:
                failinimed=["../../tekstid/"+kausat_faili_asukoht]

    elif os.path.isdir("../../tekstid/"+kausat_faili_asukoht):
        failinimed=os.listdir("../../tekstid/"+kausat_faili_asukoht)
    else:
        failinimed=["../../tekstid/"+kausat_faili_asukoht]

    


else:        
    kausat_faili_asukoht=input("kausta/teksti faili asukoht/ ava tekstifail (avtxt): ")

    if kausat_faili_asukoht=="avtxt":
        kausat_faili_asukoht=input("teksti failide kausta/teksti faili asukoht, milles on tekstid, mida on vaja läbi lugeda: ")

        if os.path.isfile("../../tekstid/"+kausat_faili_asukoht):
            failinimed=open("../../tekstid/"+kausat_faili_asukoht).read().strip().split("\n")
        elif os.path.isdir("../../tekstid/"+kausat_faili_asukoht):
            failinimed=dictfailinimekirjutaja(kausat_faili_asukoht)
        
        kausat_faili_asukoht=input("kausta faili asukoht: ")
        if os.path.isdir("../../tekstid/"+kausat_faili_asukoht):
            failinimed=os.listdir("../../tekstid/"+kausat_faili_asukoht)
        else:
            exit("not dir")
    else:
        if os.path.isdir("../../tekstid/"+kausat_faili_asukoht):
            failinimed=os.listdir("../../tekstid/"+kausat_faili_asukoht)
        else:
            failinimed=[kausat_faili_asukoht.split("/")[-1]]
            kausat_faili_asukoht=("/".join(kausat_faili_asukoht.split("/")[0:-1]))

sonaarv=0
puu={"korrad":0, "oksad":{}}

if confolemas[0]:
    inpt=confolemas[1].readline().strip()
    if inpt=="?":
        inpt=input("stanza/text : ")
else:
    inpt=input("stanza/text : ")

#komad ja kraam
if confolemas[0]:
    temp=confolemas[1].readline().strip()
    if temp == "?":
        komadega = input("komad (jah/ei)").lower() in ["jah", "j", "yes", "y", "JAH", "YES"]
    else:
        komadega = temp.lower() in ["jah", "j", "yes", "y", "JAH", "YES"]
else:
    komadega = input("komad (jah/ei)").lower() in ["jah", "j", "yes", "y", "JAH", "YES"]



if inpt == "text":

    for failinimi in failinimed:

        if kausat_faili_asukoht=="":
            ava="../../tekstid/"+failinimi
        else:
            ava="../../tekstid/"+kausat_faili_asukoht+"/"+failinimi
        if os.path.isfile(ava):

            if input("komadega (y/n)") in ["jah", "j", "yes", "y", "JAH", "YES"]:
                tekst=open(ava,encoding="utf-8").read().strip().split(".")
            else:
                tekst=open(ava,encoding="utf-8").read().strip().replace(",","").split(".")



            if len(tekst[-1])<1:
                del tekst[-1]

            for lause in range(len(tekst)):
                tekst[lause]=tekst[lause].strip().split(" ")

            for lause in range(len(tekst)):
                for sona in range(len(tekst[lause])):
                    tekst[lause][sona]=tekst[lause][sona].rstrip(",.!?:;#")
                    sonaarv+=1

            count=0
            for lause in tekst:
                lausearv+=1
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

    import stanza
    start_stanza=stanza.Pipeline(lang="et", processors="tokenize,pos,lemma")


    for failinimi in failinimed:
        print(failinimi)
        if kausat_faili_asukoht=="":
            ava="../../tekstid/"+failinimi
        else:
            ava="../../tekstid/"+kausat_faili_asukoht+"/"+failinimi
            if os.path.isfile(ava):
                if komadega:
                    stanzatudfail=start_stanza(open(ava,encoding="utf-8").read().strip())
                else:
                    stanzatudfail=start_stanza(open(ava,encoding="utf-8").read().strip().replace(",",""))
            else:
                print(ava, "not file")
                continue
#        stanzatudfail=start_stanza(open(ava, encoding="utf-8").read())
        for lause in range(len(stanzatudfail.sentences)):
            lausearv+=1
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


if confolemas[0]:
    lspk=confolemas[1].readline().strip()
    krk=confolemas[1].readline().strip()
    if lspk=="?":
        lspk=int(input("lause pikkus: "))
    if krk=="?":
        krk=int(input("min kordusde arv: "))
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

if confolemas[0]:
    protsent=confolemas[1].readline().strip()
    if protsent=="?":
        protsent=input("kas protsentidega? (jah/ei) : ")
else:
    if input("kas protsentidega? (jah/ei) : ") in ["jah", "j", "yes", "y", "JAH", "YES"]:
        protsent=True
    else:
        protsent=False

start_printer(puu, lspk, protsent, krk) #lause pikkus; sügavus
print(puu, file=programmvaljund2)
programmvaljund.close()
programmvaljund2.close()