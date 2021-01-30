menu_generico=['Saludar','Despedirse','Salir','Otra opcion','Otra opcion 2']

def menu(Lista):
    print 'Menu de la Aplicacion'
    opcion = ''
    while opcion <=0 or opcion >= (len(Lista)+1):    
        for i in range(len(Lista)):
            print  '[' + str(i+1) + '] ' + str(Lista[i])
        opcion = int(raw_input('Escoja una opcion: '))
        if opcion <=0 or opcion >= (len(Lista)+1) :
            print 'solo puede escoger una de las opciones entre 1 y ' + str(len(Lista)) + ' Intentelo de nuevo...'
    return opcion

menu(menu_generico)