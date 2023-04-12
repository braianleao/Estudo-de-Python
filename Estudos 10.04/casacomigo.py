#Importando a biblioteca tkinter e o módulo random

import tkinter as tk
import random 

# Criação da interface gráfica e definindo o tamanho dela

root = tk.Tk()
root.geometry('200x200')

# define a função hover, que é chamada quando o mouse passa pelo botão "Não"

def hover (event):
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    
    nao.place(x=x, y=y)
    
    
# define a mensagem que é chamada quando clica no botão "Sim"
    
def mensagem():
    message = tk.Label(root, text='Te amo pra S2')
    message.place(x=70, y=120, relx=0, rely=0)
    
#   Cria o rótulo com o texto "Qur casar comigo e posiciona o rótulo na parte superior da janela, em um espaço de 20px" 
    
pergunta = tk.Label(root, text='Quer casar comigo?')
pergunta.pack(anchor='n', padx=20,)

# Cria, posiciona e aciona a função "Hover" ao passar o mouse pelo botão "Não"

nao = tk.Button(root, text="Não")
nao.place(x=140, y=80)
nao.bind ('<Enter>', hover)

#Cria e posiciona o botão "Sim"

sim = tk.Button(root, text='Sim')
sim.place(x=25, y=80, relx=0, rely=0)

#Inicia o Loop da interface gráfica

root.mainloop()