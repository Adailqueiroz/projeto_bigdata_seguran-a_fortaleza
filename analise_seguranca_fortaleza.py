# ===========================================
# Projeto de Big Data - Segurança Urbana Fortaleza
# Autor: Adail Queiroz
# ===========================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import mysql.connector
from mysql.connector import errorcode

# ===============================
# 1. Conexão com MySQL
# ===============================

print("🔌 Conectando ao MySQL...")

try:
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="senha123",
        database="seguranca_fortaleza"
    )
    cursor = con.cursor()
    print("✅ Conectado ao MySQL com sucesso!")

except mysql.connector.Error as err:
    print("❌ ERRO ao conectar ao MySQL:", err)
    exit()

# ===============================
# 2. Criar tabela caso não exista
# ===============================

tabela_sql = """
CREATE TABLE IF NOT EXISTS bairros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bairro VARCHAR(100),
    ocorrencias_2025 INT,
    classificacao VARCHAR(20)
);
"""

cursor.execute(tabela_sql)
print("🏗️ Tabela 'bairros' verificada/criada.")

# ===============================
# 3. Carregar CSV
# ===============================

caminho_csv = r"C:\Users\SAMSUNG\OneDrive\Área de Trabalho\projeto_bigdata_fortaleza\bairros_fortaleza_completo.csv"

print("\n📄 Lendo CSV:", caminho_csv)
df = pd.read_csv(caminho_csv, sep=";", encoding="latin1")

# Padronizar colunas
df.columns = [col.strip().lower() for col in df.columns]

# ===============================
# 4. Inserir dados no MySQL
# ===============================

print("📥 Inserindo dados no banco (aguarde)...")

cursor.execute("DELETE FROM bairros")  # limpa antes de inserir
con.commit()

sql_insert = """
INSERT INTO bairros (bairro, ocorrencias_2025, classificacao)
VALUES (%s, %s, %s)
"""

for _, linha in df.iterrows():
    valores = (linha['bairro'], int(linha['ocorrencias_2025']), linha['classificacao'])
    cursor.execute(sql_insert, valores)

con.commit()
print("✅ Dados inseridos com sucesso!")

# ===============================
# 5. Ler dados direto do MySQL para analisar
# ===============================

print("\n📊 Lendo dados do MySQL para análise...")
cursor.execute("SELECT bairro, ocorrencias_2025, classificacao FROM bairros")
dados_mysql = cursor.fetchall()

df = pd.DataFrame(dados_mysql, columns=["Bairro", "Ocorrencias_2025", "Classificacao"])

# ===============================
# 6. Preparar dados
# ===============================

df['Bairro'] = df['Bairro'].astype(str).str.upper()
df_ordenado = df.sort_values(by="Ocorrencias_2025", ascending=False)

# ===============================
# 7. Gráfico geral por bairro
# ===============================

cores = plt.cm.RdYlGn_r(df_ordenado['Ocorrencias_2025'] / df_ordenado['Ocorrencias_2025'].max())

plt.figure(figsize=(12, 7))
barras = plt.bar(df_ordenado['Bairro'], df_ordenado['Ocorrencias_2025'], color=cores, edgecolor='black')

plt.title("📊 Análise de Segurança Urbana - Fortaleza (2025)", fontsize=16, fontweight='bold')
plt.xlabel("Bairros de Fortaleza")
plt.ylabel("Número de Ocorrências")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

for barra in barras:
    y = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, y + 5, int(y), ha='center', fontsize=8)

plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
plt.tight_layout()
plt.show()

# ===============================
# 8. Gráficos de perigosos e seguros
# ===============================

perigosos = df[df["Classificacao"].str.upper() == "PERIGOSO"]
seguros = df[df["Classificacao"].str.upper() == "SEGURO"]

plt.figure(figsize=(10, 6))
plt.bar(perigosos['Bairro'], perigosos['Ocorrencias_2025'], color='crimson')
plt.title("🚨 Bairros Mais Perigosos de Fortaleza (2025)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(seguros['Bairro'], seguros['Ocorrencias_2025'], color='mediumseagreen')
plt.title("🛡️ Bairros Mais Seguros de Fortaleza (2025)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print("\n✅ Análise finalizada com sucesso!")
