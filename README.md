Trabalho de RAD em Python<br/>
Integrantes do grupo:

João Luiz de Farias Motta(Matrícula: 202503289352)<br/>
Yuri Gustavo Marciano(Matrícula: 202503839107) <br/>
Hian Erinaldo Silva de Souza(Matrícula: 202503109192) <br/>
João Vitor Pereira Barbosa(Matrícula: 202502381468)<br/>
Hiago Pompilio da Costa(Matrícula: 202502502826)<br/>
<br/>

Perdas e Ganhos da Migração do PostgreSQL para o SQLite

- Migrar do PostgreSQL para o SQLite traz ganhos em simplicidade, mas perdas significativas em performance e recursos.<br/>
    - Principais Ganhos:<br/>
        . Banco vira um único arquivo: zero configuração de servidor.<br/>
        . Deploy, backup e desenvolvimento extremamente simples e rápidos.<br/>
        . Menor consumo de recursos (CPU/RAM) e custo mais baixo.<br/>
        . Excelente para cenários com pouca concorrência.<br/>
    - Principais Perdas:<br/>
        . Concorrência ruim: sofre bastante com várias escritas simultâneas (pode travar ou ficar lento).<br/>
        . Perde recursos avançados do Postgres (JSONB poderoso, Partitioning, Window Functions, replicação, etc.).<br/>
        . Dificuldade de escalar e menor segurança avançada.<br/>
        . Não é adequado para aplicações com muitos usuários simultâneos.<br/>


A migração vale a pena apenas se sua aplicação for pequena ou média<br/>
Com baixa concorrência (geralmente menos de 10-15 usuários escrevendo ao mesmo tempo)<br/>
E o principal objetivo for simplificar a infraestrutura e reduzir custos.<br/>
Se o sistema já tem ou pretende ter crescimento, múltiplos usuários simultâneos ou usa recursos avançados do PostgreSQL, o ideal é continuar no PostgreSQL.
