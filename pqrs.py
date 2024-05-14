def consulta(datos):
    datos=dict(datos)
    PQRS={}
    proceso=input("Escriba el proceso que el usuario ha realizado P(peticion), Q(queja), R(reclamo) o S(sugerencia): ")
    if proceso == "P":
        for P in proceso:
            print (contador, P)
            contador += 1
        return datos
    elif proceso=="Q":
        for Q in proceso:
            print (contador, Q)
            contador += 1
        return datos
    elif proceso=="R":
        for R in proceso:
            print (contador, R)
            contador += 1
        return datos
    elif proceso=="S":
        for S in proceso:
            print (contador, S)
            contador += 1
        return datos         


