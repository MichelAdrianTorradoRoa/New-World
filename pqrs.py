def consulta(datos):
    datos=dict(datos)
    PQRS={}
    proceso=input("Escriba el proceso que el usuario ha realizado P(peticion), Q(queja), R(reclamo) o S(sugerencia): ")
    if proceso == "P":
        for P in proceso:
            contador =+ 1
            print (contador, P)
        return datos
    elif proceso=="Q":
        for Q in proceso:
            contador =+ 1
            print (contador, Q)
        return datos
    elif proceso=="R":
        for R in proceso:
            contador += 1
            print (contador, R)
        return datos
    elif proceso=="S":
        for S in proceso:
            contador += 1
            print (contador, S)
        return datos         


