import mysql.connector
from difflib import get_close_matches

# Lista oficial de bairros de Fortaleza (IBGE + Prefeitura)
bairros_oficiais = [
    "Aldeota", "Meireles", "Cocó", "Centro", "Benfica", "Jangurussu", "Bom Jardim",
    "Mondubim", "Ancuri", "Prefeito José Walter", "Parangaba", "Itaperi",
    "Conjunto Ceará", "Genibaú", "Granja Portugal", "Granja Lisboa", "Serrinha",
    "Parquelândia", "Farias Brito", "Varjota", "Papicu", "Mucuripe", "Vicente Pinzon",
    "Praia do Futuro", "Barra do Ceará", "Carlito Pamplona", "Jacarecanga",
    "Cristo Redentor", "Jardim Iracema", "Jóquei Clube", "Demócrito Rocha",
    "Montese", "Maraponga", "Pici", "Bom Sucesso", "Autran Nunes",
    "Conjunto Esperança", "Passaré", "Barroso", "Dias Macedo", "Cambeba",
    "Cidade dos Funcionários", "Parque Iracema", "Sapiranga", "Sabiaguaba",
    "Messejana", "Curió", "Parque Santa Maria", "Cojáu", "Pedras", "Paupina",
    "Lagoa Redonda", "Guajeru", "Parque Dois Irmãos", "Parque Santana",
    "Jardim América", "Vila União", "Itaoca", "Canindezinho", "Jardim Guanabara",
    "Nova Assunção", "José de Alencar", "Luciano Cavalcante", "Planalto Ayrton Senna",
    "Floresta", "Alto da Balança", "Aeroporto", "Damas", "Vila Ellery",
    "Vila Peri", "Siqueira", "Antônio Bezerra", "Quintino Cunha", "Vila Velha",
    "Conjunto Palmeiras", "Tancredo Neves", "Edson Queiroz", "Guararapes",
    "Cidade 2000", "Beira Mar", "Curiú", "Parreão", "Araxá", "São José",
    "Fátima", "Sapiranga 2", "Passaré 2", "Dionísio Torres"
]

# Conexão
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha123",
    database="seguranca_fortaleza"
)
cursor = conn.cursor()

cursor.execute("SELECT id, bairro FROM bairros;")
rows = cursor.fetchall()

corrigidos = 0

for row in rows:
    id_, nome = row
    nome_original = nome

    # tenta casar com bairro oficial
    match = get_close_matches(nome, bairros_oficiais, n=1, cutoff=0.6)

    if match:
        nome_corrigido = match[0]

        if nome_corrigido != nome_original:
            cursor.execute(
                "UPDATE bairros SET bairro = %s WHERE id = %s",
                (nome_corrigido, id_)
            )
            corrigidos += 1
            print(f"✔ Corrigido: {nome_original} → {nome_corrigido}")

conn.commit()
conn.close()

print(f"\n🎉 Correção concluída! Total de nomes atualizados: {corrigidos}")
