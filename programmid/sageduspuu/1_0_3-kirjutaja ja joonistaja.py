import json

tekst=open("../../tekstid/lihtne_tekst1.txt",encoding="utf-8").read().strip().split(".")

if len(tekst[-1])<1:
    del tekst[-1]

for lause in range(len(tekst)):
    tekst[lause]=tekst[lause].strip().split(" ")

print(tekst)

puu={"korrad":0, "oksad":{}}
print(puu, "test")
print()
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

print(json.dumps(puu,indent=2, ensure_ascii=False)) #alternatiivne trükkimismoodus

print()
print()

def printer( oks, rekusioon=1, taane=0, seerekusioon=0):
    if rekusioon<=seerekusioon:
        return
    
    seerekusioon+=1
    for sona in oks["oksad"]:
        print(" "*taane, sona, oks["oksad"][sona]["korrad"])
        printer(oks["oksad"][sona], rekusioon, taane+4, seerekusioon)



    
printer(puu, 20)