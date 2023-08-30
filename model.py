
import re

palabras_clave = ["defVar", "drop", "letGo", "walk", "leap", "turn",
                  "turnto", "get", "grab", "nop", "jump", "Defproc"]

parametros_jump = ["x","y"]
parametos_walk = ["1","2","3","4","5","6","7","8","9","front","left","right","back",
                    "north","south","west","east"]
parametros_leap = ["1","2","3","4","5","6","7","8","9","front","left","right","back",
                    "north","south","west","east"]
parametros_turn = ["left","right","around"]
parametros_turnto = ["north","south","east","west"]
parametros_drop = ["1","2","3","4","5","6","7","8","9"]
parametros_get = ["1","2","3","4","5","6","7","8","9"]
parametros_grab = ["1","2","3","4","5","6","7","8","9"]
parametros_letGo = ["1","2","3","4","5","6","7","8","9"]

def tokenize_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        tokens = re.findall(r'\w+|\S', text)
    return tokens

def parametro_x_palabra (palabra):
    if palabra == "jump":
        return parametros_jump
    elif palabra == "walk":
        return parametros_walk
    elif palabra == "leap":
        return parametros_leap
    elif palabra == "turn":
        return parametros_turn
    elif palabra == "turnto":
        return parametros_turnto
    elif palabra == "drop":
        return parametros_drop
    elif palabra == "get":
        return parametros_get
    elif palabra == "grab":
        return parametros_grab
    elif palabra == "letGo":
        return parametros_letGo
    else:
        return ""

""" No se si esta función sirva y sea la manera optimizada de la función de arriba,
creo que no sirve porque el return va a terminar siendo un String igual a parametros_...
más no la variable"""

def parametro_x_palabra_opti (palabra, palabras_clave):
    for word in palabras_clave:
        if palabra in palabras_clave and palabra == "parametros_"+palabra:
            return "parametros_"+palabra

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def palabras_clave (palabras_clave, palabra):
    for word in palabras_clave:
        if palabra not in palabras_clave:
            return "No"

def palabra_parametro (palabras_clave, parametro, palabra):
    for word in palabras_clave:
        if palabra in palabras_clave:
            comparacion = palabra 
            prueba = parametro_x_palabra(comparacion)
            if prueba != "":
                for valor in prueba:
                    if parametro in prueba:
                        return "Yes"
                    else:
                        return "No"
            else: 
                return "No"
            

                

