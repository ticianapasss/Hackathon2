def guardarEnBlacklist(mails):
    archivo = open(r"blacklist.txt","w")
    archivo.writeLines(mails)

def mailYaBloqueado(mail):
    archivo = open(r"blacklist.txt","r")
    lineas = archivo.readlines()
    for linea in lineas:
        if(mail == linea):
            return True
    return False