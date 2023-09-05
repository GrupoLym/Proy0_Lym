
import re
from pathlib import Path

palabras_clave = ["defVar", "drop", "letGo", "walk", "leap", "turn",
                  "turnto", "get", "grab", "nop", "jump", "defProc"]

caracteres_usados = ["(", ")", "{", "}", ";", ":", "," , "="]

operadores = ["if", "else", "can", "facing", "not", "while", "whilecan"]

parametros_comandos = ["1","2","3","4","5","6","7","8","front","left","right","back",
                    "north","south","west","east", ",", "around"]

global variables_creadas
variables_creadas =  [[],
                     []]
global procesos_creados
procesos_creados = [[],
                    []]
list_tokens = None

lista_posibles_escritos = [palabras_clave, caracteres_usados, operadores, parametros_comandos]

def create_tokens(archivo):
    path = Path(archivo)
    with path.open('r') as file:
        text = file.read()
        global list_tokens
        list_tokens = re.findall(r'\w+|\S', text)

"""esta funcion recorre la lista de tokens y la compar con las listas de caracteres que tenemos arriba, si hay algo
que no deberia estar, retorna false y el programa está mal escrito"""

def analizador():
    respuesta = None #acá quiero que si la respuesta al final sigue siendo NONE, signifique que el programa esta bien escrito
    corrector_sintax = corrector_sintaxis_parametros()
    if corrector_sintax == False:
        return False
    return respuesta

"""acá creé una funcion que recibe la lista de todos los tokens y la funcion(jump, walk, turn, etc) y saca los tokens
que esten al interior de los parentesis"""

def corrector_sintaxis_parametros():
    respuesta = None
    cant_abrir_parentesis = list_tokens.count("(")
    cant_cerrar_parentesis = list_tokens.count(")")
    cant_abrir_corchetes = list_tokens.count("{")
    cant_cerrar_corchetes = list_tokens.count("}")
    if cant_abrir_corchetes != cant_cerrar_corchetes or cant_abrir_parentesis != cant_cerrar_parentesis:
        respuesta = False
    
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
        if token == "defProc":
            respuesta = definir_procesos()
            
        for listas_caracteres in lista_posibles_escritos:
            if token in listas_caracteres or token in variables_creadas[0] or token in variables_creadas[1]:
                existe = True
                break
            if token in procesos_creados[0] or token in procesos_creados[1]:
                existe = True
                break
        if existe == False:
            return False
        
        if token == "if":
            respuesta = condicional_if()
        elif token == "while":
            respuesta = ciclo_while()
        elif token == "jump":
            respuesta = funcion_comandos("jump")
        elif token == "walk":
            respuesta = funcion_comandos("walk")
        elif token == "leap":
            respuesta = funcion_comandos("leap")
        elif token == "turn":
            respuesta = funcion_comandos("turn")
        elif token == "turnto":
            respuesta = funcion_comandos("turnto")
        elif token == "drop":
            respuesta = funcion_comandos("drop")
        elif token == "get":
            respuesta = funcion_comandos("get")
        elif token == "grab":
            respuesta = funcion_comandos("grab")
        elif token == "letGo":
            respuesta = funcion_comandos("letGo")
        else:
            if token in procesos_creados[0]:
                respuesta = check_proceso(token)
                
                    
        list_tokens.remove(token)
        
    return respuesta
 

def extraer_parentesis(funcion):
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

def extraer_parentesis_funciones(list, funcion):
    interior_parentesis = []
    switch = False

    for token in list:
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

def extraer_corchetes_procesos(list):
    interior_corchetes = []
    switch = False

    for token in list:
        if token == "{":
            switch = True
        elif switch:
            if token == "{":
                continue  # Ignorar el paréntesis de apertura
            elif token == "}":
                break  # Salir cuando se encuentre el paréntesis de cierre
            else:
                interior_corchetes.append(token)

    return interior_corchetes

def funcion_comandos(comando):
    respuesta = None
    parametros = extraer_parentesis(comando)
    for caracter in parametros:
        if caracter not in parametros_comandos and caracter not in variables_creadas[0] and caracter not in variables_creadas[1] and caracter not in procesos_creados[0] and caracter not in procesos_creados[1]:
            respuesta = False
                
    return respuesta

def creacion_variables(nombre_variable, valor_variable):
    variables_creadas[0].append(nombre_variable)
    variables_creadas[1].append(valor_variable)

def condicional_if(): #Lista de token que comienza con un if y sigue 
    respuesta = None
    if list_tokens[1] in operadores:
        interior_if = extraer_parentesis_funciones(list_tokens, list_tokens[1])
        interior_comando = extraer_parentesis_funciones(interior_if, interior_if[0])
        for i in interior_comando:
            if i not in parametros_comandos:
               respuesta = False 
        acciones = extraer_corchetes_procesos(list_tokens)
        ciclo = 0
        while respuesta == None and ciclo < len(acciones):
            i = acciones[ciclo]
            if i == "jump":
               respuesta = funcion_comandos("jump")
            elif i == "walk":
                respuesta = funcion_comandos("walk")
            elif i == "leap":
                respuesta = funcion_comandos("leap")
            elif i == "turn":
                respuesta = funcion_comandos("turn")
            elif i == "turnto":
                respuesta = funcion_comandos("turnto")
            elif i == "drop":
                respuesta = funcion_comandos("drop")
            elif i == "get":
                respuesta = funcion_comandos("get")
            elif i == "grab":
                respuesta = funcion_comandos("grab")
            elif i == "letGo":
                respuesta = funcion_comandos("letGo")
            ciclo += 1
    else:
        respuesta = False
        
    return respuesta  

def ciclo_while():
    respuesta = None
    if list_tokens[1] in operadores:
        interior_if = extraer_parentesis_funciones(list_tokens, list_tokens[1])
        interior_comando = extraer_parentesis_funciones(interior_if, interior_if[0])
        for i in interior_comando:
            if i not in parametros_comandos:
               respuesta = False 
        acciones = extraer_corchetes_procesos(list_tokens)
        ciclo = 0
        while respuesta == None and ciclo < len(acciones):
            i = acciones[ciclo]
            if i == "jump":
               respuesta = funcion_comandos("jump")
            elif i == "walk":
                respuesta = funcion_comandos("walk")
            elif i == "leap":
                respuesta = funcion_comandos("leap")
            elif i == "turn":
                respuesta = funcion_comandos("turn")
            elif i == "turnto":
                respuesta = funcion_comandos("turnto")
            elif i == "drop":
                respuesta = funcion_comandos("drop")
            elif i == "get":
                respuesta = funcion_comandos("get")
            elif i == "grab":
                respuesta = funcion_comandos("grab")
            elif i == "letGo":
                respuesta = funcion_comandos("letGo")
            ciclo += 1
    else:
        respuesta = False
    return respuesta

def definir_procesos(): 
    respuesta = None
    procesos_creados[0].append(list_tokens[1])
    variables_proc = extraer_parentesis_funciones(list_tokens, list_tokens[1])
    if "," in variables_proc:
        variables_proc.remove(",")
    for variable in variables_proc:
        procesos_creados[1].append(variable)
    interior_proceso = extraer_corchetes_procesos(list_tokens)
    ciclo = 0
    while respuesta == None and ciclo < len(interior_proceso):
        i = interior_proceso[ciclo]
        if i == "jump":
            respuesta = funcion_comandos("jump")
        elif i == "walk":
            respuesta = funcion_comandos("walk")
        elif i == "leap":
            respuesta = funcion_comandos("leap")
        elif i == "turn":
            respuesta = funcion_comandos("turn")
        elif i == "turnto":
            respuesta = funcion_comandos("turnto")
        elif i == "drop":
            respuesta = funcion_comandos("drop")
        elif i == "get":
            respuesta = funcion_comandos("get")
        elif i == "grab":
            respuesta = funcion_comandos("grab")
        elif i == "letGo":
            respuesta = funcion_comandos("letGo")
        ciclo += 1
    return respuesta

def check_proceso(nombre_proceso):
    respuesta = None
    if nombre_proceso not in procesos_creados[0]:
        respuesta = False
    else:
        respuesta = check_parametros_proceso(nombre_proceso)
    return respuesta

def check_parametros_proceso(nombre_proceso):
    respuesta = None
    parametros = extraer_parentesis(nombre_proceso)
    for value in parametros:
        if value not in parametros_comandos and value not in procesos_creados[1]:
            respuesta = False
    return respuesta

#no entiendo que hizo de acá para abajo

def parametro_x_palabra (palabra):
    if palabra == "jump":
        return parametros_comandos
    elif palabra == "walk":
        return parametros_comandos
    elif palabra == "leap":
        return parametros_comandos
    elif palabra == "turn":
        return parametros_comandos
    elif palabra == "turnto":
        return parametros_comandos
    elif palabra == "drop":
        return parametros_comandos
    elif palabra == "get":
        return parametros_comandos
    elif palabra == "grab":
        return parametros_comandos
    elif palabra == "letGo":
        return parametros_comandos
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
            

                

