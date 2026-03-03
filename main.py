from tkinter import *
from tkinter import ttk

# será utilizado cores retirados do color piker

cor1 = "#3b3b3b"  # black/preta
cor2 = "#feffff"  # white/branca
cor3 = "#38576b"  # Azul carregado
cor4 = "#ECEFF1"  # cizenta
cor5 = '#FFAB40'  # Orange/laranja

# biblioteca necessaria para criação da calculadora.
# o "*" significa que será importado tudo que estiver na biblioteca citada.
# "ttk" é uma parte do ttk que oferece outro widget mais avançados que o tkinter.

# etapa 2 criaçao de janela para calculadora
janela = Tk()
janela.title("Calculadora") # nome
janela.geometry("235x318") #tamanho que a janela da qualculadora irá abrir
janela.config(bg=cor1) # cor da ja nela

# etapa 3 separação de display e teclado da calculadora
# a melhor opção para ser feita separação será o frames.

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_teclado = Frame(janela, width=235, height=268)
frame_teclado.grid(row=1, column=0)

# variável todos os valores

todos_valores = ''# qualquer variável adicionada nesta função, ela será mantida idependente do que for feito. ela será
# reutilizada para futuras operações.

# criando label
valor_texto = StringVar() # Essa string irá receber o valor digitado e passa_lo para o código abaixo.


# Criando função


def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

# passando valor para tela
    valor_texto.set(todos_valores)

# função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# Limpar tela

def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('yvi 18'), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)




# Criando botões

b_1 = Button(frame_teclado, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0) #o "x" representa a movimentação da esquerda para a direita e o "y"
# a movimentaçao de cima para baixo
b_2 = Button(frame_teclado, command=lambda:entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_teclado,command=lambda:entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2,font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=179, y=0) # Agora é só copiar as teclas já feitas e alterar apenas a altura da tecla no caso ela saiu de y=0 para
# y=52 que foi o tamanho ideal.
b_4 = Button(frame_teclado,command=lambda:entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_teclado,command=lambda:entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=52)
b_6 = Button(frame_teclado,command=lambda:entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=52)
b_7 = Button(frame_teclado, command=lambda:entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2,font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=179, y=52)
b_8 = Button(frame_teclado,command=lambda:entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_teclado, command=lambda:entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=104)
b_10 = Button(frame_teclado, command=lambda:entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=104)
b_11 = Button(frame_teclado, command=lambda:entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2,font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=179, y=104)
b_12 = Button(frame_teclado, command=lambda:entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_teclado, command=lambda:entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=156)
b_14 = Button(frame_teclado, command=lambda:entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=156)
b_15 = Button(frame_teclado, command=lambda:entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2,font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=179, y=156)
b_16 = Button(frame_teclado, command=lambda:entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_teclado, command=lambda:entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=208)
b_18 = Button(frame_teclado, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor2,font=('yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=179, y=208)

janela.mainloop() # necessario para executar o janela que vai ser aberta com o nome acima
# 'Calculadora'.

# etapa 3 separação de display e teclado da calculadora
# a melhor opção para ser feita separação será o frames.




