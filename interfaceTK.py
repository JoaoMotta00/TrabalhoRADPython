import tkinter as tk
from tkinter import messagebox
from RADcrud import adicionarAluno, exibirAluno, removerAluno

def cadastrar():
    try:
        matricula = int(campo_matricula.get())
        cpf = int(campo_cpf.get())
        nome = campo_nome.get()
        data = campo_data.get()
        endereco = campo_endereco.get()
        nota1 = int(campo_nota1.get())
        nota2 = int(campo_nota2.get())

        adicionarAluno(
            matricula,
            cpf,
            nome,
            data,
            endereco,
            nota1,
            nota2
        )

        messagebox.showinfo("Sistema", "Aluno cadastrado com sucesso!")

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite apenas números nos campos numéricos"
        )


def exibir():
    lista.delete(0, tk.END)

    dados = exibirAluno()

    for aluno in dados:
        lista.insert(tk.END, aluno)



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

janela = tk.Tk()
janela.title("Sistema de cadastro de Alunos")
janela.geometry("500x700")
janela.resizable(False, False)
janela.config(bg="black")


msg = tk.Label(janela, text="Bem-vindo ao sistema de cadastro de alunos!", padx=0, pady=0,)
msg.config(font=("Comic Sans MS", 13, "underline",), fg="white", bg="black")
msg.pack()

msg2 = tk.Label(janela, text="Para CADASTRAR um aluno, preencha os campos abaixo e clique em 'Cadastrar'.\nPara EXIBIR os alunos cadastrados, clique em 'Exibir alunos'.\nPara REMOVER um aluno, digite a matrícula e clique em 'Remover aluno'.", padx=0, pady=20,)
msg2.config(font=("Comic Sans MS", 10), fg="white", bg="black")
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



botao_cadastrar = tk.Button(
    janela,
    text="Cadastrar",
    bg="yellow",
    fg="black",
    command=cadastrar
)

botao_cadastrar.pack(pady=5)


botao_exibir = tk.Button(
    janela,
    text="Exibir alunos",
    bg="yellow",
    fg="black",
    command=exibir
)

botao_exibir.pack(pady=5)



botao_remover = tk.Button(
    janela,
    text="Remover aluno",
    bg="lightcoral",
    fg="black",
    command=remover
)

botao_remover.pack(pady=5)


lista = tk.Listbox(janela, width=80, fg="white", bg="black", font=("Comic Sans MS", 10, "bold"))
lista.pack(pady=5)


janela.mainloop()