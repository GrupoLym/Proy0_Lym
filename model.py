
import re
from pathlib import Path

palabras_clave = ["defVar", "drop", "letGo", "walk", "leap", "turn",
                  "turnto", "get", "grab", "nop", "jump", "Defproc"]

caracteres_usados = ["(", ")", "{", "}", ";", ":", "," , "="]

operadores = ["if", "else", "can", "facing", "not", "while", "whilecan"]

parametros_comandos = ["1","2","3","4","5","6","7","8","9","front","left","right","back",
                    "north","south","west","east", ",", "around"]
variables_creadas = [[],
                     []]


lista_posibles_escritos = [palabras_clave, caracteres_usados, operadores, parametros_comandos]

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
    respuesta = None
    
    while len(list_tokens) > 0 and respuesta == None:
        token = list_tokens[0] 
        existe = False
        
        if token == "defVar":
           if list_tokens[list_tokens.index(token) + 2] == "=":
                posicion_nombre = list_tokens.index(token) + 1
                posicion_valor = posicion_nombre + 2
                valor = list_tokens[posicion_valor]
                creacion_variables(list_tokens[posicion_nombre], valor)
           else:
                posicion_nombre = list_tokens.index(token) + 1
                posicion_valor = posicion_nombre + 1
                valor = list_tokens[posicion_valor]
                creacion_variables(list_tokens[posicion_nombre], valor)
                
        for listas_caracteres in lista_posibles_escritos:
            if token in listas_caracteres or token in variables_creadas[0] or token in variables_creadas[1]:
                existe = True
                break
        if existe == False:
            return False
        
        if token == "if":
            respuesta = condicional_if(list_tokens)
        elif token == "jump":
            respuesta = funcion_comandos(list_tokens, "jump")
        elif token == "walk":
            respuesta = funcion_comandos(list_tokens, "walk")
        elif token == "leap":
            respuesta = funcion_comandos(list_tokens, "leap")
        elif token == "turn":
            respuesta = funcion_comandos(list_tokens, "turn")
        elif token == "turnto":
            respuesta = funcion_comandos(list_tokens, "turnto")
        elif token == "drop":
            respuesta = funcion_comandos(list_tokens, "drop")
        elif token == "get":
            respuesta = funcion_comandos(list_tokens, "get")
        elif token == "grab":
            respuesta = funcion_comandos(list_tokens, "grab")
        elif token == "letGo":
            respuesta = funcion_comandos(list_tokens, "letGo")
        list_tokens.remove(token)
        
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
     
def funcion_comandos(list_tokens, comando):
    respuesta = None
    parametros = extraer_parentesis(list_tokens, comando)
    for caracter in parametros:
        if caracter not in parametros_comandos:
            respuesta = False
            break
    return respuesta

def creacion_variables(nombre_variable, valor_variable):
    variables_creadas[0].append(nombre_variable)
    variables_creadas[1].append(valor_variable)

def condicional_if(list_tokens):
    respuesta = None
    if list_tokens[1] in operadores:
        interior_if = extraer_parentesis(list_tokens, list_tokens[1])
        interior_comando = extraer_parentesis(interior_if, interior_if[0])
        for i in interior_comando:
            if i not in parametros_comandos:
               respuesta = False
    else:
        respuesta = False
    return respuesta    

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
            

                

