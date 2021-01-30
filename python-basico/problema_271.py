def cadena_tipo(cadena):
    var1 = cadena[0].lower()
    var2 = cadena[0]
    if var1 == var2:
        resultado = True
    else:
        resultado = False

    return resultado

print cadena_tipo('Edward')