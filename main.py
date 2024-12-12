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

    # Agrupar os dados por mês e contar as vendas
    vendas_por_mes = vendas_df.groupby(vendas_df['Data'].dt.month).size()

    # Criar o gráfico de barras
    plt.figure(figsize=(12, 6))
    plt.bar(vendas_por_mes.index, vendas_por_mes.values, color='purple', edgecolor='black')
    plt.xlabel("Mês")
    plt.ylabel("Quantidade Vendida")
    plt.title("Evolução Mensal das Vendas")
    plt.xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
               labels=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])

    # Definir os limites e os valores do eixo X
    plt.xlim(1, 12)  # Ajusta o limite do eixo x para mostrar todos os meses

    # Definir os limites e os valores do eixo y
    plt.ylim(1, 15)  # Limita o eixo y de 1 a 15
    plt.yticks(range(1, 16))  # Define os valores inteiros de 1 a 15 no eixo y

    plt.grid(axis='y')
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