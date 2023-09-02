import model

def comenzar_parse():
    file = input("Ingrese el nombre del archivo: ")
    lista_tokens = model.create_tokens(file)
    if model.analizador(lista_tokens) == None:
        print("Tu programa está bien escrito")
    elif model.analizador(lista_tokens) == False:
        print("Hay un error en tu programa")
    
comenzar_parse()