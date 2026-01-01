def InserisciInput():
    inputValido = False

    while inputValido == False:
        inputUtente = input("\nInserire il numero di coordinate della n-upla: ")
        try:
            coordinate = int(inputUtente)
            inputValido = True
        except:
            print("Il numero di coordinate deve essere un numero intero positivo")
            
    tupla = AzzeraTupla(coordinate)

    i = 0

    while i < coordinate:
        inputUtente = input(f"Inserire la {i+1}° coordinata: ")
        try:
            coordinata = int(inputUtente)
            if(coordinata < 0):
                print("Coordinata non valida! La coordinata deve essere un numero naturale.")
            else:
                tupla[i] = coordinata
                i += 1
        except:
            print("Coordinata non valida")
    return tupla

def AzzeraTupla(n):
    tupla = []
    for i in range(1, n + 1):
        tupla.append(0)
    return tupla

def StampaTupla(tupla):
    print(f"\nLa tua {len(tupla)}-pla è: ({', '.join(str(x) for x in tupla)})")

## Versione ricorsiva
def PairingR(tupla):
    # <X, Y> = (2^X * (2*Y + 1)) - 1
    if(len(tupla) == 1):
        print("Non è possibile codificare solo una coordinata")
        return 0
    elif(len(tupla) == 2):
        codifica = int(((1 << tupla[0]) * ((2 * tupla[1]) + 1)) - 1)
        return codifica
    else:
        coppia = [tupla[len(tupla) - 2], tupla[len(tupla) - 1]]
        tupla.pop()
        tupla.pop()
        codificaCoppia = PairingR(coppia)
        tupla.append(codificaCoppia)
        return PairingR(tupla)

def NPrimo(n):
    count = 0
    numero_corrente = 2
    ultimo_primo = 0
    while count < n:
        is_primo = True
        for j in range(2, numero_corrente):
            if numero_corrente % j == 0:
                is_primo = False
                break
        if is_primo:
            count += 1
            ultimo_primo = numero_corrente
        numero_corrente += 1
    return int(ultimo_primo)
    
def NumeriDiGodel(tupla):
    indicePrimo = 1
    codifica = 1
    for i in range(0, len(tupla)):
        primo = NPrimo(indicePrimo)
        codifica = codifica * (primo**tupla[i])
        indicePrimo += 1
    return int(codifica)

print("Codifica e decodifica di n-uple")
print("------------------------------------------------------------------")

tupla = InserisciInput()
continua = True

while continua:
    StampaTupla(tupla)

    inputValido = False

    while inputValido == False:
        print("\nScegliere una funzione:")
        print("1 - Funzione di pairing")
        print("2 - Numeri di Gödel")
        print("3 - Reinserisci input")
        print("4 - Esci")

        inputUtente = input("\nScegli una funzione: ")
        
        try:
            idFunzione = int(inputUtente)
            inputValido = True
        except:
            print("La funzione scelta non è valida")

    codifica = 0
    tuplaDaCodificare = tupla

    match(idFunzione):
        case 1:
            codifica = PairingR(tuplaDaCodificare)
        case 2:
            codifica = NumeriDiGodel(tuplaDaCodificare)
        case 3:
            tupla = InserisciInput()
        case 4:
            continua = False
            print("\nProgramma terminato.")
        case _:
            print("\nCodifica non disponibile")

    if(codifica > 0):
        print("\nLa codifica è: ", codifica)
    print("------------------------------------------------------------------")