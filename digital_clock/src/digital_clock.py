import locale
from tkinter import *
from time import strftime
from locale import setlocale
import os
from TimeFormatBrazil import TimeFormatBrazil
from TimeFormatInternational import TimeFormatInternational


def update_clock():
    """
    Atualiza o relógio digital com o horário e data atual no formato brasileiro ou internacional
    :return:
    """
    setlocale(locale.LC_TIME, list_time[current_radio.get()].locale)  # Acessa a classe do rádio selecionado para
    # definir o idioma
    current_time = strftime(list_time[current_radio.get()].horario_atual)  # Acessa a classe do rádio selecionado
    # para definir a formatação do padrão do horário
    current_date = strftime(list_time[current_radio.get()].data_atual)  # Acessa a classe do rádio selecionado para
    # definir a formatação do padrão da data

    label_time.config(text=current_time)  # Define o texto da label relogio como o horário atual (str current_time)
    label_date.config(text=current_date)  # Define o texto da label data como o data atual (str current_date)

    label_time.after(1000, update_clock)  # Atualiza o relógio a cada 1000ms (1seg), parando a função anterior
    # e começando uma nova


window = Tk()  # Cria uma nova janela
window.config(bg="black")  # Define background da tela para a cor preta

icon = PhotoImage(file=os.path.join("./assets/icon.png"))  # Converte a imagem para um PhotoImage
# os.path evita o uso de "\" para acessar diretório, assim evitando erro em sistemas linux

window.title("Relógio Digital")  # Define o título da janela(window)
window.iconphoto(True, icon)  # Define o icon como icone da janela
window.resizable(False, False)  # Não permite alteração do tamanho da janela

label_time = Label(window,  # Cria uma label do horário pertecente à janela window
                   font=("DS-Digital", 60),  # Fonte e tamanho do texto
                   bg="black",  # Cor de fundo preta
                   fg="#00FF00",  # Cor do texto (relógio) verde (em hexadecimal)
                   padx=20,  # Espaço interno entre o texto e a borda no eixo x
                   pady=10)  # Espaço interno entre o texto e a borda no eixo y
label_time.pack(anchor="center")  # Centraliza o relógio (não muito necessário existindo apenas esse elemento e se a
# janela não pode ter seu tamanho alterado

label_date = Label(window,  # Cria uma label da data pertecente à janela window
                   font=("DS-Digital", 40),  # Fonte e tamanho do texto
                   bg="black",  # Cor de fundo preta
                   fg="#00FF00",  # Cor do texto verde (em hexadecimal)
                   padx=20,  # Espaço interno entre o texto e a borda no eixo x
                   pady=10)  # Espaço interno entre o texto e a borda no eixo y
label_date.pack()

label_config = Label(window, bg="black")  # Cria uma label da data pertecente à janela window com background preto
label_config.pack()

list_time = [TimeFormatBrazil(), TimeFormatInternational()]  # Lista de opções de formatação do horário

current_radio = IntVar()  # Variável responsável pelo vínculo dos botões rádio (radio_time_format)
for i in range(len(list_time)):
    radio_time_format = Radiobutton(label_config,  # Define que os botões seram da label label_configuracao
                                    text=list_time[i].text,  # Adiciona texto ao botão
                                    variable=current_radio,  # Define variável responsável pelo vínculo do botão
                                    value=i,  # Define valor do botão
                                    indicatoron=False,  # remove circulo do botão para fazer ele ser clicável
                                    font=("DS-Digital", 20),  # Fonte e tamanho do texto
                                    fg="#00FF00",  # Cor do texto verde (em hexadecimal)
                                    bg="black",  # Cor de fundo preta
                                    padx=20,  # Espaço interno entre o texto e a borda no eixo x
                                    pady=10)  # Espaço interno entre o texto e a borda no eixo y
    radio_time_format.grid(row=0, column=i)  # Invoca o botão utilizando a organização de grid, para que os botões
    # fiquem lado a lado

update_clock()  # Chama a função que atualiza o relógio para dar início a contagem

window.mainloop()
