import time
import pyautogui

#depedencias antes de rodar o codigo
print('''TABELA DO TEMPO DE INCIAR O PROGAMA
1 a 59(Segundos normais)
60(segundos)   e 1(minutos)
300(segundos)  e 5(minutos)
600(segundos)  e 10(minutos)
900(sengundos) e 15(minutos)
1800(segundos) e 30(minutos)
3600(segundos) e 1(hora)
''')
tempo = int(input('Digite o Tempo Que Quer Para o Progama Iniciar:'))
descrepiton = input('Digite Algo Para a Descrição Do Trabalho:')
work = input('Digite Nome Da Pessoa que Ira Receber o Trabalho:')
#iniciar
time.sleep(tempo)
#abrir pastas
pyautogui.hotkey('win','r')
pyautogui.press('backspace')
pyautogui.write('Documents')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=730, y=334)
pyautogui.press('enter')
#escolher arquivos
time.sleep(3)
pyautogui.click(x=428, y=284)
#mandar o arquivo para pessoa no discord
pyautogui.hotkey('ctrl','c')
pyautogui.sleep(2)
pyautogui.hotkey('win','r')
pyautogui.press('backspace')
pyautogui.write('https://www.google.com.br/')
pyautogui.press('enter')
time.sleep(15)
#discord
pyautogui.click(x=401, y=63)
pyautogui.press('backspace')
pyautogui.write('https://discord.com/channels/@me')
pyautogui.press('enter')
time.sleep(30)
pyautogui.click(x=224, y=208)
time.sleep(2)
pyautogui.write(f'{work}')
time.sleep(2)
pyautogui.press('enter')
#mandar para pessoa 
time.sleep(4)
pyautogui.click(x=538, y=697)
time.sleep(2)
pyautogui.hotkey('ctrl','v')
#Descrição do trabalho ou da  imagem 
time.sleep(2)
pyautogui.write(f'{descrepiton}')
time.sleep(3)
pyautogui.press('enter')
#Encerar o codigo
time.sleep(5)
pyautogui.hotkey('win','d')


