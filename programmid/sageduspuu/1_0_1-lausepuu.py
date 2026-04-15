tekst=str(open("../../tekstid/lihtne_tekst1.txt",encoding="utf-8").read()).strip().split(".")

for lause in range(len(tekst)):
    tekst[lause]=tekst[lause].strip().split(" ")

print(tekst)

puu={"korrad":0, "oksad":{}}
print(puu)
count=0
for lause in tekst:
    p_oks=puu
    for sona in lause:
        count+=1
        print(count)
        if sona in p_oks["oksad"]:
            p_oks["oksad"][sona]["korrad"]+=1
        else:
            p_oks["oksad"][sona]={}
            p_oks["oksad"][sona]["korrad"]=1
            p_oks["oksad"][sona]["oksad"]={}
        p_oks=p_oks["oksad"][sona]
print(puu)