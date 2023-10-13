import locale
from tkinter import *
from time import strftime
from locale import setlocale
import os


def atualizar_relogio():
    """
    Atualiza o relógio digital com o horário e data atual no formato brasileiro ou internacional
    :return:
    """
    if x.get() == 0:  # Acessa a variável que armazena o valor do botão rádio selecionado
        setlocale(locale.LC_TIME, 'pt_BR')  # Define a localização para PT-BR, traduzindo mês e dia para português
        horario_atual = strftime("%H:%M:%S")  # Acessa o horário atual do usuário no formato Hora(24):Minuto:Segundo
        data_atual = strftime("%d de %B %Y, %A")  # Acessa o data atual do usuário no formato "Dia de Mês Ano,
        # dia da semana"
    else:
        setlocale(locale.LC_TIME, 'en_US')  # Define a localização para PT-BR, traduzindo mês e dia para inglês (padrão)
        horario_atual = strftime("%I:%M:%S %p")  # Acessa o horário atual do usuário no formato Hora(12):Minuto:Segundo
        data_atual = strftime("%B %d %Y, %A")  # Acessa o data atual do usuário no formato "Mês Dia Ano, dia da semana"

    label_data.config(text=data_atual)  # Define o texto da label data como o data atual (str data_atual)

    label_horario.config(text=horario_atual)  # Define o texto da label relogio como o horário atual (str horario_atual)
    label_horario.after(1000, atualizar_relogio)  # Atualiza o relógio a cada 1000ms (1seg), parando a função anterior
    # e começando uma nova


window = Tk()  # Cria uma nova janela
window.config(bg="black")  # Define background da tela para a cor preta

icon = PhotoImage(file=os.path.join("./assets/icon.png"))  # Converte a imagem para um PhotoImage
# os.path evita o uso de "\" para acessar diretório, assim evitando erro em sistemas linux

window.title("Relógio Digital")  # Define o título da janela(window)
window.iconphoto(True, icon)  # Define o icon como icone da janela
window.resizable(False, False)  # Não permite alteração do tamanho da janela

label_horario = Label(window,  # Cria uma label do horário pertecente à janela window
                      font=("DS-Digital", 60),  # Fonte e tamanho do texto
                      bg="black",  # Cor de fundo preta
                      fg="#00FF00",  # Cor do texto (relógio) verde (em hexadecimal)
                      padx=20,  # Espaço interno entre o texto e a borda no eixo x
                      pady=10)  # Espaço interno entre o texto e a borda no eixo y
label_horario.pack(anchor="center")  # Centraliza o relógio (não muito necessário existindo apenas esse elemento e se a
# janela não pode ter seu tamanho alterado

label_data = Label(window,  # Cria uma label da data pertecente à janela window
                   font=("DS-Digital", 40),  # Fonte e tamanho do texto
                   bg="black",  # Cor de fundo preta
                   fg="#00FF00",  # Cor do texto verde (em hexadecimal)
                   padx=20,  # Espaço interno entre o texto e a borda no eixo x
                   pady=10)  # Espaço interno entre o texto e a borda no eixo y
label_data.pack()

label_configuracao = Label(window, bg="black")  # Cria uma label da data pertecente à janela window com background preto
label_configuracao.pack()

horas_list = ["24HRS", "12AM/PM"]  # Lista de opções de formatação do horário

x = IntVar()  # Variável responsável pelo vínculo dos botões rádio (radio_horas)
for i in range(len(horas_list)):
    radio_horas = Radiobutton(label_configuracao,  # Define que os botões seram da label label_configuracao
                              text=horas_list[i],  # Adiciona texto ao botão
                              variable=x,  # Define variável responsável pelo vínculo do botão
                              value=i,  # Define valor do botão
                              indicatoron=False,  # remove circulo do botão para fazer ele ser clicável por completo
                              font=("DS-Digital", 20),  # Fonte e tamanho do texto
                              fg="#00FF00",  # Cor do texto verde (em hexadecimal)
                              bg="black",  # Cor de fundo preta
                              padx=20,  # Espaço interno entre o texto e a borda no eixo x
                              pady=10)  # Espaço interno entre o texto e a borda no eixo y
    radio_horas.grid(row=0, column=i)  # Invoca o botão utilizando a organização de grid, para que os botões fiquem
    # lado a lado

atualizar_relogio()  # Chama a função que atualiza o relógio para dar início a contagem

window.mainloop()
