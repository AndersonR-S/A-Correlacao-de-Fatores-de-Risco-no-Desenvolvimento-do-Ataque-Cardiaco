import os

import processData
import processGrafo

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
    
    df = processData.download_data(output_dir)
    df = processData.preprocess_data(df, columns_nodes)
    df.columns = columns_upgrade_name  
    df.to_csv(f"{output_dir}/heart_attack_modeling.csv", index=False)

    correlation_matrix = processGrafo.save_correlation_matrix(df, output_dir, output_img)

    nodes_df = processGrafo.generate_nodes(df)
    nodes_df.to_csv(f"{output_dir}/nodes.csv", index=False)

    edges_df = processGrafo.generate_edges(correlation_matrix, nodes_df)
    edges_df.to_csv(f"{output_dir}/edges.csv", index=False)

    print("Processamento finalizado. Dados salvos em:", output_dir)

if __name__ == "__main__":
    main()
