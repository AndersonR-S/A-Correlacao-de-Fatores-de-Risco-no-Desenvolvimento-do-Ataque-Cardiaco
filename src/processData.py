import kagglehub
import pandas as pd

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

    df = df[df["Age_Group"] != "Youth"]

    df = df[columns_nodes].copy()

    df['BMI'] = df['BMI'].apply(lambda x: 0 if x < 25 else 1)
    df['Alcohol_Consumption'] = df['Alcohol_Consumption'].apply(lambda x: 0 if x < 20 else 1)
    df['Cholesterol_Level'] = df['Cholesterol_Level'].apply(lambda x: 0 if x < 190 else 1)
    df['Stress_Level'] = df['Stress_Level'].apply(lambda x: 1 if x == 'High' else 0)
    df['Physical_Activity_Level'] = df['Physical_Activity_Level'].apply(lambda x: 0 if x == 'High' else 1)
    df['Diet_Quality'] = df['Diet_Quality'].apply(lambda x: 1 if x == 'Poor' else 0)

    return df
