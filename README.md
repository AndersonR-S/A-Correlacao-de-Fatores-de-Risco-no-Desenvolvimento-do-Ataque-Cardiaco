# A Correlação de Fatores de Risco no Desenvolvimento do Ataque Cardíaco

## 📂 Estrutura do Repositório

- [`article/`](https://github.com/AndersonR-S/A-Correlacao-de-Fatores-de-Risco-no-Desenvolvimento-do-Ataque-Cardiaco/blob/f984e1b716b09062a667492fd55b4f9f232a1e01/article/A_Correla%C3%A7%C3%A3o_de_Fatores_de_Risco_no_Desenvolvimento_do_Ataque_Card%C3%ADaco.pdf): Contém o artigo científico em formato em PDF.
- `src/`: Scripts Python utilizados para modelagem e análise dos grafos.
- `data/`: Arquivos CSV baixados e modelados
- `img/`: Imagens e gráficos gerados a partir dos experimentos.

## 📄 Objetivo
O trabalho consiste na aplicação de grafos em uma situação específica, sendo o problema principal *ataque cardíaco*. O objetivo é descobrir quais conjuntos de fatores de risco podem influenciar negativamente o desenvolvimento de ataques cardíacos.

A ideia geral da discussão é apresentada no artigo: <a href= "https://github.com/AndersonR-S/A-Correlacao-de-Fatores-de-Risco-no-Desenvolvimento-do-Ataque-Cardiaco/blob/f984e1b716b09062a667492fd55b4f9f232a1e01/article/A_Correla%C3%A7%C3%A3o_de_Fatores_de_Risco_no_Desenvolvimento_do_Ataque_Card%C3%ADaco.pdf">A Correlação de Fatores de Risco no Desenvolvimento do Ataque Cardíaco</a>.

## ⚙️ Compilação e Execução

Para executar o algoritmo de modelagem, é necessário instalar as seguintes bibliotecas em Python: 

    pandas -> Manipulação de dados 
    os -> Verificação de pasta
    kagglehub -> Download de arquivos
    seaborn -> Geração de tabela
    matplotlib -> Geração de imagem

Para instalar todas as dependências, utilize o seguinte comando:  

```bash
pip install pandas os kagglehub matplotlib seaborn
```

Após instalar as bibliotecas, basta digitar o comando abaixo no terminal, estando na pasta principal:

    python3 src/main.py


Para a visualização dos grafos citados e apresentados no artigo, é necessário a instalação do software Gephi. Seque o link abaixo para o download do aplicativo.



A visualização do grafo, é necessário importar o arquivo *correlation_matriz.csv* na pasta **data**, as configurações de implementação devem ser em matriz separado pela virgula.


## Ambiente de Execução
<table border="1">
  <tr> 
    <th>Sistema Operacional</th>
    <td>Ubuntu 22.04.5 LTS x86_64</td>
  </tr>
  <tr>
    <th>Compilador</th>
    <td>G++ 12.2.0</td>
  </tr>
  <tr>
    <th>Hardware</th>
    <td>Intel i5-7300HQ (4) @ 2.500GHz, 8GB RAM, 1TB HD</td>
  </tr>
</table>
