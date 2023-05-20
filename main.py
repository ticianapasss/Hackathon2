from Modules import auth, mail, ai, terminal, db

servicioMail = auth.authenticate()
mails = mail.obtenerUltimosMails(10,servicioMail)

#ejemplo de uso
#mailsComprometidos = ai.analyze(mails)
#db.guardarEnBlacklist(mailsComprometidos)
#terminal.mostrarMailsComprometidos(mailsComprometidos)
