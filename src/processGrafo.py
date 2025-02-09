import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

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
