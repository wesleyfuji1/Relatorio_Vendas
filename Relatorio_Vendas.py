import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
file_path = "RELATÓRIO DE VENDAS(VENDAS).csv"  # Substitua pelo caminho correto
vendas_df = pd.read_csv(file_path, encoding='latin1', sep=';', skiprows=1)

# Remover colunas vazias e limpar espaços nos nomes das colunas
vendas_df = vendas_df.dropna(how='all', axis=1)
vendas_df.columns = vendas_df.columns.str.strip()

### 1. Modelos mais vendidos
if 'Modelo' in vendas_df.columns:
    vendas_por_modelo = vendas_df['Modelo'].value_counts()
    print("\nVendas por Modelo:\n", vendas_por_modelo)

    # Gerar gráfico de barras para modelos mais vendidos
    vendas_por_modelo.plot(kind='bar', title="Vendas por Modelo", color='skyblue')
    plt.xlabel("Modelo")
    plt.ylabel("Quantidade Vendida")
    plt.tight_layout()
    plt.show()
else:
    print("A coluna 'Modelo' não foi encontrada na planilha.")

### 2. Modalidade de pagamento mais utilizada
if 'Modalidade' in vendas_df.columns:
    pagamentos = vendas_df['Modalidade'].value_counts()
    print("\nModalidade de Pagamento:\n", pagamentos)

    # Gerar gráfico de pizza para modalidade de pagamento
    pagamentos.plot(kind='pie', autopct='%1.1f%%', title="Modalidade de Pagamento", ylabel="")
    plt.tight_layout()
    plt.show()
else:
    print("A coluna 'Modalidade de Pagamento' não foi encontrada na planilha.")

### 3. Evolução semanal das vendas (caso a coluna Data esteja presente)
if 'Data' in vendas_df.columns:
    # Converter a coluna 'Data' para o formato de data
    vendas_df['Data'] = pd.to_datetime(vendas_df['Data'], dayfirst=True)

    # Criar a coluna de número da semana
    vendas_df['Semana'] = vendas_df['Data'].dt.isocalendar().week

    # Evolução semanal das vendas
    vendas_por_semana = vendas_df.groupby('Semana').size()
    print("\nEvolução semanal:\n", vendas_por_semana)

    # Gerar gráfico de linha para evolução semanal
    vendas_por_semana.plot(kind='line', marker='o', title="Evolução Semanal das Vendas", color='green')
    plt.xlabel("Semana")
    plt.ylabel("Quantidade Vendida")
    plt.tight_layout()
    plt.show()
else:
    print("A coluna 'Data' não está presente na planilha. Adicione esta coluna para análise semanal.")


# Relatório dos modelos que mais vendem no consórcio

# Carregar o arquivo CSV
file_path2 = "RELATÓRIO DE VENDAS(Consórcio).csv"  # Substitua pelo caminho correto
vendas_cons = pd.read_csv(file_path2, encoding='latin1', sep=';', skiprows=1)

# Remover colunas vazias e limpar espaços nos nomes das colunas
vendas_cons = vendas_cons.dropna(how='all', axis=1)
vendas_cons.columns = vendas_cons.columns.str.strip()

### 1. Modelos mais vendidos
if 'Modelo' in vendas_cons.columns:
    vendas_por_modelo_cons = vendas_cons['Modelo'].value_counts()
    print("\nVendas por Modelo:\n", vendas_por_modelo_cons)

    # Gerar gráfico de barras para modelos mais vendidos
    vendas_por_modelo_cons.plot(kind='bar', title="Vendas por Modelo no Consórcio", color='darkorange')
    plt.xlabel("Modelo")
    plt.ylabel("Quantidade Vendida")
    plt.tight_layout()
    plt.show()
else:
    print("A coluna 'Modelo' não foi encontrada na planilha.")