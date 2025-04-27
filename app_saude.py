import customtkinter as ctk

ctk.set_appearance_mode('dark') #mudar a cor da janela dark(escuro) 

#criar interface    #largura=1920px altura=1080 tela cheia(padrão)
#=================================JANELA PRINCIPAL============================================
janela = ctk.CTk() #criar uma janela
janela.geometry('500x550') #determina o tamanho
janela.title('Aplicativo Saúde') #altera o nome da janela
janela.iconbitmap('heartrate_86852.ico') #altera o icone da janela (site https://icon-icons.com/)
#==============================================================================================


#=================================Titulo da Janela ============================================
#objetos importantes precisam estar numa variavel
#criar primeiro titulo da janela(não precisa de variavel)
ctk.CTkLabel(janela,
             text='Aplicativo Saúde',
             text_color='#c1f7ba', #escolher cor através do color picker
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
                     placeholder_text='Digite o seu nome')   #criar texto em marca d'agua
nome.pack(pady=15) #inicializa o componente com variavel #pady = 10 (dá um espaçamento entre o titulo e a tela)
#==============================================================================================

#=================================CADASTRO ALTURA ============================================
#é preciso criar uma variavel
altura = ctk.CTkEntry(janela,    #CTkEntry(cria caixas)
                     width=450, # largura
                     height=40, #altura
                     border_color='#e3f2e1', #borda
                     fg_color='#f2f2f2', #cor de fundo da caixa             
                     placeholder_text='Digite a sua altura')   #criar texto em marca d'agua
altura.pack(pady=15) #inicializa o componente com variavel #pady = 10 (dá um espaçamento entre o titulo e a tela)
#==============================================================================================

#=================================CADASTRO PESO ============================================
#é preciso criar uma variavel
peso = ctk.CTkEntry(janela,    #CTkEntry(cria caixas)
                     width=450, # largura
                     height=40, #altura
                     border_color='#e3f2e1', #borda
                     fg_color='#f2f2f2', #cor de fundo da caixa  
                     placeholder_text='Digite o seu peso')   #criar texto em marca d'agua
peso.pack(pady=18) #inicializa o componente com variavel #pady = 10 (dá um espaçamento entre o titulo e a tela)
#==============================================================================================


#================================= BOTÃO CALCULAR ============================================
botao_calcular = ctk.CTkButton(janela, #CTkButton - cria o botão 
                      text='Calcular', #texto do botão
                      width=120,
                      height=70,
                      fg_color='darkgreen', #a cor do botão 
                      hover_color='#e3f2e1', #a cor do botão quando o mouse passa por cima  
                      cursor='Heart', #transforma o botão em um coração(pra dizer que aquela area é clicavél)  
                      text_color='black', #cor do texto
                      font= ('Helvetica',20, 'bold'))#fonte do texto    
botao_calcular.pack(side="left", padx=100, pady=10) #inicializa o componente com variavel #pady = 10 (dá um espaçamento entre o titulo e a tela)
#==============================================================================================


#================================= BOTÃO LIMPAR ============================================
botao_limpar = ctk.CTkButton(janela, #CTkButton - cria o botão 
                      text='Limpar', #texto do botão
                      width=120, #largura
                      height=70, #altura
                      fg_color='darkred', #a cor do botão 
                      hover_color='#e3f2e1', #a cor do botão quando o mouse passa por cima  
                      cursor='Heart', #transforma o botão em um coração(pra dizer que aquela area é clicavél)  
                      text_color='black', #cor do texto
                      font= ('Helvetica',20, 'bold'))#fonte do texto   
botao_limpar.pack(side="left", padx=10, pady=10) #inicializa o componente com variavel #pady = 10 (dá um espaçamento entre o titulo e a tela)
#==============================================================================================



janela.mainloop() #rodar o sistema