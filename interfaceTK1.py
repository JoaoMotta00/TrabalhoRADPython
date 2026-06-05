import tkinter as tk
import sqlite3
from tkinter import messagebox
from RADcrud1 import adicionarAluno, exibirAluno, removerAluno, editarAluno

# Conexão com o banco de dados


#função para cadastrar um aluno, recebendo os dados dos campos de entrada e chamando a função adicionarAluno do arquivo RADcrud1.py, além de limpar os campos de entrada após o cadastro e exibir uma mensagem de sucesso ou erro.
def cadastrar():
    try:
        matricula = int(campo_matricula.get())
        cpf = int(campo_cpf.get())
        nome = campo_nome.get()
        data = campo_data.get()
        endereco = campo_endereco.get()
        nota1 = campo_nota1.get()
        nota2 = campo_nota2.get()
        
        adicionarAluno(
            matricula,
            cpf,
            nome,
            data,
            endereco,
            nota1,
            nota2
        )

        campo_matricula.delete(0,tk.END)
        campo_cpf.delete(0,tk.END)
        campo_nome.delete(0,tk.END)
        campo_data.delete(0,tk.END)
        campo_endereco.delete(0,tk.END)
        campo_nota1.delete(0,tk.END)
        campo_nota2.delete(0,tk.END)

        messagebox.showinfo("Sistema", "Aluno cadastrado com sucesso!")

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite apenas números nos campos numéricos"
        )


#Função para exibir os alunos cadastrados, limpando a lista e inserindo os dados dos alunos na lista.
def exibir():
    lista.delete(0, tk.END)

    dados = exibirAluno()

    for aluno in dados:
        lista.insert(tk.END, aluno)


#Função para remover um aluno, recebendo a matrícula do campo de entrada e chamando a função removerAluno do arquivo RADcrud1.py, além de exibir uma mensagem de sucesso ou erro.
def remover():
    try:
        matricula = int(campo_matricula.get())

        removerAluno(matricula)

        messagebox.showinfo("Sistema", "Aluno removido com sucesso!")

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite uma matrícula válida"
        )


#Função para editar os dados de um aluno, recebendo a matrícula do campo de entrada e chamando a função editarAluno do arquivo RADcrud1.py, além de exibir uma mensagem de sucesso ou erro.
def editar():
    connection = sqlite3.connect("alunos.db") #Cria um arquivo .db para armazenar os dados
    alunos = connection.cursor()

    matricula = int(campo_matricula.get())


    try:
        alunos.execute("SELECT nome,endereco,nota1,nota2 FROM alunos WHERE matricula = ?", ([matricula]))
        aluno = alunos.fetchone()
        connection.commit()

        lista.forget()
        botao_confirma.pack(pady=5)
        botao_cancela.pack(pady=5)
        botao_editar.forget()
        botao_remover.forget()
        lista.pack(pady=5)

        campo_nome.delete(0, tk.END)
        campo_nome.insert(0, aluno[0])
        
        campo_endereco.delete(0,tk.END)
        campo_endereco.insert(0, aluno[1])
        
        campo_nota1.delete(0,tk.END)
        campo_nota1.insert(0, aluno[2])

        campo_nota2.delete(0,tk.END)
        campo_nota2.insert(0, aluno[3])
       
    except IndexError:
        messagebox.showerror(
            "Erro",
            "Digite uma matrícula válida"
        )

#Função para confirmar a edição dos dados de um aluno, chamando a função editarAluno do arquivo RADcrud1.py, além de limpar os campos de entrada e exibir uma mensagem de sucesso ou erro.
def confirma():
    editarAluno(campo_matricula.get(),campo_nome.get(),campo_endereco.get(), campo_nota1.get(),campo_nota2.get()), 
    messagebox.showinfo("Sistema","Aluno editado"),

    lista.forget()
    botao_editar.pack(pady=5)
    botao_remover.pack(pady=5)
    botao_confirma.forget()
    botao_cancela.forget()
    lista.pack(pady=5)

    campo_matricula.delete(0, tk.END)
    campo_nome.delete(0, tk.END)
    campo_endereco.delete(0,tk.END)
    campo_nota1.delete(0,tk.END)
    campo_nota2.delete(0,tk.END)

#Função para cancelar a edição dos dados de um aluno, limpando os campos de entrada e exibindo uma mensagem de cancelamento.
def cancela():

    lista.forget()
    botao_editar.pack(pady=5)
    botao_remover.pack(pady=5)
    botao_cancela.forget()
    botao_confirma.forget()
    lista.pack(pady=5)

    campo_matricula.delete(0, tk.END)
    campo_nome.delete(0, tk.END)
    campo_endereco.delete(0,tk.END)
    campo_nota1.delete(0,tk.END)
    campo_nota2.delete(0,tk.END)


#Janela principal do sistema, com título, tamanho, cor de fundo e widgets para exibir mensagens, campos de entrada e botões para cadastrar, exibir, editar e remover alunos, além de uma lista para exibir os alunos cadastrados.
janela = tk.Tk()
janela.title("Sistema de cadastro de Alunos")
janela.geometry("600x700")
janela.resizable(False, False)
janela.config(bg="black")

#Widgets da janela principal, com mensagens de boas-vindas e instruções, campos de entrada para matrícula, cpf, nome, data de nascimento, endereço e notas, botões para cadastrar, exibir, editar e remover alunos, além de uma lista para exibir os alunos cadastrados.
msg = tk.Label(janela, text="Bem-vindo ao sistema de cadastro de alunos!", padx=0, pady=0,)
msg.config(font=("Arial", 12, "underline",), fg="white", bg="black")
msg.pack()

#Mensagem de instruções para o usuário, explicando como usar o sistema.
msg2 = tk.Label(janela, text="Para CADASTRAR um aluno, preencha os campos abaixo e clique em 'Cadastrar'.\nPara EXIBIR os alunos cadastrados, clique em 'Exibir alunos'.\nPara REMOVER um aluno, digite a matrícula e clique em 'Remover aluno'.\nPara EDITAR um aluno, digite a matrícula e clique em 'Editar aluno'.", padx=0, pady=0,)
msg2.config(font=("Arial", 8), fg="white", bg="black")
msg2.pack()

#Matrícula
label_matricula = tk.Label(janela, text="Matrícula", bg="black", fg="white")
label_matricula.pack()

campo_matricula = tk.Entry(janela)
campo_matricula.pack()


# CPF
label_cpf = tk.Label(janela, text="CPF", bg="black", fg="white")
label_cpf.pack()

campo_cpf = tk.Entry(janela)
campo_cpf.pack()


# NOME
label_nome = tk.Label(janela, text="Nome", bg="black", fg="white")
label_nome.pack()

campo_nome = tk.Entry(janela)
campo_nome.pack()


# DATA
label_data = tk.Label(janela, text="Data de nascimento", bg="black", fg="white")
label_data.pack()

campo_data = tk.Entry(janela)
campo_data.pack()


# ENDEREÇO
label_endereco = tk.Label(janela, text="Endereço", bg="black", fg="white")
label_endereco.pack()

campo_endereco = tk.Entry(janela)
campo_endereco.pack()


# NOTA 1
label_nota1 = tk.Label(janela, text="Nota 1", bg="black", fg="white")
label_nota1.pack()

campo_nota1 = tk.Entry(janela)
campo_nota1.pack()


# NOTA 2
label_nota2 = tk.Label(janela, text="Nota 2", bg="black", fg="white")
label_nota2.pack()

campo_nota2 = tk.Entry(janela)
campo_nota2.pack()


#Botões para cadastrar, exibir, editar e remover alunos, além de uma lista para exibir os alunos cadastrados.

botao_cadastrar = tk.Button(
    janela,
    text="Cadastrar",
    bg="lightgreen",
    fg="black",
    command=cadastrar
)

botao_cadastrar.pack(pady=5)


botao_exibir = tk.Button(
    janela,
    text="Exibir alunos",
    bg="lightblue",
    fg="black",
    command=exibir
)

botao_exibir.pack(pady=5)

botao_editar = tk.Button(
    janela,
    text="Editar aluno",
    bg="pink",
    fg="black",
    command=editar
)

botao_editar.pack(pady=5)

botao_confirma = tk.Button(
    janela,
    text="Confirmar edição",
    bg="Green",
    fg="black",
    command=confirma
)

botao_cancela = tk.Button(
    janela,
    text="Cancelar edição",
    bg="Red",
    fg="black",
    command=cancela
)

botao_remover = tk.Button(
    janela,
    text="Remover aluno",
    bg="lightcoral",
    fg="black",
    command=remover
)

botao_remover.pack(pady=5)


#Lista para exibir os alunos cadastrados, com largura, altura, cor de fundo e fonte personalizada.
lista = tk.Listbox(janela, width=70, height=20, fg="white", bg="black", font=("Arial", 10, "bold"))
lista.pack(pady=5)

#Inicia a janela principal do sistema, exibindo a interface gráfica para o usuário interagir com o sistema de cadastro de alunos.
janela.mainloop()