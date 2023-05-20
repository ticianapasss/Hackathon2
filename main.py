from Modules import auth, mail, ai, terminal, db

servicioMail = auth.authenticate()
mails = mail.obtenerUltimosMails(10,servicioMail)
for mail in mails:
    if(not db.mailYaBloqueado(mail)):
        deberiaBloquearse = ai.analyze(mail)
        if(deberiaBloquearse):
            terminal.mostrarMailComprometidos(mail)
            db.guardarEnBlacklist(mail)
    else:
        terminal.mostrarMailComprometidos(mail)