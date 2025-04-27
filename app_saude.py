import customtkinter as ctk

#auto-py-to-exe (transforma python em executavel)
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNÇÃO CALCULAR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def imc():
    n = nome.get() #get é o comando que puxa o que tem na caixa, vem como texto(input)
    p = int(peso.get())
    a = float(altura.get().replace(',','.')) #replace(toda vez q digitar a ',' subistitua por '.')
    
    imc = p/(a**2)
    

    if (imc <= 18.5):
        situacao = 'Baixo peso'
    elif (imc >= 18.5 and imc < 25):
        situacao = 'Parabéns!, Peso ideal'
    elif (imc >=25 and imc <30):
        situacao = 'Sobrepeso'
    else:
        situacao = 'Obeso'
    
    resultado.configure (
        text=f'Olá {n}, \nSeu IMC está em {imc:.1f}. \nSituação: {situacao}'
        ) #'configure' que dizer altere /configura
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNÇÃO LIMPAR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def limpar():
    nome.delete(0,'end')
    peso.delete(0,'end')
    altura.delete(0,'end')
    resultado.configure(text='')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ctk.set_appearance_mode('dark') #mudar a cor da janela dark(escuro) 

#criar interface    #largura=1920px altura=1080 tela cheia(padrão)
#=================================JANELA PRINCIPAL============================================
janela = ctk.CTk() #criar uma janela
janela.geometry('500x550') #determina o tamanho
janela.resizable(False,False)#travar o tamanho da janela
janela.title('Aplicativo Saúde') #altera o nome da janela
janela.iconbitmap('heartrate_86852.ico') #altera o icone da janela (site https://icon-icons.com/)
#==============================================================================================


#=================================Titulo da Janela ============================================
#objetos importantes precisam estar numa variavel
#criar primeiro titulo da janela(não precisa de variavel)
ctk.CTkLabel(janela,
             text='Aplicativo Saúde',
             text_color='#c1f7ba', #Cor da letra (escolher cor através do color picker)
             font=('Helvetica', 30, 'bold') #tipo da letra, tamanho, deixar a letra mais intensa(negrito)
             ).pack(pady=15) #inicializa o componente  #pady = 10 (dá um espaçamento entre o titulo e a tela)
#==============================================================================================



#=================================CADASTRO NOME ============================================
#é preciso criar uma variavel
nome = ctk.CTkEntry(janela,    #CTkEntry(cria caixas)
                     width=450, # largura
                     height=40, #altura
                     border_color='#e3f2e1', #borda
                     fg_color='#f2f2f2', #cor de fundo da caixa  
                     placeholder_text='Digite o seu nome',   #criar texto em marca d'agua
                     text_color='black') #Cor da letra quando usuario digitar (escolher cor através do color picker)
nome.pack(pady=15) #inicializa o componente com variavel #pady = 10 (dá um espaçamento entre o titulo e a tela)
#==============================================================================================

#=================================CADASTRO ALTURA ============================================
#é preciso criar uma variavel
altura = ctk.CTkEntry(janela,    #CTkEntry(cria caixas)
                     width=450, # largura
                     height=40, #altura
                     border_color='#e3f2e1', #borda
                     fg_color='#f2f2f2', #cor de fundo da caixa             
                     placeholder_text='Digite a sua altura',   #criar texto em marca d'agua
                     text_color='black') #Cor da letra quando usuario digitar (escolher cor através do color picker)
altura.pack(pady=15) #inicializa o componente com variavel #pady = 10 (dá um espaçamento entre o titulo e a tela)
#==============================================================================================

#=================================CADASTRO PESO ============================================
#é preciso criar uma variavel
peso = ctk.CTkEntry(janela,    #CTkEntry(cria caixas)
                     width=450, # largura
                     height=40, #altura
                     border_color='#e3f2e1', #borda
                     fg_color='#f2f2f2', #cor de fundo da caixa  
                     placeholder_text='Digite o seu peso',   #criar texto em marca d'agua
                     text_color='black') #Cor da letra quando usuario digitar (escolher cor através do color picker)
peso.pack(pady=18) #inicializa o componente com variavel #pady = 10 (dá um espaçamento entre o titulo e a tela)
#==============================================================================================


#================================= BOTÃO CALCULAR ============================================
botao_calcular = ctk.CTkButton(janela, #CTkButton - cria o botão 
                      text='Calcular', #texto do botão
                      width=120,
                      height=40,
                      fg_color='darkgreen', #a cor do botão 
                      hover_color='#e3f2e1', #a cor do botão quando o mouse passa por cima  
                      cursor='Heart', #transforma o botão em um coração(pra dizer que aquela area é clicavél)  
                      text_color='black', #cor do texto
                      font= ('Calibri',20, 'bold'),#fonte do texto
                      command=imc)    
botao_calcular.place(x=100,y=300) #inicializa o componente com variavel 
               #place (coloca os botões um ao lado do outro)
#==============================================================================================


#================================= BOTÃO LIMPAR ============================================
botao_limpar = ctk.CTkButton(janela, #CTkButton - cria o botão 
                      text='Limpar', #texto do botão
                      width=120, #largura
                      height=40, #altura
                      fg_color='darkred', #a cor do botão 
                      hover_color='#e3f2e1', #a cor do botão quando o mouse passa por cima  
                      cursor='Heart', #transforma o botão em um coração(pra dizer que aquela area é clicavél)  
                      text_color='black', #cor do texto
                      font= ('Calibri',20, 'bold'),#fonte do texto
                      command=limpar)   
botao_limpar.place(x=300,y=300) #inicializa o componente com variavel 
               #place (coloca os botões um ao lado do outro)
#==============================================================================================

#=================================Resultado ============================================
#objetos importantes precisam estar numa variavel
#criar primeiro titulo da janela(não precisa de variavel)
resultado= ctk.CTkLabel(janela,
             text='',
             text_color='#c1f7ba', #escolher cor através do color picker
             font=('Helvetica', 15, )) # tipo da letra tamanho, bold= deixar a letra mais intensa(negrito)
resultado.place(x=150,y=350) #inicializa o componente com variavel 
               #place (coloca os botões um ao lado do outro)
#==============================================================================================

janela.mainloop() #rodar o sistema