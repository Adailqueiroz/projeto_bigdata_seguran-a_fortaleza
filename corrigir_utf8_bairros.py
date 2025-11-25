import mysql.connector

print("\n=== CORRIGINDO NOME DOS BAIRROS (DECODIFICAÇÃO AUTOMÁTICA) ===")

# ----------------------------
# CONEXÃO COM O BANCO
# ----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha123",
    database="seguranca_fortaleza"
)
cursor = conn.cursor()

# ----------------------------
# BUSCAR TODOS OS BAIRROS
# ----------------------------
cursor.execute("SELECT id, bairro FROM bairros;")
bairros = cursor.fetchall()

def corrigir_texto_quebrado(texto):
    """
    Tenta corrigir texto com acentuação quebrada,
    aplicando dupla conversão utf-8/latin-1.
    """
    try:
        # Reinterpreta a string como se tivesse sido lida errado
        return texto.encode('latin1').decode('utf8')
    except:
        try:
            # Tentativa reversa
            return texto.encode('utf8').decode('latin1')
        except:
            # Se não corrigir, retorna original
            return texto


correcoes = 0

# ----------------------------
# PROCESSAR CORREÇÕES
# ----------------------------
for id_bairro, nome in bairros:

    nome_corrigido = corrigir_texto_quebrado(nome)

    # Só atualiza se realmente mudou
    if nome_corrigido != nome:
        cursor.execute(
            "UPDATE bairros SET bairro = %s WHERE id = %s;",
            (nome_corrigido, id_bairro)
        )
        correcoes += 1
        print(f"✔ Corrigido: '{nome}' → '{nome_corrigido}'")

# Salvar alterações
conn.commit()

print("\n--------------------------------------")
print(f"✅ Total de nomes corrigidos: {correcoes}")
print("--------------------------------------\n")

cursor.close()
conn.close()

print("🎉 Correção automática finalizada!")
