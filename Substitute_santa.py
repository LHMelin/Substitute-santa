'''
Tomten är sjuk och ni ska avlasta honom. 

Ditt program handlar om önskelistor.
Skapa ett program som har en meny.
Menyn ska ha två lägen.
1. Skapa önskelista.
2. Läs upp önskelista.

Skapa Önskelista
När du skapar en önskelista så behöver du be användaren om några saker.
1. Vad ska filen heta?
2. Vad heter barnet?
3. Vilka saker ska skrivas till på önskelistan? (for- eller while-loop)

Gör sedan så att du skriver ner i filen på följande sätt.
Rad 1: Namn på barnet
Rad 2 till n: Sak

Läs upp önskelista
Fråga användaren om vad filen heter.
Skriv sedan ut namnet på barnet (första raden).
Skriv sedan "ÖNSKELISTA"
Skriv sedan ut rad för rad vad önskelistan innehåller.
'''
def önskelista():
    global kinder
    kinder = input("Vad heter barnet?\n")
    with open("önskelista.txt", "w", encoding="utf8") as körda:
        print("Skriv in vad du önskar dig. Skriv # om du är klar.")
        while True:
            sak = input(": ")
            if "#" in sak:
                break
            else:
                körda.write(f"{sak}\n")


def läs_önskelista():
    print(f"{kinder}\nÖnskelista\n")              
    with open("önskelista.txt", "r", encoding="utf8") as personal:
        print(personal.readlines())


def meny():

    tr=True
    while tr:
        a = int(input("""
        Vill du:

        1. Skapa önskelista.
        2. Läs upp önskelista.\n
        """))

        if a!=1 and a!=2:
            print("Oj nu blev det fel.\n")
        elif a==1 or a==2:
            tr=False
    
    if a == 1:
        önskelista()
    elif a == 2:
        läs_önskelista()


if __name__ == "__main__":
    meny()


