Esse arquivo tem função de mostrar quais dados foram precisos limitar para ter uma eficiência e otimização.


### Niveis de Colesterol

De acordo com a Diretriz Brasileira de Hipercolesterolemia Familiar de 2021, o nível de colesterol que é associado a a risco elevado de doença aterosclerótica cardiovascular (DAC) é 190 mg/dl ou mais.

Com a modelagem dos dados do colesterol, todos os dados que não tenha 190 ou mais de colesterol será retirado.

**Fonte da Diretriz**

Izar, M.C.O., et al. Atualização da Diretriz Brasileira de Hipercolesterolemia Familiar – 2021. Arq Bras Cardiol. 2021; 117(4):782-844. Disponível em: DOI https://doi.org/10.36660/abc.20210788


###  Niveis de IMC

**Categorias de IMC para adultos**

* Subpeso é um IMC inferior a 18,5
* Peso saudável é um IMC de 18,5 a 24,9
* Excesso de peso é um IMC de 25 a 29,9
* Obesidade é um IMC de 30 ou acima

Para uma análise mais precisa dos riscos associados ao excesso de peso, este estudo se concentrará em indivíduos adultos (25 anos ou mais). A utilização de tabelas de IMC específicas para adultos é mais adequada, uma vez que as crianças e adolescentes apresentam curvas de crescimento distintas e requerem um cálculo de IMC adaptado. A decisão de focar nos adultos também é embasada nos achados do National Institutes of Health (NIH), que demonstram uma forte correlação entre o excesso de peso nessa faixa etária e o desenvolvimento de doenças cardiovasculares.

A modelagem dos dados de IMC, será com a condição de se for maior ou igual a 25 permanecerá, se não será apagado.

National Heart, Lung, and Blood Institute. (n.d.). Causes and Risk Factors. In Overweight and Obesity. National Institutes of Health (NIH). https://www.nhlbi.nih.gov/health/overweight-and-obesity/causes


### Niveis do Alcolismo
A Organização Mundial da Saúde (OMS) recomenda que os homens não consumam mais de 40 gramas de álcool puro por dia e as mulheres mais de 20 gramas.

A Modelagem do necessita de duas colunas o gênero e o consumo, haverá condições de se for homem e consumo é maior ou igual a 40 gramas ou mulher e consumo é maior ou igual a 20 gramas, representa qe eles são alcoólatras.
Por simplicidade, consideramos que 25 gramas sera o limite inferior, se for menos terá que ser removido.

Referencias

Rehm, J., & Monteiro, M. (2005). Alcohol consumption and burden of disease in the Americas: implication

Regional Status Report on Alcohol and Health 2020. Washington, D.C.: Pan American Health Organization; 2020. License: CC BY-NC-SA 3.0 IGO.
https://iris.paho.org/handle/10665.2/52705