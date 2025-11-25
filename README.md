📊 Projeto Big Data – Segurança Urbana em Fortaleza (2025)

Este projeto tem como objetivo analisar dados simulados de segurança pública em bairros de Fortaleza, utilizando técnicas de Big Data, Python, MySQL, Pandas e Visualização de Dados.
O sistema importa um arquivo CSV, estrutura um banco de dados e gera gráficos analíticos para apoiar estudos e apresentações.

🚀 Tecnologias Utilizadas

Python 3.14

MySQL Community Server

Pandas

Matplotlib

NumPy

VS Code (opcional)

📦 Estrutura do Projeto
projeto_bigdata_fortaleza/
│-- setup_banco.py          # Cria o banco, tabela e importa o CSV
│-- gerar_graficos.py       # Gera gráficos a partir do banco de dados
│-- verificar_tabela.py     # Verifica registros no MySQL
│-- dados/
│     └── seguranca_fortaleza_modelo_121bairros.csv
│-- graficos/
      ├── grafico_ocorrencias.png
      ├── grafico_mortes.png
      └── grafico_indice_risco.png
│-- README.md

🗂️ Descrição dos Scripts
🔧 setup_banco.py

Conecta ao MySQL

Cria o banco seguranca_fortaleza

Cria a tabela bairros

Importa automaticamente o CSV

Converte caracteres para UTF-8

Insere todos os dados no banco

📊 gerar_graficos.py

Gera automaticamente três gráficos:

Ocorrências por Bairro (2025)

Mortes por Bairro (2025)

Índice de Risco Estimado

Todos são salvos em PNG com alta qualidade (300 DPI).

🔍 verificar_tabela.py

Lista os primeiros registros da tabela

Verifica se a importação ocorreu corretamente

🖼️ Exemplos de Gráficos

Os gráficos são salvos automaticamente na pasta graficos/.

📌 Ocorrências por Bairro
📌 Mortes por Bairro
📌 Índice de Risco Estimado

📥 Como Executar o Projeto
1️⃣ Instale as dependências no Python
pip install mysql-connector-python pandas matplotlib

2️⃣ Certifique-se de que o MySQL está rodando
3️⃣ Execute o script de setup
python setup_banco.py

4️⃣ Gere os gráficos
python gerar_graficos.py

🔐 Configurações do Banco

As credenciais padrão são:

HOST = "localhost"
USER = "root"
PASSWORD = "senha123"
DATABASE = "seguranca_fortaleza"


Pode alterar no próprio script, se necessário.

📌 Objetivo do Projeto

Este projeto foi desenvolvido para:

Treinar habilidades em análise de dados

Compreender fluxo ETL (Extrair, Transformar, Carregar)

Criar visualizações inteligentes para apresentação acadêmica

Demonstrar domínio de banco de dados + Python

Ser parte de um projeto extensionista da Estácio

🧑‍💻 Autor

Adail Queiroz
Projeto acadêmico – Estácio
Fortaleza – 2025
