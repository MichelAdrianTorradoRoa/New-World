def consulta(datos):
    datos=dict(datos)
    proceso={}
    procesos=input("Escriba el proceso que el usuario ha realizado P(peticion), Q(queja), R(reclamo) o S(sugerencia): ")
    if procesos == "P":
        for P in proceso:
            print (contador, P)
            contador =+ 1
        return datos
    elif procesos=="Q":
        for Q in proceso:
            contador =+ 1
            print (contador, Q)
        return datos
    elif procesos=="R":
        for R in proceso:
            contador += 1
            print (contador, R)
        return datos
    elif procesos=="S":
        for S in proceso:
            contador += 1
            print (contador, S)
        return datos
    datos["PQRS"].append(proceso)
    print("PQRS registrado con éxito!")
    return datos         


