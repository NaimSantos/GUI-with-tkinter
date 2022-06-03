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


# Strings do Tkinter

textolabel = Tkntr.StringVar()
textolabel.set("Novo TEXTO")

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
                    width = 20,
                    anchor='center')
label_3= Tkntr.Label(menu_inicial,
                    textvariable=textolabel,
                    bg="orange",
                    font = "Times 30",
                    bd=1,
                    relief= "solid",
                    width = 15,
                    height=2,
                    anchor='nw')
label_4= Tkntr.Label(menu_inicial,
                    text="Label Numero 4",
                    bg="blue",
                    font = "Arial 10",
                    bd=1,
                    relief= "raised",
                    width = 15,
                    height=3,
                    anchor='nw',
                    padx=50)
label_5= Tkntr.Label(menu_inicial,
                    text="Label Numero 4\nEste eh um texto original\nCom multiplas linhas",
                    bg="gray",
                    font = "Arial 15",
                    bd=3,
                    relief= "raised",
                    width=60,
                    height=4,
                    anchor="w",
                    justify="left")
label_6= Tkntr.Label(menu_inicial)
label_6['text'] = "Label Numero 5"
label_6['bg'] = "pink"
label_6['relief'] = "raised"
label_6['bd']=3

# for item in label_6.keys():
#    print(item, ": ", label_6[item])

#height:  altura em funçao do numero de 'linhas' disponiveis para o text
#anchor: posicao do text (nao e alinhamento)
#padx : deslocamento do text em x (em pixels)
#pady : deslocamento do text em y (em pixels)


# Comandos
def OnClick_FileButton():
    print("Botao File Clicado")
def OnClick_SettingsButton():
    print("Botao Settings Clicado")
def OnClick_ToolsButton():
    print("Botao Tools Clicado")   
# Botoes
btn_File = Tkntr.Button(menu_inicial,
                        text= "File",
                        command=lambda: OnClick_FileButton(),
                        bg="gray",
                        borderwidth=1,
                        relief="raised")
btn_Settings = Tkntr.Button(menu_inicial,
                            text= "Settings",
                            bg="gray",
                            command=lambda: OnClick_SettingsButton(),
                            borderwidth=1,
                            relief="raised")
btn_Tools = Tkntr.Button(menu_inicial,
                        text= "Tools",
                        bg="gray",
                        command=lambda: OnClick_ToolsButton(),
                        borderwidth=1,
                        relief="raised")
btn_BotaoExtra1 = Tkntr.Button(menu_inicial,
                        text= "BotaoExtra 1",
                        bg="gray",
                        borderwidth=1,
                        relief="raised")
btn_BotaoExtra2 = Tkntr.Button(menu_inicial,
                        text= "BotaoExtra 2",
                        bg="gray",
                        borderwidth=1,
                        relief="raised")
btn_BotaoExtra3 = Tkntr.Button(menu_inicial,
                        text= "BotaoExtra 3",
                        bg="gray",
                        borderwidth=2,
                        relief="raised")
                        
label_user = Tkntr.Label(menu_inicial, text= "Usuario")
label_password = Tkntr.Label(menu_inicial, text= "Senha")

textbox_user =Tkntr.Entry(menu_inicial)
textbox_password =Tkntr.Entry(menu_inicial)
btn_Login= Tkntr.Button(menu_inicial, text= "Login")
# Grids
btn_File.grid(row=0, column=0)
btn_Settings.grid(row=0, column=1)
btn_Tools.grid(row=0, column=2)
btn_BotaoExtra1.grid(row=0, column=3)
btn_BotaoExtra2.grid(row=0, column=4)
btn_BotaoExtra3.grid(row=0, column=5)
label_user.grid(row=1, column=0, sticky="w")
label_password.grid(row=2, column=0, sticky="w")
textbox_user.grid(row=1, column=1)
textbox_password.grid(row=2, column=1)
btn_Login.grid(row=3, column=3)





# Packs (gera os botoes no layout)
#btn_File.pack()
#btn_Settings.pack()
#btn_Tools.pack()
#label_1.pack()
#label_2.pack()
#label_3.pack()
#label_4.pack()
#label_5.pack()
#label_6.pack()

menu_inicial.mainloop()