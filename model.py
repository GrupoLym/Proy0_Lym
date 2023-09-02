
import re
from pathlib import Path

palabras_clave = ["defVar", "drop", "letGo", "walk", "leap", "turn",
                  "turnto", "get", "grab", "nop", "jump", "Defproc"]

caracteres_usados = ["(", ")", "{", "}", ";", ":", "," ]

operadores = ["if", "else", "can", "while", "whilecan"]

parametros_jump = ["x","y", ","]
parametros_walk = ["1","2","3","4","5","6","7","8","9","front","left","right","back",
                    "north","south","west","east", ","]
parametros_leap = ["1","2","3","4","5","6","7","8","9","front","left","right","back",
                    "north","south","west","east", ","]
parametros_turn = ["left","right","around", ","]
parametros_turnto = ["north","south","east","west", ","]
parametros_drop = ["1","2","3","4","5","6","7","8","9", ","]
parametros_get = ["1","2","3","4","5","6","7","8","9", ","]
parametros_grab = ["1","2","3","4","5","6","7","8","9", ","]
parametros_letGo = ["1","2","3","4","5","6","7","8","9", ","]

lista_posibles_escritos = [palabras_clave, caracteres_usados, operadores, parametros_jump, parametros_walk,
                           parametros_leap, parametros_turn, parametros_turnto, parametros_drop, parametros_get,
                           parametros_grab, parametros_letGo]

def create_tokens(archivo):
    path = Path(archivo)
    with path.open('r') as file:
        text = file.read()
        tokens = re.findall(r'\w+|\S', text)
    return tokens

"""esta funcion recorre la lista de tokens y la compar con las listas de caracteres que tenemos arriba, si hay algo
que no deberia estar, retorna false y el programa está mal escrito"""

def analizador(list_tokens):
    respuesta = None #acá quiero que si la respuesta al final sigue siendo NONE, signifique que el programa esta bien escrito
    corrector_sintax = corrector_sintaxis_parametros(list_tokens)
    if corrector_sintax == False:
        return False
    return respuesta

"""acá creé una funcion que recibe la lista de todos los tokens y la funcion(jump, walk, turn, etc) y saca los tokens
que esten al interior de los parentesis"""

def corrector_sintaxis_parametros(list_tokens):
    parametros = None
    respuesta = None
    
    for token in list_tokens:
        existe = False
        for listas_caracteres in lista_posibles_escritos:
            if token in listas_caracteres:
                existe = True
                break
        if existe == False:
            return False
        
        if token == "jump":
            parametros = extraer_parentesis(list_tokens, "jump")
            for caracter in parametros:
                if caracter not in parametros_jump:
                    respuesta = False
        elif token == "walk":
            parametros = extraer_parentesis(list_tokens, "walk")
            for caracter in parametros:
                if caracter not in parametros_walk:
                    respuesta = False
        elif token == "leap":
            parametros = extraer_parentesis(list_tokens, "leap")
            for caracter in parametros:
                if caracter not in parametros_leap:
                    respuesta = False
        elif token == "turn":
            parametros = extraer_parentesis(list_tokens, "turn")
            for caracter in parametros:
                if caracter not in parametros_turn:
                    respuesta = False
        elif token == "turnto":
            parametros = extraer_parentesis(list_tokens, "turnto")
            for caracter in parametros:
                if caracter not in parametros_turnto:
                    respuesta = False
        elif token == "drop":
            parametros = extraer_parentesis(list_tokens, "drop")
            for caracter in parametros:
                if caracter not in parametros_drop:
                    respuesta = False
        elif token == "get":
            parametros = extraer_parentesis(list_tokens, "get")
            for caracter in parametros:
                if caracter not in parametros_get:
                    respuesta = False
        elif token == "grab":
            parametros = extraer_parentesis(list_tokens, "grab")
            for caracter in parametros:
                if caracter not in parametros_grab:
                    respuesta = False
        elif token == "letGo":
            parametros = extraer_parentesis(list_tokens, "letGo")
            for caracter in parametros:
                if caracter not in parametros_letGo:
                    respuesta = False
    return respuesta
 
def extraer_parentesis(list_tokens, funcion):
    interior_parentesis = []
    switch = False

    for token in list_tokens:
        if token == funcion:
            switch = True
        elif switch:
            if token == '(':
                continue  # Ignorar el paréntesis de apertura
            elif token == ')':
                break  # Salir cuando se encuentre el paréntesis de cierre
            else:
                interior_parentesis.append(token)

    return interior_parentesis
     
#no entiendo que hizo de acá para abajo

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
            

                

