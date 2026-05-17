import datetime # ipmortē datetime moduli, ļauj stradāt ar datumiem un laikiem

preces = [] #izveido tukšu sarakstu preces

def pievienot_preces(): #izveidoju funkciju ar nosaukumu pievienot_preces
    nosaukums = input("Preces nosaukums: ") #pieprasu ievadīt preces nosaukumu
    materials = input("Materials: ") #pieprasu ievadīt meteriāla veidu
    daudzums = int(input("Daudzums:")) #pieprasu ievadīt preces daudzumu, int() pārveido ievadīto tekstu par veselu skaitli
    cena = float(input("Cena:")) # pieprasu ievadīt preces cenu, float() pārveido tekstu par decimālskaitli
    garantija_gados = int(input("Garantijas termiņš (gados): ")) #pieprasu ievadīt preces garantijas termiņu

    garantijas_beigas = datetime.date.today().replace(year=datetime.date.today().year + garantija_gados)

    prece = { # izveido vārdnīcu ar preces datiem
        "nosaukums": nosaukums,
        "materials": materials,
        "daudzums": daudzums,
        "cena": cena,
        "garantijas_beigas": garantijas_beigas
    } #aizver vārdnīcu

    preces.append(prece) #pievieno jauno preci sarakstam preces
    print("Prece pievienota!") # ievada ziņojumu ekrānā

def paradit_preces(): # funkcija preču attēlošanai
    if not preces: # pārbauda, vai saraksts ir tukš
        print("Nav nevienas preces.") # izvada paziņojumu, ja tukšs
        return # pārtrauc funkcijas darbību

    for p in preces: # cikls iziet cauri katrai precei sarakstā
        print(f"{p['nosaukums']}, {p['materials']}, Daudzums: {p['daudzums']}, Cena: {p['cena']}, Garantija līdz: {p['garantijas_beigas']}")
    print() #Izvada preces informāciju, p - paņem informāciju no vārdnīcas

def atrast_preces(): #funkcija preces atrašanai
    mekle = input("Iavadi preces nosaukumu: ")# ievada meklējamo nosaukumu
    for p in preces: # pārbauda katru preci sarakstā
        if p["nosaukums"].lower() == mekle.lower():# salīdzina nosaukumus, lower()pārvērš tekstu mazajos burtos
            print("Atrastā prece:")# izvada tekstu
            print(p)#izvada visu vārdnīcu
            return # beidz funkciju, kad prece atrasta
        print("Prece nav atrasta.") # ja nekas nav atrasts

def parbaudit_garantijas(): #funkcija garantiju pārbaudei
    sodiena = datetime.date.today()#saglabā šodienas datumu
    for p in preces:#pārbauda visas preces
        if (p["garantijas_beigas"]- sodiena).days <= 30:# aprēķina dienu starpību, ja līdz garantijas beigām <=30 dienas, tad izvada brīdinājumu
            print(f"Precei '{p['nosaukums']}' drīz beigsies garantija!")# izvada paziņojumu pa garantiju
    print() #

while True: #bezgalīgs cikls, proframma darbojas, līdz lietotājs izvēlas iziet
    print("1 - Pievienot preci")
    print("2 - Parādīt visas preces ")
    print("3 - Atrast preci")
    print("4 - Pārbaudīt garantijas")
    print("0 - Iziet")

    izvelne = input("Izvēlies darbību:") #lietotājs ievada izvēli

    if izvelne == "1":
        pievienot_preces()
    elif izvelne == "2":
        paradit_preces()
    elif izvelne == "3":
        atrast_preces()
    elif izvelne == "4":
        parbaudit_garantijas()
    elif izvelne == "0":
        break# pārtrauc while ciklu, programma beidzas
    else:# citādi
        print("Nepareiza izvēle.")# kļūdas ziņojums
