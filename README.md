# <center> Analise-De-Dados
### Aprendendo e treinando sobre Análise de Dados em Python

---
## 1.0 - APLICAÇÃO DE BANCO DE DADOS
  * Python é uma linguagem de programação amplamente utilizada para interagir com sistemas de gerenciamento de banco de dados (SGBD) por meio de bibliotecas como a sqlite3. Essa biblioteca permite a criação, leitura, atualização e exclusão de dados em bancos de dados SQL, seguindo o modelo CRUD (Create, Read, Update, Delete). Com a Python, nós, desenvolvedores, podemos desenvolver aplicativos que se comunicam de forma eficaz com bancos de dados relacionais, proporcionando flexibilidade e escalabilidade para nossas aplicações.
###  Conexão com banco de dados
* Quando desenvolvemos uma aplicação em uma linguagem de programação que precisa interagir com um Sistema Gerenciador de Banco de Dados Relacional (RDBMS), é essencial estabelecer uma conexão entre esses dois processos distintos. Depois que a conexão é estabelecida, podemos enviar comandos SQL para realizar operações no banco de dados. Para viabilizar essa comunicação entre a linguagem de programação e o RDBMS, fazemos uso de tecnologias como Open Database Connectivity (ODBC) e Java Database Connectivity (JDBC).

    1.    Importamos o módulo "sqlite3" e conectamos (ou criamos) um banco de dados chamado “exemplo.db”.
    2.    Criamos um objeto cursor que nos permite executar comandos SQL.
    3.    Definimos o comando SQL para criar a tabela “Produtos” com campos para “id”, “nome”, “preco” e “estoque”.
    4.    Executamos o comando SQL usando o cursor.
    5.    Confirmamos as alterações no banco de dados com commit().
    6.    Por fim, fechamos a conexão com o banco de dados.

O comando CREATE TABLE é um exemplo de DDL (Data Definition Language, ou Linguagem de Definição de Dados), pois possibilita a definição de uma nova estrutura de banco de dados.
    
### CRUD – CREATE, READ, UPDATE, DELETE
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
## 2.0 - BIBLIOTECA PANDAS
### Introdução
* pandas é uma poderosa biblioteca de código aberto para a linguagem de programação Python criada para facilitar a manipulação e análise de dados tabulares e séries temporais. Ela fornece estruturas de dados flexíveis e eficientes, como DataFrames e Series, que permitem aos desenvolvedores trabalhar com dados de forma mais intuitiva e produtiva. Algumas características notáveis do panda incluem:

  1.    DataFrames e Series: o DataFrame é uma estrutura bidimensional semelhante a uma tabela, enquanto a Series é uma estrutura unidimensional semelhante a uma lista ou matriz. Ambas as estruturas são altamente flexíveis e podem acomodar diversos tipos de dados.
  2.    Manipulação de dados: o pandas oferece uma ampla gama de funções e métodos para realizar tarefas comuns de manipulação de dados, como filtragem, seleção, ordenação, agrupamento e agregação.
  3.    Leitura e escrita de dados: o pandas suporta a leitura e escrita de dados em vários formatos, incluindo CSV, Excel, SQL, HDF5 e muitos outros, tornando-se uma ferramenta versátil para lidar com dados de diferentes fontes.
  4.    Tratamento de dados ausentes: a biblioteca simplifica o tratamento de dados faltantes, permitindo que os desenvolvedores preencham ou removam valores ausentes de forma eficaz.
  5.    Visualização de dados: embora o pandas seja mais conhecido por sua capacidade de manipular dados, também pode ser integrado a outras bibliotecas de visualização, como Matplotlib e Seaborn, para criar gráficos e visualizações informativas.
  6.    Integração com NumPy: o pandas é construído sobre a biblioteca NumPy, o que significa que você pode facilmente combinar as capacidades de NumPy para cálculos numéricos com as funcionalidades do pandas para manipulação de dados.
  7.    Comunidade ativa: o pandas tem uma comunidade de usuários e desenvolvedores ativa, o que resulta em suporte contínuo e atualizações regulares.

O pandas é amplamente utilizado em análise de dados, ciência de dados e engenharia de dados. Ele oferece uma maneira eficiente e amigável de lidar com dados, fato que o torna uma escolha popular para profissionais que trabalham com informações estruturadas.

### 2.1 - Series em Lista e Dicionários
* Para criar um objeto do tipo Series no pandas, utilizamos o método Series() com vários parâmetros opcionais. O principal parâmetro é “data”, que pode conter um único valor, uma lista de valores ou um dicionário. Outros parâmetros, como “index”, “dtype” e “name”, têm valores-padrão predefinidos, tornando sua especificação opcional. A documentação oficial do pandas fornece detalhes completos sobre esses parâmetros. Saiba mais em: [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html.).

### 2.3 - Leitura de dados estruturados com a biblioteca pandas
* Um recurso poderoso no pandas é a capacidade de ler dados estruturados e armazená-los em um DataFrame. A biblioteca oferece vários métodos de leitura de dados, identificados pelo padrão “read”, como pandas.read_XXXXX(). Cada um desses métodos é projetado para ler diferentes tipos de fontes de dados.

### 2.4 - Aplicando o aprendizado
* Começamos esse exercício criando um dicionário chamado dados, que contém os nomes e idades dos clientes. Em seguida, usamos o pandas para criar uma série chamada serie_idades a partir desse dicionário, de forma que os nomes são definidos como o índice da série.
* Após criar a série, calculamos a média das idades usando o método mean() e a exibimos na saída.
* A saída do código mostra a série de idades e a média das idades do grupo. Esse é um exemplo simples de como você pode usar o pandas para realizar cálculos em dados estruturados.

---
## 3.0 - MANIPULAÇÃO DE DADOS EM PANDA
### Métodos para leitura e escrita da biblioteca pandas
* Os métodos de leitura de dados estruturados no pandas têm em comum o prefixo “pd.read_XXXX”, sendo “pd” um, aliás frequentemente utilizado ao importar a biblioteca e “XXX” a parte restante da sintaxe específica de cada método. Além da leitura, o pandas oferece diversos métodos para escrever os dados contidos em um DataFrame em arquivos, bancos de dados ou até mesmo para a área de transferência do sistema operacional. Isso torna o pandas uma ferramenta versátil para lidar com dados estruturados, independentemente de sua origem.

### 3.1 - Captura e transformação dos dados
* A etapa de captura e transformação/padronização dos dados é uma parte crucial no processo de análise de dados e modelagem de machine learning, por exemplo. Nessa fase, você coleta os dados brutos de várias fontes, como arquivos CSV, bancos de dados, APIs, e os prepara para uma análise posterior. O pandas é uma biblioteca Python muito útil para realizar essas tarefas, pois fornece estruturas de dados flexíveis e ferramentas poderosas para manipular e transformar dados.
* O primeiro passo para o desenvolvimento desse processo é importar o pandas. Em seguida, utilizamos o método para ler um arquivo JSON. Por fim, pedimos informações sobre esse DataFrame: existem 9.379 registros, 2 colunas, os índices são numéricos e variam de 0 a 9.378; não existem linhas faltantes, pois existem 9.379 registros não nulos; os dados são do tipo “object”, ou são todos strings, ou há uma mistura desses tipos.
* Já conhecemos nosso DataFrame. Agora, vamos verificar a duplicidade de linhas (um passo muito importante) utilizando a função drop_duplicates(). No nosso exemplo, usaremos: df_selic.drop_duplicates(keep='last', inplace=True), que mantém o último registro (keep='last') e, a partir do parâmetro inplace=True, faz com que a transformação seja salva do DataFrame. Na prática, estamos sobrescrevendo o objeto na memória. Nesse caso, não existem linhas duplicadas.
* Outra ação que podemos efetuar é criar uma nova coluna no DataFrame. Para isso, a sintaxe é simples: df_[‘nova_coluna’] = dado. No nosso caso, vamos inserir duas colunas, uma com a data da extração dos dados e outra com o responsável pela extração.

### Extração de informações
* Após saber coletar os dados e transformá-los, devemos passar para o próximo passo, que é extrair informação deles. Nessa etapa, precisamos conhecer o que estamos procurando para tentar encontrar esse elemento nos dados. Existem inúmeras ferramentas e maneiras pelas quais podemos fazer isso, como por meio de filtros utilizando loc., filtros utilizando testes booleanos, entre outras medidas.

### 3.2 - Sobre a Aplicação
* Criamos um DataFrame com dados fictícios. Observe que temos duas linhas duplicadas e, após excluir uma delas, ficamos com quatro itens, sendo que somente o produto B do vestuário tem valor acima de R$ 50,00.

---
## 4.0 - VISUALIZAÇÃO DE DADOS
### 4.1 - Matplotlib
* A biblioteca Matplotlib exerce uma função central na criação de gráficos em Python, sendo amplamente adotada em projetos de visualização de dados. John Hunter é o criador e uma figura-chave para o desenvolvimento dessa biblioteca, que surge como uma alternativa ao uso de ferramentas como gnuplot e MATLAB na comunidade científica. Anteriormente, os cientistas tinham que gerar gráficos em outros softwares após extrair os resultados de suas análises, fato que tornava o processo incômodo. Assim, a biblioteca Matplotlib emergiu como uma solução eficiente para criar visualizações em Python.
* A instalação do Matplotlib pode ser facilmente realizada com o comando “pip install matplotlib”. Em ambientes como Anaconda e Google Colab, essa biblioteca já está prontamente disponível. O módulo “pyplot” é uma parte essencial do Matplotlib, pois disponibiliza funções que facilitam a criação e personalização de gráficos. Duas sintaxes comuns para importar o Matplotlib com o apelido “plt” são: “import matplotlib.pyplot as plt” e “from matplotlib import pyplot as plt”
* Existem duas formas de criar o gráfico:
  1. O pyplot cria e gerencia automaticamente figuras e eixos, e usa as funções do pyplot para plotagem.
  2. Criar explicitamente figuras e eixos, e chamar métodos sobre eles (o “estilo orientado a objetos (OO)”).

### 4.2 - Biblioteca pandas
* Conheci muitas funcionalidades da biblioteca pandas; uma delas diz respeito à visualização gráfica. As principais estruturas de dados da biblioteca pandas (Series e DataFrame) possuem o método plot(), construído com base no Matplotlib que permite criar gráficos a partir dos dados nas estruturas.

### 4.3 - Biblioteca Seaborn
* O Seaborn, uma biblioteca Python construída sobre a base do Matplotlib, destaca-se na criação de gráficos de forma especializada. Você pode usar essa biblioteca importando-a em seus projetos da seguinte forma: “import seaborn as sns”. Uma característica notável do Seaborn é seu repositório de conjuntos de dados prontos para uso, o que facilita a exploração das funcionalidades. Você pode acessar esses conjuntos de dados em [seaborn-data](https://github.com/mwaskom/seaborn-data). Para ilustrar, foi carregado dados sobre gorjetas (tips) e utilizado em nosso estudo. O Seaborn simplifica a criação de gráficos e as análises de dados, mostrando-se uma ferramenta valiosa para a visualização de informações.

### 4.4 - Aplicação com DataSet
* Utilizado o DataSet sobre gorjeta apresentado nesta etapa de aprendizagem.
* Consegui verificar que o gasto no jantar é bem superior ao gasto no almoço. Mas quantos clientes almoçaram e quantos jantaram? Investigado o gasto médio por período.
* Entendi que a média gasta no jantar também é superior à do almoço. Logo, esse é o principal período do restaurante em relação a faturamento. Por fim, foi verificado a média de gorjeta por período.
* A média de gorjeta no jantar também é superior à do almoço.

---
## 5.0 - ANÁLISE DE DADOS COM PYTHON
* Ao tratar de manipulação de dados, devemos ter em mente que muitas vezes os dados não se apresentam da forma mais padronizada possível, o que dificulta a extração de informações úteis. Por essa razão, a manipulação é uma parte do processo com a qual se deve ter muito cuidado.

### 5.1 - Conectar ao banco de dados SQLite
* Primeiro, precisamos criar um banco de dados SQLite e uma tabela para armazenar as informações dos funcionários. Vamos estabelecer uma conexão com o banco de dados.
### 5.2 - Criar a tabela de funcionários
* Vamos criar uma tabela chamada “funcionários” para armazenar as informações dos funcionários.
### 5.3 - Inserir um novo funcionário
* Agora, vamos inserir um novo funcionário na tabela, simulando a operação de “Create”.
### 5.4 - Consultar funcionários
* Podemos consultar os funcionários existentes na tabela, simulando a operação de “Read”.
### 5.5 - Atualizar informações de um funcionário
* Agora, vamos atualizar as informações de um funcionário específico, simulando a operação de “Update”.
### 5.6 - Deletar um funcionário
* Por fim, vamos deletar um funcionário da tabela, simulando a operação de “Delete”.