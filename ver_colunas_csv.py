import pandas as pd

CSV_PATH = r"C:\Users\SAMSUNG\OneDrive\Área de Trabalho\projeto_bigdata_fortaleza\seguranca_fortaleza_modelo_121bairros.csv"

df = pd.read_csv(CSV_PATH, encoding="latin1", sep=";", engine="python")

print("\n=== COLUNAS ENCONTRADAS NO CSV ===")
for col in df.columns:
    print(f"- '{col}'")
