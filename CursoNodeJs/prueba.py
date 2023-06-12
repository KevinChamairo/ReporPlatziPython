def agrupar_arreglo(arr):
    grupos = []
    grupo_actual = []
    
    for elemento in arr:
        grupo_actual.append(elemento)
        
        if len(grupo_actual) == 3:
            grupos.append(grupo_actual)
            grupo_actual = []
    
    # Si quedan elementos en el grupo actual y no son suficientes para formar un grupo completo
    if grupo_actual:
        grupos.append(grupo_actual)
    
    return grupos

arreglo = ['A','A','B','C','A','A','A','D','A']
grupos = agrupar_arreglo(arreglo)

for grupo in grupos:
    print(grupo)