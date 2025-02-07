import pandas as pd
import os
import kagglehub
import seaborn as sns
import matplotlib.pyplot as plt


def download_data(output_dir):
    """Baixa o conjunto de dados e salva na pasta especificada."""
    path = kagglehub.dataset_download("ankushpanday1/heart-attack-in-youth-vs-adult-in-germany")
    print("Path to dataset files:", path)

    df = pd.read_csv(path + "/heart_attack_germany.csv")
    df.to_csv(f"{output_dir}/heart_attack_germany.csv", index=False)
    return df

def preprocess_data(df, columns_nodes):
    """Filtra e transforma as colunas do DataFrame."""
    missing_columns = [col for col in columns_nodes if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Colunas ausentes no DataFrame: {missing_columns}")

    # Remover as linhas que possuem "Youth" na coluna "BMI"
    df = df[df["Age_Group"] != "Youth"]

    df = df[columns_nodes].copy()

    # Transformações
    df['BMI'] = df['BMI'].apply(lambda x: 0 if x < 25 else 1)
    df['Alcohol_Consumption'] = df['Alcohol_Consumption'].apply(lambda x: 0 if x < 20 else 1)
    df['Cholesterol_Level'] = df['Cholesterol_Level'].apply(lambda x: 0 if x < 190 else 1)
    df['Stress_Level'] = df['Stress_Level'].apply(lambda x: 1 if x == 'High' else 0)
    df['Physical_Activity_Level'] = df['Physical_Activity_Level'].apply(lambda x: 0 if x == 'High' else 1)
    df['Diet_Quality'] = df['Diet_Quality'].apply(lambda x: 1 if x == 'Poor' else 0)

    return df


def save_correlation_matrix(df, output_dir, output_img):
    """Calcula e salva a matriz de correlação como CSV e PNG."""
    correlation_matrix = df.corr()

    for i in range(correlation_matrix.shape[0]):
        for j in range(correlation_matrix.shape[1]):
            if correlation_matrix.iloc[i, j] < 0:
                correlation_matrix.iloc[i, j] = 0

    correlation_matrix.to_csv(f"{output_dir}/correlation_matriz.csv")

    plt.figure(figsize=(10, 8))  
    sns.heatmap(
        correlation_matrix, 
        annot=True, 
        cmap="coolwarm", 
        fmt=".4f", 
        linewidths=0.5
    )
    plt.title("Matriz de Correlação (Coeficiente de Pearson)")
    plt.tight_layout()

    plt.savefig(f"{output_img}/correlation_matrix.png", dpi=300)
    plt.close()

    return correlation_matrix

def generate_nodes(df):
    """Gera os nós para o grafo."""
    nodes = []
    seen_nodes = set()
    node_id = 0

    for column in df.columns:
        if column not in seen_nodes:
            nodes.append({"Id": node_id, "Label": column, "Description": column})
            seen_nodes.add(column)
            node_id += 1

    return pd.DataFrame(nodes)

def generate_edges(correlation_matrix, nodes_df):
    """Gera as arestas para o grafo com base na matriz de correlação."""
    edges = []
    for i, col1 in enumerate(correlation_matrix.columns):
        for j, col2 in enumerate(correlation_matrix.columns):
            if i < j:  # Evitar duplicações
                from_node = nodes_df[nodes_df['Label'] == col1].iloc[0]['Id']
                to_node = nodes_df[nodes_df['Label'] == col2].iloc[0]['Id']
                weight = correlation_matrix.loc[col1, col2]
                edges.append({"Source": from_node, "Target": to_node, "Type": 'Undirected', "Weight": weight})

    return pd.DataFrame(edges)

def main():
    output_dir = "data"
    output_img = "img"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(output_img, exist_ok=True)

    columns_nodes = [
        "Heart_Attack_Incidence", 
        "BMI", 
        "Alcohol_Consumption", 
        "Physical_Activity_Level", 
        "Diet_Quality", 
        "Family_History", 
        "Hypertension", 
        "Cholesterol_Level", 
        "Diabetes", 
        "Stress_Level"
    ] 

    columns_upgrade_name = [
        "Incidência de Ataque Cardíaco",
        "IMC",
        "Consumo de Álcool",
        "Nível de Atividade Física",
        "Qualidade da Dieta",
        "Histórico Familiar",
        "Hipertensão",
        "Nível de Colesterol",
        "Diabetes",
        "Nível de Estresse"
    ]
    
    # Download e pré-processamento
    df = download_data(output_dir)
    df = preprocess_data(df, columns_nodes)
    df.columns = columns_upgrade_name  
    df.to_csv(f"{output_dir}/heart_attack_modeling.csv", index=False)

    # Matriz de correlação
    correlation_matrix = save_correlation_matrix(df, output_dir, output_img)

    # Gerar nós e arestas
    nodes_df = generate_nodes(df)
    nodes_df.to_csv(f"{output_dir}/nodes.csv", index=False)

    edges_df = generate_edges(correlation_matrix, nodes_df)
    edges_df.to_csv(f"{output_dir}/edges.csv", index=False)

    print("Processamento finalizado. Dados salvos em:", output_dir)

if __name__ == "__main__":
    main()
