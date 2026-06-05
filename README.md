Trabalho de RAD em Python

Integrantes do grupo:
- João Luiz de Farias Motta(Matrícula: (202503289352)
- Yuri Gustavo Marciano(Matrícula: (202503839107)
- Hian Erinaldo Silva de Souza(Matrícula: (202503109192)
- João Vitor Pereira Barbosa(Matrícula: (202502381468)
- Hiago Pompilio da Costa(Matrícula: (202502502826)

Sistema de Cadastro de Alunos
Desenvolvido em Python, utilizando interface gráfica com Tkinter e banco de dados SQLite. O banco de dados é criado em um arquivo local chamado alunos.db, onde são armazenados dados como matrícula, CPF, nome, data de nascimento, endereço e notas dos alunos.
A interface gráfica permite cadastrar, consultar, editar e remover alunos de forma simples e intuitiva.
Funcionalidades:

Cadastro de novos alunos.
Consulta de registros.
Edição de dados.
Remoção de alunos.
Armazenamento permanente dos dados em banco de dados SQLite.

Estrutura do Projeto:

RADcrud1.py: responsável pelas operações do banco de dados.
interfaceTK1.py: responsável pela interface gráfica do sistema.

Como executar:

Execute o arquivo interfaceTK1.py (o arquivo RADcrud1.py deve estar no mesmo diretório).
Digite os dados dos alunos nos campos da tela.
Clique nos botões correspondentes para cadastrar, consultar, editar ou remover registros.

Perdas e Ganhos da Migração do PostgreSQL para o SQLite:
Migrar do PostgreSQL para o SQLite traz ganhos em simplicidade, porém perdas significativas em performance e recursos avançados:
Principais Ganhos:

Banco de dados vira um único arquivo: zero configuração de servidor.
Deploy, backup e desenvolvimento extremamente simples e rápidos.
Menor consumo de recursos (CPU/RAM) e custo mais baixo.
Excelente para cenários com pouca concorrência.

Principais Perdas:

Concorrência ruim: sofre bastante com várias escritas simultâneas (pode travar ou ficar lento).
Perde recursos avançados do PostgreSQL (JSONB poderoso, Partitioning, Window Functions, replicação, etc.).
Dificuldade de escalar e menor segurança avançada.
Não é adequado para aplicações com muitos usuários simultâneos.

A migração vale a pena apenas se sua aplicação for pequena ou média, com baixa concorrência (geralmente menos de 10-15 usuários escrevendo ao mesmo tempo) e o principal objetivo for simplificar a infraestrutura e reduzir custos.
Caso o sistema já tenha ou pretenda ter crescimento, múltiplos usuários simultâneos ou utilize recursos avançados do PostgreSQL, o ideal é manter o PostgreSQL.
