from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-(prijs * korting):.2f} euro.") 

def inkomsten_totaal(inkomsten,btw=0):
    totaal = sum(inkomsten)
    bedrag = float(btw)*totaal
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag:.2f} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    return min(mijn_lijst),max(mijn_lijst)

def gemiddelde(mijn_lijst):
    return (f"De gemiddelde inkomsten deze week zijn {(sum(mijn_lijst)/len(mijn_lijst)):.2f} euro")

def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)
    return (tijdelijk[1],tijdelijk[0])
    
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return (mijn_functie_2(korte_lijst))

# testen functie inkomsten_totaal: 
# answer = inkomsten_totaal([220, 430, 125, 160, 205, 90, 345],0.09)
# print(answer)

# testen functie inkomsten_totaal: zonder parameter btw
# answer = inkomsten_totaal([220, 430, 125, 160, 205, 90, 345])
# print (answer)
    
# testen functie laag_hoog
# answer = laag_en_hoog([220, 430, 125, 160, 205, 90, 345])
# print (answer)

# testen functie gemiddelde
# answer = gemiddelde([220, 430, 125, 160, 205, 90, 345])
# print (answer)

# testen functie meervoudig
# answer = meervoudig([10,5,3,2,1,2,9])
# print(answer)