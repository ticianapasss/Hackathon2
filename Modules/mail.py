
def obtenerMensaje ():

    results = service.users().threads().list(userId='me').execute()
    threads = results.get('threads', [])

    if not threads:
        print("no se encontraron hilosd e correo electrónico.")
    else:
        print("Hilos de correo electónico encontrados:")

    for thread in threads: 
        print(f"ID del hilo: {thread['id']}")

    return  




