# <center> Analise-De-Dados
## Aprendendo e treinando sobre Análise de Dados em Python

---
## 1.0 - Aplicação de banco de dados.
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
####
* 1.6 - O objetivo foi criar a tabela “Contatos” para armazenar informações de contatos, incluindo nome, e-mail e número de telefone.

---
## 2.0 - Biblioteca Pandas
### Introdução:
* pandas é uma poderosa biblioteca de código aberto para a linguagem de programação Python criada para facilitar a manipulação e análise de dados tabulares e séries temporais. Ela fornece estruturas de dados flexíveis e eficientes, como DataFrames e Series, que permitem aos desenvolvedores trabalhar com dados de forma mais intuitiva e produtiva. Algumas características notáveis do pandas incluem:

  1.    DataFrames e Series: o DataFrame é uma estrutura bidimensional semelhante a uma tabela, enquanto a Series é uma estrutura unidimensional semelhante a uma lista ou matriz. Ambas as estruturas são altamente flexíveis e podem acomodar diversos tipos de dados.
  2.    Manipulação de dados: o pandas oferece uma ampla gama de funções e métodos para realizar tarefas comuns de manipulação de dados, como filtragem, seleção, ordenação, agrupamento e agregação.
  3.    Leitura e escrita de dados: o pandas suporta a leitura e escrita de dados em vários formatos, incluindo CSV, Excel, SQL, HDF5 e muitos outros, tornando-se uma ferramenta versátil para lidar com dados de diferentes fontes.
  4.    Tratamento de dados ausentes: a biblioteca simplifica o tratamento de dados faltantes, permitindo que os desenvolvedores preencham ou removam valores ausentes de forma eficaz.
  5.    Visualização de dados: embora o pandas seja mais conhecido por sua capacidade de manipular dados, também pode ser integrado a outras bibliotecas de visualização, como Matplotlib e Seaborn, para criar gráficos e visualizações informativas.
  6.    Integração com NumPy: o pandas é construído sobre a biblioteca NumPy, o que significa que você pode facilmente combinar as capacidades de NumPy para cálculos numéricos com as funcionalidades do pandas para manipulação de dados.
  7.    Comunidade ativa: o pandas tem uma comunidade de usuários e desenvolvedores ativa, o que resulta em suporte contínuo e atualizações regulares.

O pandas é amplamente utilizado em análise de dados, ciência de dados e engenharia de dados. Ele oferece uma maneira eficiente e amigável de lidar com dados, fato que o torna uma escolha popular para profissionais que trabalham com informações estruturadas.

### 2.1 - Series em Lista e Dicionários:
* Para criar um objeto do tipo Series no pandas, utilizamos o método Series() com vários parâmetros opcionais. O principal parâmetro é “data”, que pode conter um único valor, uma lista de valores ou um dicionário. Outros parâmetros, como “index”, “dtype” e “name”, têm valores-padrão predefinidos, tornando sua especificação opcional. A documentação oficial do pandas fornece detalhes completos sobre esses parâmetros. Saiba mais em: [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html.).

### 2.3 - Leitura de dados estruturados com a biblioteca pandas:
* Um recurso poderoso no pandas é a capacidade de ler dados estruturados e armazená-los em um DataFrame. A biblioteca oferece vários métodos de leitura de dados, identificados pelo padrão “read”, como pandas.read_XXXXX(). Cada um desses métodos é projetado para ler diferentes tipos de fontes de dados.

### 2.4 - Aplicando o aprendizado:
* Começamos esse exercício criando um dicionário chamado dados, que contém os nomes e idades dos clientes. Em seguida, usamos o pandas para criar uma série chamada serie_idades a partir desse dicionário, de forma que os nomes são definidos como o índice da série.

* Após criar a série, calculamos a média das idades usando o método mean() e a exibimos na saída.

* A saída do código mostra a série de idades e a média das idades do grupo. Esse é um exemplo simples de como você pode usar o pandas para realizar cálculos em dados estruturados.