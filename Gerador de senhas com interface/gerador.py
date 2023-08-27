from PySimpleGUI import PySimpleGUI as sg
from random import shuffle

caracteres = [1,2,3,4,5,6,7,8,9,0,'!','@','/','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','*','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
shuffle(caracteres)
aux = 0

sg.theme('DarkBlue14')

def principal():
    layout = [
        [sg.Text('Gerador de senhas', justification='center', size=(30, 1))],
        [sg.Button('Padrão', size=(10, 1), pad=(18)), sg.Button('Longa', size=(10, 1))],
    ]
    return sg.Window('Senhas', layout, finalize=True, size=(255, 110), icon='icon.ico')

def senha():
    layout = [
        [sg.Text('Sua senha:'),sg.Text('', key='val_senha', justification='center')],
        [sg.Button('Copiar',size=(12), pad=(5)),sg.Button("Gerar outra",size=(12),)],
        [sg.Button('Voltar',size=(12), pad=(5))],
    ]
    return sg.Window('senha', layout, finalize=True, size=(255, 110), icon='icon.ico')

janela1, janela2 = principal(), None

while True: 
    window, event, values = sg.read_all_windows()
    
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    
    if window == janela2 and event == sg.WIN_CLOSED:
        janela2.hide()
        janela1.un_hide()

    if window == janela1 and event == 'Padrão':
        aux = 0
        try:
            janela2 = senha()
        except:
            janela2.un_hide()
            
        janela1.hide()
        valores = caracteres[0:9]
        senha = ''.join(map(str, valores))            
        janela2['val_senha'].update(senha)
        
    if window == janela1 and event == 'Longa':
        aux = 1
        try:
            janela2 = senha()
        except:
            janela2.un_hide()
            
        janela1.hide()
        valores = caracteres[0:14]
        senha = ''.join(map(str, valores))            
        janela2['val_senha'].update(senha)
        
    if window == janela2 and event == 'Copiar':
        values["val_senha"] = senha
        sg.clipboard_set(senha) 
        sg.popup('Senha copiada para área de transferência!',icon='icon.ico', title='Copiar')
    
    if window == janela2 and event == 'Gerar outra':
        if aux == 0:
            shuffle(caracteres)
            valores = caracteres[0:9]
            senha = ''.join(map(str, valores))            
            janela2['val_senha'].update(senha)
        elif aux == 1:
            shuffle(caracteres)
            valores = caracteres[0:14]
            senha = ''.join(map(str, valores))            
            janela2['val_senha'].update(senha)
            
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
        

        

 