#!/usr/bin/env python

import sys, os
try:
    import pipe
except ImportError:
    print "Fora do sistema da atomo."

namePlataform = sys.platform

if namePlataform == "linux2":
    print namePlataform
    if namePlataform == "win32":
        print namePlataform
else:
    print namePlataform

info = os.uname()
entrada = sys.argv

def shutdown():

    print ''' Encarregado de desliga o sistema '''

    if entrada[1] == 'shut':
        os.system('shutdown -h now')
    else:
        print 'Comando (shut), argumando passado invalido!'

def killProcess():

    ''' comandos para eliminar todos os programas que estao rodando no momento.
        pkill -9 nome-do-programa
        killall -9 -1, mata todos os processos que seu usuario tem permissao
        kill
        kill -9 $(pidof nome_programa)
        xkill

    '''
    
    if entrada[1] == 'all':
        os.system('killall -9 -1')

    nameProgram = 'pgrep -l %s' % (entrada[1])
    kill        = 'pkill -9 %s' % (entrada[1])
    programos_mortos = os.popen(nameProgram).readlines()
    for i in programos_mortos:
        print '-> ' + i
    os.system(kill)

def recuperar():
    # Recupera barra superior do fedora.
    com = 'gconftool-2 --recursive-unset /apps/panel'
    rem = 'rm -rf ~/.gconf/apps/panel'
    pki = 'pkill gnome-panel'

# killProcess()
