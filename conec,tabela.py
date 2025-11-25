import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# CONEXÃO COM O BANCO DE DADOS
# ===============================
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha123",
    database="seguranca_fortaleza"
)

print("✔ Conectado ao banco!")

query = """
SELECT bairro, indice_risco_estimado
FROM bairros
WHERE indice_risco_estimado IS NOT NULL
ORDER BY indice_risco_estimado DESC;
"""

df = pd.read_sql(query, con)

con.close()

print("✔ Dados carregados:", len(df), "bairros")

# ===============================
# GERAR GRÁFICO
# ===============================

plt.figure(figsize=(14, 10))
plt.barh(df["bairro"], df["indice_risco_estimado"])

plt.xlabel("Índice de Risco Estimado")
plt.ylabel("Bairros")
plt.title("Índice de Risco por Bairro - Fortaleza")
plt.gca().invert_yaxis()  # Bairros mais perigosos no topo

plt.tight_layout()

# Salvar imagem
plt.savefig("grafico_risco_bairros.png", dpi=300)

plt.show()

print("✔ Gráfico salvo como 'grafico_risco_bairros.png'")
