import sqlite3

#EXECUTAR PRIMEIRO
#Cria o banco de dados
try:
#Cria o banco de dados
    connection = sqlite3.connect("alunos.db") #Cria um arquivo .db para armazenar os dados
    alunos = connection.cursor() #Cria cursor pra executar comandos SQL no banco de dados

    #Cria a tabela alunos, caso ela não exista, com os campos matrícula, cpf, nome, data_nascimento e endereço.
    alunos.execute("""
        CREATE TABLE IF NOT EXISTS alunos(matricula INTEGER,
                                        cpf INTEGER,
                                        nome TEXT NOT NULL,
                                        data_nascimento TEXT NOT NULL,
                                        endereco TEXT NOT NULL,
                                        nota1 INTEGER,
                                        nota2 INTEGER,
                                        PRIMARY KEY(matricula, cpf))
    """) #PRIMARY KEY: chave primária. Composta por matrícula e cpf nesse caso, garantindo que cada aluno seja único no banco de dados.
    #INTEGER: números inteiros
    #TEXT NOT NULL: campo obrigatório, não pode ser nulo

    connection.commit() #Salva as alterações feitas no banco de dados
    
#Tratamento de exceção para erros relacionados ao banco de dados SQLite3. 
except sqlite3.Error as erro:
    print(f"Erro ao conectar/criar banco de dados: {erro}")
    
#EXECUTE APÓS O PRIMEIRO

def adicionarAluno(matricula, cpf, nome, data, endereco, nota1, nota2):
    try:
        alunos.execute(
            """
            INSERT INTO alunos(
                matricula,
                cpf,
                nome,
                data_nascimento,
                endereco,
                nota1,
                nota2
            )
            VALUES(?, ?, ?, ?, ?, ?, ?)
            """,
            (
                matricula,
                cpf,
                nome,
                data,
                endereco,
                nota1,
                nota2
            )
        )

        connection.commit()

    except sqlite3.Error as erro:
        return f"Erro: {erro}"


def removerAluno(matricula):
    alunos.execute(
        "DELETE FROM alunos WHERE matricula = ?",
        (matricula,)
    )

    connection.commit()
    

def exibirAluno():
    alunos.execute("SELECT * FROM alunos")
    return alunos.fetchall()

def editarAluno(matricula, nome, endereco, nota1, nota2):
        try:
            alunos.execute("""UPDATE alunos 
                              SET nome = ?, 
                                  endereco = ?,
                                  nota1 = ?,
                                  nota2 = ?
                              WHERE matricula = ?  """, (nome, endereco, nota1, nota2, matricula))
            connection.commit()
        except ValueError:
                print("Erro: matrícula deve ser um número inteiro.")


#####################################################################################################################################


#_Perdas e Ganhos da Migração do PostgreSQL para o SQLite_

#Migrar do PostgreSQL para o SQLite traz ganhos em simplicidade, mas perdas significativas em performance e recursos.
    #Principais Ganhos:
        #Banco vira um único arquivo: zero configuração de servidor.
        #Deploy, backup e desenvolvimento extremamente simples e rápidos.
        #Menor consumo de recursos (CPU/RAM) e custo mais baixo.
        #Excelente para cenários com pouca concorrência.
    #Principais Perdas:
        #Concorrência ruim: sofre bastante com várias escritas simultâneas (pode travar ou ficar lento).
        #Perde recursos avançados do Postgres (JSONB poderoso, Partitioning, Window Functions, replicação, etc.).
        #Dificuldade de escalar e menor segurança avançada.
        #Não é adequado para aplicações com muitos usuários simultâneos.
#A migração vale a pena apenas se sua aplicação for pequena ou média
#Com baixa concorrência (geralmente menos de 10-15 usuários escrevendo ao mesmo tempo)
#E o principal objetivo for simplificar a infraestrutura e reduzir custos.
#Se o sistema já tem ou pretende ter crescimento, múltiplos usuários simultâneos ou usa recursos avançados do PostgreSQL, o ideal é continuar no Postgres.