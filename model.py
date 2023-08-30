
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


def palabras_clave (palabras_clave, palabra):
    for palabra in palabras_clave:
        if palabra not in palabras_clave:
            return False

#def palabra_parametro (palabras_clave, parametro, palabra):
    #if palabra in palabras_clave:
        #while parametro == 