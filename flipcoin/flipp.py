from time import sleep
from random import choice

def flip():
    coin = ['cara', 'coroa']
    comp = choice(coin)
    
    player = ' '
    print('escolha entre cara ou coroa')
    
    while player not in 'caracoroa':
        player = input(' >>> ')
        
        if player == 'cara' or player == 'coroa':
            print('|')
            sleep(1)
            print('/')
            sleep(1)
            print('—')
            sleep(1)
            print('\ ')
            sleep(1)
            print('|')
            sleep(1)
            print('/')
            sleep(1)
            print('—')
            sleep(1)            
            print(comp)    
        

def confirm():
    resp = ' '
    
    while True:
        while resp not in 'SN':
            print('\ndeseja continuar jogando? [S/N]')
            resp = input(' >>> ').strip().upper()[0]
            
            if resp == 'S':
                flip()
                confirm()
                
            else:
                if resp == 'N':
                    print('Obrigado por jogar! Até mais...')
                    break
        sleep(3)
        break
            
        