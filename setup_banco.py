# ===========================================
# SETUP DO BANCO DE DADOS - SEGURANÇA FORTALEZA
# Criação do banco, tabela e importação do CSV
# ===========================================

import mysql.connector
import pandas as pd
import os

print("\n=== INICIANDO SETUP DO BANCO DE DADOS ===")

# -----------------------------
# CONFIGURAÇÕES DO BANCO
# -----------------------------
HOST = "localhost"
USER = "root"
PASSWORD = "senha123"
DATABASE = "seguranca_fortaleza"

CSV_PATH = r"C:\Users\SAMSUNG\OneDrive\Área de Trabalho\projeto_bigdata_fortaleza\seguranca_fortaleza_modelo_121bairros.csv"


# -----------------------------
# 1. CONECTAR AO MYSQL (SEM BANCO)
# -----------------------------
print("\n🔌 Conectando ao MySQL (sem banco)...")
conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD
)
print("✔ Conexão OK!")
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE};")
cursor.close()
conn.close()
print(f"✔ Banco verificado/criado: {DATABASE}")


# -----------------------------
# 2. CONECTAR AO BANCO
# -----------------------------
print(f"\n🔌 Conectando ao banco: {DATABASE}")
conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)
cursor = conn.cursor()
print("✔ Conectado ao banco!")


# -----------------------------
# 3. RECRIAR TABELA
# -----------------------------
print("\n📄 Removendo tabela antiga (se existir)...")
cursor.execute("DROP TABLE IF EXISTS bairros;")
conn.commit()
print("✔ Tabela antiga removida.")

print("📄 Criando tabela 'bairros'...")

cursor.execute("""
    CREATE TABLE bairros (
        id INT AUTO_INCREMENT PRIMARY KEY,
        bairro VARCHAR(255),
        ocorrencias_2025 INT,
        mortes_2025 INT,
        classificacao VARCHAR(255),
        populacao_2022 INT,
        idh_bairro VARCHAR(20),
        indice_risco_estimado FLOAT,
        observacoes TEXT,
        fonte VARCHAR(255)
    );
""")

conn.commit()
print("✔ Tabela criada com sucesso!")


# -----------------------------
# 4. CARREGAR CSV
# -----------------------------
print(f"\n📥 Lendo CSV: {CSV_PATH}")
df = pd.read_csv(CSV_PATH, encoding="latin1", sep=";", engine="python")

# normalizar nomes das colunas
df.columns = [c.strip().lower() for c in df.columns]

print("✔ CSV carregado. Linhas:", len(df))


# -----------------------------
# 5. INSERIR DADOS
# -----------------------------
print("\n🧹 Importando dados para o MySQL...")

insert_sql = """
    INSERT INTO bairros (
        bairro, ocorrencias_2025, mortes_2025, classificacao, populacao_2022,
        idh_bairro, indice_risco_estimado, observacoes, fonte
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

for _, row in df.iterrows():

    cursor.execute(insert_sql, (
        row["bairro"],
        None if pd.isna(row["ocorrencias_2025"]) else int(row["ocorrencias_2025"]),
        None if pd.isna(row["mortes_2025"]) else int(row["mortes_2025"]),
        row["classificacao"],
        None if pd.isna(row["populacao_2022"]) else int(row["populacao_2022"]),
        row["idh_bairro"],
        None if pd.isna(row["indice_risco_estimado"]) else float(row["indice_risco_estimado"]),
        row["observacoes"],
        row["fonte"]
    ))

conn.commit()
print("✔ Importação concluída!")


# -----------------------------
# 6. VERIFICAR
# -----------------------------
cursor.execute("SELECT COUNT(*) FROM bairros")
total = cursor.fetchone()[0]
print(f"\n📊 Total de registros no banco: {total}")

cursor.close()
conn.close()

print("\n🎉 SETUP FINALIZADO COM SUCESSO!")
