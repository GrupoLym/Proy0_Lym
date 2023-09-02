import model

def comenzar_parse():
    file = input("Ingrese el nombre del archivo: ")
    lista_tokens = model.create_tokens(file)
    
    
comenzar_parse()