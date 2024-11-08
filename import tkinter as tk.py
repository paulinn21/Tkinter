import tkinter as tk
from tkinter import messagebox
from tkinter import *
#Cadastro 

#criando janela no tkinter
janela = tk.Tk("Sistema de Cadastro")
janela.title("Usuário do Sistema")
janela.geometry("1000x500")


imagem = tk.PhotoImage(file="images/pequena.png")
label_for_code = tk.Label(janela, image=imagem)
label_for_code.pack()

#nome
tk.Label(janela, text="Digite seu nome:").pack(anchor = "w", pady=5)
dado_nome = tk.Entry(janela)
dado_nome.pack(anchor = "w" )

#cpf
tk.Label(janela, text="Digite seu CPF:").pack(anchor = "w", pady=5)
dado_cpf = tk.Entry(janela)
dado_cpf.pack(anchor = "w")

#senha
tk.Label(janela, text="Digite uma senha (Deve conter ABC,123,!@#$%*):").pack(anchor = "w", pady=5)
dado_senha = tk.Entry(janela)
dado_senha.pack(anchor = "w")

#simbolos
sim = ["@","#","!","$","%*"]

#Confirme a senha
tk.Label(janela, text="Confirme sua senha:").pack(anchor = "w", pady=5)
dado_confirma_senha = tk.Entry(janela)
dado_confirma_senha.pack(anchor = "w")

#Definindo label_dados

label_dados = tk.Label(janela, text="")

#Função que o botão executa
def mostrar_mensagem() :
    nome = str(dado_nome.get().title().strip())
    cpf = dado_cpf.get().strip()
    senha = dado_senha.get().strip()
    confirma_senha = dado_confirma_senha.get().strip()

    if not nome: 
        messagebox.showwarning("Erro", "Por favor, insira seu nome.")
        return

    if not len(cpf) == 11 or not cpf.isnumeric():
        messagebox.showwarning("Erro", "Por favor, insira um CPF válido.")
        return
    if len(senha) <= 4:
        messagebox.showwarning("Erro", "Senha fraca")
        return
    elif senha.isalpha() or senha.isnumeric() or senha.isalnum():
        messagebox.showwarning("Erro", "Sua senha deve conter ao menos uma letra, um número e um símbolo (!@#$%*).")
        return
    if not confirma_senha == senha:
        messagebox.showwarning("Erro", "Sua senha deve ser igual à confirmação.")
        return
    else:  
        for c in senha:
            if not c.isalpha() and not c.isnumeric():
            
                if c in sim: 
                    continue
                else:
                    messagebox.showwarning("Erro", "Sua senha deve conter ao menor um síbolo (!@#$%*).")
                    return

    label_dados.config(text=f"Olá, {nome}. Cadastro concluído com sucesso!")


#botão com o comando = função
botão_confirmar = tk.Button(janela, text="Confirmar", command = mostrar_mensagem)
botão_confirmar.pack( anchor = "w", pady=10)

#printa label_dados
label_dados.pack()



janela.mainloop()
