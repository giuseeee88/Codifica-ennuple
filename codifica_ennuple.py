import math

def AzzeraTupla(n):
    tupla = []
    for i in range(1, n + 1):
        tupla.append(0)
    return tupla

def StampaTupla(tupla):
    print(f"\nLa tua {len(tupla)}-pla è: ({', '.join(str(x) for x in tupla)})")

def Pairing(tupla):
    # Bisogna controllare in base al numero di componenti quante volte applicare la funzione di pairing (impostare uno schema ricorsivo)
    # <X, Y> = 2^X * (2*y + 1) - 1
    codifica = int((math.pow(2, tupla[0]) * ((2 * tupla[1]) + 1)) - 1) # <- caso più semplice a due coordinate
    return codifica

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
        codifica = codifica * math.pow(primo, tupla[i])
        indicePrimo += 1
    return int(codifica)

print("Codifica e decodifica di n-uple")
print("------------------------------------------------------------------")

coordinate = int(input("\nInserire il numero di coordinate della n-upla: "))

tupla = AzzeraTupla(coordinate)

i = 0

while i < coordinate:
    try:
        coordinata = int(input(f"Inserire la {i+1}° coordinata: "))
        if(coordinata < 0):
            print("Coordinata non valida! La coordinata deve essere un numero naturale.")
        else:
            tupla[i] = coordinata
            i += 1
    except:
        print("Coordinata non valida")

StampaTupla(tupla)

print("\nScegliere il tipo di codifica:")
print("1 - Funzione di pairing")
print("2 - Numeri di Gödel")

numeroCodifica = int(input(f"\nCodifica in: "))

match(numeroCodifica):
    case 1:
        codifica = Pairing(tupla)
    case 2:
        codifica = NumeriDiGodel(tupla)
    case _:
        print("Codifica non disponibile")

print("\nCodifica:", codifica)