Trabalho de RAD em Python

Integrantes do grupo:
- João Luiz de Farias Motta(Matrícula: 202503289352)
- Yuri Gustavo Marciano(Matrícula: 202503839107)
- Hian Erinaldo Silva de Souza(Matrícula: 202503109192)
- João Vitor Pereira Barbosa(Matrícula: 202502381468)
- Hiago Pompilio da Costa(Matrícula: 202502502826)

Sistema de Cadastro de Alunos desenvolvido em Python, utilizando interface gráfica com Tkinter e banco de dados em SQLite. O banco de dados é criado em um arquivo local chamado alunos.db, onde são armazenadas dados como matrícula, CPF, nome, data de nascimento, endereço e notas dos alunos.
A interface gráfica permite cadastrar, consultar, editar e remover alunos de forma simples.

Funcionalidades:
- Cadastro de alunos
- Consulta de registros
- Edição de dados
- Remoção de alunos
- Armazenamento permanente dos dados em banco SQLite

Estrutura do Projeto:
- RADcrud1.py: responsável pelas operações do banco de dados.
- interfaceTK1.py: responsável pela interface gráfica do sistema.

Como executar:
- Junto do arquivo RADcrud1.py, execute o arquivo interfaceTK1.py.
- Digite os dados dos alunos nos campos de texto da tela.
- Depois clique em um dos botões para cadastrar, ou exibir, editar ou remover algum registro de alunos.


Perdas e Ganhos da Migração do PostgreSQL para o SQLite:

- Migrar do PostgreSQL para o SQLite traz ganhos em simplicidade, mas perdas significativas em performance e recursos.
    - Principais Ganhos:
        . Banco vira um único arquivo: zero configuração de servidor.
        . Deploy, backup e desenvolvimento extremamente simples e rápidos.
        . Menor consumo de recursos (CPU/RAM) e custo mais baixo.
        . Excelente para cenários com pouca concorrência.
    - Principais Perdas:<br/>
        . Concorrência ruim: sofre bastante com várias escritas simultâneas (pode travar ou ficar lento).
        . Perde recursos avançados do Postgres (JSONB poderoso, Partitioning, Window Functions, replicação, etc.).
        . Dificuldade de escalar e menor segurança avançada.
        . Não é adequado para aplicações com muitos usuários simultâneos.


A migração vale a pena apenas se sua aplicação for pequena ou média
Com baixa concorrência (geralmente menos de 10-15 usuários escrevendo ao mesmo tempo)
E o principal objetivo for simplificar a infraestrutura e reduzir custos.
Se o sistema já tem ou pretende ter crescimento, múltiplos usuários simultâneos ou usa recursos avançados do PostgreSQL, o ideal é continuar no PostgreSQL.
