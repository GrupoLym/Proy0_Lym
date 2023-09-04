import model

def comenzar_parse():
    #file = input("Ingrese el nombre del archivo: ")
    file = "test.txt"
    lista_tokens = model.create_tokens(file)
    respuesta = model.analizador()
    if respuesta == None:
        print("Tu programa está bien escrito")
    elif respuesta == False:
        print("Hay un error en tu programa")
        
comenzar_parse()