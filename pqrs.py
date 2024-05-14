def consulta(datos):
    datos=dict(datos)
    proceso={}
    proceso["pqrs"]=input("Escriba el proceso que el usuario ha realizado P(peticion), Q(queja), R(reclamo) o S(sugerencia): ")
    if proceso["pqrs"] == "P":
        for P in proceso:
            contador =+ 1
            print (contador, P)
        return datos
    elif proceso["pqrs"]=="Q":
        for Q in proceso:
            contador =+ 1
            print (contador, Q)
        return datos
    elif proceso["pqrs"]=="R":
        for R in proceso:
            contador += 1
            print (contador, R)
        return datos
    elif proceso["pqrs"]=="S":
        for S in proceso:
            contador += 1
            print (contador, S)
        return datos
    datos["PQRS"].append(proceso)
    print("PQRS registrado con éxito!")
    return datos         


