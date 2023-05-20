from Modules import auth, mail, ai, terminal, db

servicioMail = auth.authenticate()
mensajes = mail.obtenerMensajes(servicioMail)

#ejemplo de uso
#mensajesComprometidos = ai.analyze(mensajes)
#db.guardarEnBlacklist(mensajesComprometidos)
#terminal.mostrar(mensajesComprometidos)
