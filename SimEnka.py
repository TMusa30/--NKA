import sys

def ukloni_duplikate(lista):
  nova_lista = []
  for element in lista :
    if element not in nova_lista:
      nova_lista.append(element)
  return nova_lista

ulaz_string = ""
for line in sys.stdin:
    ulaz_string += line

lines = ulaz_string.splitlines()

pocetno_stanje = lines[4]
prijelazi = lines[5:]

ulazi = lines[0].split("|")




stanjaTrenutnogProblema = [pocetno_stanje]
izlaz = []

for trenutno_stanje in stanjaTrenutnogProblema:
    for prijelaz in prijelazi:
        pocetno, prijelazni_simbol = prijelaz.split("->")[0].split(",")
        if pocetno == trenutno_stanje and prijelazni_simbol == "$":
            novo_stanje = prijelaz.split("->")[1]
            for stanje in novo_stanje.split(","):
                if stanje not in stanjaTrenutnogProblema:
                    stanjaTrenutnogProblema.append(stanje)
if len(stanjaTrenutnogProblema) > 1 and "#" in stanjaTrenutnogProblema:
            stanjaTrenutnogProblema.remove("#")
izlaz.append(",".join(sorted(stanjaTrenutnogProblema)))
proba = stanjaTrenutnogProblema
i = 0
for ulaz in ulazi:
    i += 1
    izlaz_trenutnog_ulaza = []
    
    for simbol in ulaz.split(","):
        
        nova_trenutna_stanja = []
        for trenutnoStanjeTrenutnogProblema in stanjaTrenutnogProblema:
            for prijelaz in prijelazi:
                pocetno, prijelazni_simbol = prijelaz.split("->")[0].split(",")
                if pocetno == trenutnoStanjeTrenutnogProblema and prijelazni_simbol == simbol:
                    novo_stanje = prijelaz.split("->")[1]
                    for stanje in novo_stanje.split(","):
                        nova_trenutna_stanja.append(stanje)
        nova_trenutna_stanja = ukloni_duplikate(nova_trenutna_stanja)
        if not nova_trenutna_stanja:
            nova_trenutna_stanja.extend("#")
        if len(nova_trenutna_stanja) > 1 and "#" in nova_trenutna_stanja:
            nova_trenutna_stanja.remove("#")
        stanjaTrenutnogProblema = nova_trenutna_stanja

        
        for trenutnoStanjeTrenutnogProblema in stanjaTrenutnogProblema:
            for prijelaz in prijelazi:
                pocetno, prijelazni_simbol = prijelaz.split("->")[0].split(",")
                if pocetno == trenutnoStanjeTrenutnogProblema and prijelazni_simbol == "$":
                    novo_stanje = prijelaz.split("->")[1]
                    for stanje in novo_stanje.split(","):
                        if stanje not in stanjaTrenutnogProblema:
                            stanjaTrenutnogProblema.append(stanje)
        
        if len(stanjaTrenutnogProblema) > 1 and "#" in stanjaTrenutnogProblema:
            stanjaTrenutnogProblema.remove("#")
        izlaz_trenutnog_ulaza.append(",".join(sorted(stanjaTrenutnogProblema)))
    if i != 1:
        izlaz_trenutnog_ulaza.insert(0, ",".join(sorted(proba)))
    izlaz.append("|".join(izlaz_trenutnog_ulaza))
    print("|".join(izlaz))
    izlaz = []
    stanjaTrenutnogProblema = proba
    
    
    
    
