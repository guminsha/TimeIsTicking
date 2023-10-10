from tkinter import *
from time import strftime


def atualizar_relogio():
    """
    Atualiza o relógio digital com o horário atual
    :return:
    """
    horario_atual = strftime("%H:%M:%S")  # Acessa o horário atual do usuário no formato Hora:Minuto:Segundo
    label_relogio.config(text=horario_atual)  # Define o texto da label como o horário atual (str horario_atual)
    label_relogio.after(1000, atualizar_relogio)  # Atualiza o relógio a cada 1000ms (1seg)


window = Tk()  # Cria uma nova janela

icon = PhotoImage(file="src\\icon.png")  # Converte a imagem para um PhotoImage

window.title("Relógio Digital")  # Define o título da janela(window)
window.iconphoto(True, icon)  # Define o icon como icone da janela
window.resizable(False, False)  # Não permite alteração do tamanho da janela

label_relogio = Label(window,  # Cria uma label pertecente à janela window
                      font=("DS-Digital", 60),  # Fonte e tamanho do texto
                      bg="black",  # Cor de fundo preta
                      fg="#00FF00",  # Cor do texto (relógio) verde (em hexadecimal)
                      padx=20,  # Espaço interno entre o texto e a borda no eixo x
                      pady=10)  # Espaço interno entre o texto e a borda no eixo y
label_relogio.pack(anchor="center")  # Centraliza o relógio (não muito necessário existindo apenas esse elemento e se a
# janela não pode ter seu tamanho alterado

atualizar_relogio()  # Chama a função que atualiza o relógio para dar início a contagem

window.mainloop()
