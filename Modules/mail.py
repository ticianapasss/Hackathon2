
def listarThreads(service):
    results = service.messages().list(userId='me').execute()
    messages = results.get('messages', [])

    if not messages:
        print("no se encontraron hilos de correo electrónico.")
    else:
        print("Buscando Hilos:")

    return messages

def obtenerUltimosMails(cantEmails, service):
    threads = listarThreads(service)
    mensajes = []
    #temporal hasta saber como limitar la busqueda
    count = 0
    for thread in threads:
        if(count == 3):
            break
        mensajes.append(obtenerMensajes(thread, service))
        count =+ 1
    return mensajes

def obtenerMensajes(thread, service):
    results = service.threads().get(userId='me', id=thread["id"]).execute()
    messages = results.get('messages', [])

    if not messages:
        print("no se encontraron mensajes en los hilos.")

    Froms = []
    count = 0
    for message in messages:
        if(count == 10):
            break
        headers = message['payload']['headers']
        for header in headers:
            if(header['name'] == "From"):
                Froms.append(header['value'])
        count =+ 1
    return Froms



