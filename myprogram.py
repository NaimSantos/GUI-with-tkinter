import tkinter as Tkntr

# Variaveis globais
largura = 800
altura = 600

#Inicializacao
menu_inicial = Tkntr.Tk()
menu_inicial.title("Meu App")

# Resolucao do sistema
LarguraSystem=menu_inicial.winfo_screenwidth()
AlturaSystem=menu_inicial.winfo_screenheight()

# Posicao da janela
posx=LarguraSystem/2 - largura/2
posy=AlturaSystem/2 - altura/2
menu_inicial.wm_geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
menu_inicial.resizable(True, True)
menu_inicial.state("normal")

# Labels
label_1=Tkntr.Label(menu_inicial,
                    text = "Este o label 1",
                    bg="yellow",
                    fg="black",
                    font="Arial 20",
                    width=20)
label_2=Tkntr.Label(menu_inicial,
                    text = "Este o label 2",
                    bg = "#FF0000",
                    fg="black",
                    font="Arial 10",
                    width = 20)

# Comandos
def OnClick_FileButton():
    print("Botao File Clicado")
def OnClick_SettingsButton():
    print("Botao Settings Clicado")
    
# Botoes
btn_file = Tkntr.Button(menu_inicial,
                        text= "File",
                        command=lambda: OnClick_FileButton(),
                        bg="green",
                        width=20,
                        borderwidth=5,
                        relief="raised")
btn_settings = Tkntr.Button(menu_inicial,
                            text= "Settings\nOptions",
                            font="Arial 20",
                            borderwidth=2,
                            relief="solid")

# Packs (gera os botoes no layout)
label_1.pack()
label_2.pack()
btn_file.pack()
btn_settings.pack()


menu_inicial.mainloop()
