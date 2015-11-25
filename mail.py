#!/usr/bin/env python
# -*- encoding: utf-8 -*-
 
import poplib
 
usuario = "********"
senha =  "*******"
 
try:
    M = poplib.POP3_SSL('pop3.live.com', 995) # Porta padrão do POP3 é 110, com uso de SSL (POP3_SSL) a padrão é 995
    print M.user(usuario)
except:
      print 'Erro ao Conectar'
 
try:
    pwmsg = M.pass_(senha)
    print pwmsg
    if pwmsg[0:3] == '+OK':
        print "Conta válida"
    M.quit()
except:
    print 'Conta Inválida:', usuario
