#Criado dia 04/08/2022
#Created day 04/08/2022

from random import shuffle

caracteres = [1,2,3,4,5,6,7,8,9,0,'!','@','/','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','*',]

shuffle(caracteres)
while True:
    tamanhoSenha = input('Deseja senha media ou longa? (digite "media" ou "longa") ')

    if tamanhoSenha == 'media':
        senha = caracteres[0:9]
        print('\nSUA SENHA:')
        for i in senha:
            print(i,end='')
        break

    elif tamanhoSenha == 'longa':
        senha = caracteres[0:14]
        print('\nSUA SENHA:')
        for i in senha:
            print(i,end='')
            
        break

    else:
        print('Informe um dos tamanhos de senha.')

        
        













