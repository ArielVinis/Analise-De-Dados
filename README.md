# <center> Analise-De-Dados
## Aprendendo e treinando sobre Análise de Dados em Python

---
## 1 - Aplicação de banco de dados.
* Python é uma linguagem de programação amplamente utilizada para interagir com sistemas de gerenciamento de banco de dados (SGBD) por meio de bibliotecas como a sqlite3. Essa biblioteca permite a criação, leitura, atualização e exclusão de dados em bancos de dados SQL, seguindo o modelo CRUD (Create, Read, Update, Delete). Com a Python, nós, desenvolvedores, podemos desenvolver aplicativos que se comunicam de forma eficaz com bancos de dados relacionais, proporcionando flexibilidade e escalabilidade para nossas aplicações.
###  Conexão com banco de dados:
* Quando desenvolvemos uma aplicação em uma linguagem de programação que precisa interagir com um Sistema Gerenciador de Banco de Dados Relacional (RDBMS), é essencial estabelecer uma conexão entre esses dois processos distintos. Depois que a conexão é estabelecida, podemos enviar comandos SQL para realizar operações no banco de dados. Para viabilizar essa comunicação entre a linguagem de programação e o RDBMS, fazemos uso de tecnologias como Open Database Connectivity (ODBC) e Java Database Connectivity (JDBC).`

  1.    Importamos o módulo "sqlite3" e conectamos (ou criamos) um banco de dados chamado “exemplo.db”.
  2.    Criamos um objeto cursor que nos permite executar comandos SQL.
  3.    Definimos o comando SQL para criar a tabela “Produtos” com campos para “id”, “nome”, “preco” e “estoque”.
  4.    Executamos o comando SQL usando o cursor.
  5.    Confirmamos as alterações no banco de dados com commit().
  6.    Por fim, fechamos a conexão com o banco de dados.

O comando CREATE TABLE é um exemplo de DDL (Data Definition Language, ou Linguagem de Definição de Dados), pois possibilita a definição de uma nova estrutura de banco de dados.
    
### CRUD – CREATE, READ, UPDATE, DELETE:
* Podemos inserir informações (create), ler (read), atualizar (update) e apagar (delete). Os passos necessários para efetuar uma das operações do CRUD são sempre os mesmos: 
  1. estabelecer a conexão com um banco;
  2. criar um cursor e executar o comando;
  3. gravar a operação;
  4. fechar o cursor e a conexão.
####
* Obs.: É importante lembrar que esses são exemplos simplificados. Em uma aplicação real, talvez você precise adicionar tratamento de erros, validação de dados e outros recursos extras. Por isso é essencial sempre praticar e analisar cada vez mais exemplos para compreender tais conceitos.

#### 1.6 - O objetivo foi criar a tabela “Contatos” para armazenar informações de contatos, incluindo nome, e-mail e número de telefone.

---
## 2 - Biblioteca Pandas