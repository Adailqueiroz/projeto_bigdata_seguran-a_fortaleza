import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --------------------------
# CONEXÃO COM O BANCO
# --------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha123",
    database="seguranca_fortaleza",
    charset="utf8mb4",
    collation="utf8mb4_unicode_ci"
)

query = """
    SET NAMES utf8mb4;
"""
cursor = conn.cursor()
cursor.execute(query)

query = "SELECT bairro, ocorrencias_2025, mortes_2025, indice_risco_estimado FROM bairros ORDER BY ocorrencias_2025 DESC;"
df = pd.read_sql(query, conn)
conn.close()

print("✔ Dados carregados:", len(df), "bairros")

# ===============================
# CONFIG VISUAL DOS GRÁFICOS
# ===============================
plt.style.use("ggplot")

def salvar_grafico(titulo, x, y, rotulo_y, nome_arquivo):
    plt.figure(figsize=(18, 9))
    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.title(titulo, fontsize=20, fontweight="bold")
    plt.ylabel(rotulo_y, fontsize=14)
    plt.tight_layout()
    plt.savefig(nome_arquivo, dpi=300)
    plt.close()
    print(f"✔ Gráfico salvo: {nome_arquivo}")


# ===============================
# GRÁFICO 1 - OCORRÊNCIAS
# ===============================
salvar_grafico(
    "Ocorrências por Bairro (2025)",
    df["bairro"],
    df["ocorrencias_2025"],
    "Total de Ocorrências",
    "grafico_ocorrencias.png"
)

# ===============================
# GRÁFICO 2 - MORTES
# ===============================
salvar_grafico(
    "Mortes por Bairro (2025)",
    df["bairro"],
    df["mortes_2025"],
    "Total de Mortes",
    "grafico_mortes.png"
)

# ===============================
# GRÁFICO 3 - ÍNDICE DE RISCO
# ===============================
salvar_grafico(
    "Índice de Risco Estimado por Bairro (2025)",
    df["bairro"],
    df["indice_risco_estimado"],
    "Índice de Risco",
    "grafico_indice_risco.png"
)

print("\n🎉 Todos os gráficos foram gerados com sucesso!")
