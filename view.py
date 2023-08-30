import model

def comenzar_parse():
    file = input("Ingrese el nombre del archivo: ")
    print(model.tokenize_text_from_file(file))
    
comenzar_parse()