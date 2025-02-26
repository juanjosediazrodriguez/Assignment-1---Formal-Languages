def leerDFA():
    DFAS = []
    nDFA = int(input())
    
    for i in range(nDFA):
        nEstados = int(input())

        while True:
            alfabeto = input("").split()
    
            if all(c.isalpha() and c.islower() and len(c) == 1 for c in alfabeto):
                break
            print(" Error: Solo se permiten letras en minúsculas (a-z). Inténtalo de nuevo.")
            

        estadosFinales = set(map(int, input().split()))

        transiciones = {estado: {} for estado in range(nEstados)}  

       
        for estado in range(nEstados):
            valores = list(map(int, input().split()))

            for j, simbolo in enumerate(alfabeto):
                    transiciones[valores[0]][simbolo] = int(valores[j+1])
        

        DFAS.append((nEstados, alfabeto, estadosFinales, transiciones))
    return DFAS

def encontrarEquivalentes(nEstados, alfabeto, estadosFinales, transiciones):
    TablaEquivalencias = [[True] * nEstados for i in range(nEstados)]
    
    paresMin = []
    
    for i in range(nEstados):
        for j in range(i+1,nEstados):
            if (i in estadosFinales and j not in estadosFinales) or (i not in estadosFinales and j in estadosFinales):
                TablaEquivalencias[i][j] = TablaEquivalencias[j][i] = False
             

    cambios = True
    while cambios:
        cambios = False
        for i in range(nEstados):
            for j in range(i+1,nEstados):
                if TablaEquivalencias[i][j] == True:
                    for simbolo in alfabeto:
                        estado_i = transiciones[i][simbolo]
                        estado_j = transiciones[j][simbolo]
                        if TablaEquivalencias[estado_i][estado_j] == False:
                            TablaEquivalencias[i][j] = TablaEquivalencias[j][i] = False
                            cambios = True
                            break
        

    for i in range(nEstados):
        for j in range(i+1,nEstados):
            if TablaEquivalencias[i][j] == True:
                paresMin.append((i,j))
    
    return paresMin
    
def main():
    DFAS = leerDFA()  

    for i, (nEstados, alfabeto, estadosFinales, transiciones) in enumerate(DFAS):
        
     
        equivalentes = encontrarEquivalentes(nEstados, alfabeto, estadosFinales, transiciones)
        
     
        print("\n✅ Estados equivalentes encontrados:")
        if equivalentes:
            for par in equivalentes:
                print(par)
        else:
            print("No hay estados equivalentes.")
