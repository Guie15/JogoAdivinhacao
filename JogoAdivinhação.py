from time import sleep
from random import randint
from line import linha
from emoji import emojize



comp = randint(0, 10) #intervalo de Número que o computador pode "pensar"

linha()
print(emojize('\033[1;33m Adivinhe o Número que eu pensei... :wink: \033[m', use_aliases = True))
linha()

acertou = False
tentativas = 0

while not acertou:
   jogador = int(input('\033[1;33m Qual é  o seu palpite?: \033[m'))
   tentativas += 1
   if jogador == comp:
     break
   else:
      if jogador > comp:
         print(' \033[1;34m  Menos... tente novamente!\033[m') 
      if jogador < comp:
         print(' \033[1;34m  Mais... tente novamente!\033[m')
        
        
linha()
print('\033[1;92m PROCESSANDO... \033[m')
sleep(2)
linha()
print(emojize('\033[1;33m VOCÊ GANHOU DE MIM!!! :white_check_mark: \033[m', use_aliases=True))
print(f'\033[1;90m Com {tentativas} tentativas \033[m')
        