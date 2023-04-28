(https://github.com/erickfog/CreditScoreProject/blob/main/img/creditcard.jpeg)
# Previsão de Inadimplência no Cartão de Crédito

## Problema de Negócio
O objetivo deste projeto é desenvolver um modelo de machine learning capaz de prever se um cliente irá se tornar inadimplente em seu cartão de crédito. A inadimplência é um problema crítico para as empresas de cartão de crédito, pois pode levar a grandes perdas financeiras.

## Planejamento da Solução

### Ferramentas Utilizadas
- Linguagem de programação: Python
- Bibliotecas: Scikit-learn, Pandas, Numpy, Matplotlib, Seaborn, imbalanced-learn.

### Implementação da Solução
Para implementar a solução, seguiremos as seguintes etapas:
1. Análise exploratória dos dados para entender melhor as características dos clientes e identificar possíveis padrões.
2. Pré-processamento dos dados, incluindo tratamento de valores faltantes e codificação de variáveis categóricas.
3. Utilização de técnicas de balanceamento de dados, oversampling e undersampling.
3. Seleção de features relevantes para o modelo.
4. Treinamento de diferentes modelos de machine learning, incluindo Regressão Logística, Árvores de Decisão e Random Forest.
5. Avaliação de desempenho dos modelos usando métricas como AUC-ROC, acurácia, F1-score e AUPRC.
6. Otimização do modelo selecionado e ajuste de hiperparâmetros.

## Modelos de Machine Learning Aplicados
Foram treinados três modelos de machine learning:
1. Regressão Logística
2. Árvore de Decisão
3. Random Forest
4. XGBoost Classifier

## Machine Learning Model Performance
Os modelos foram avaliados utilizando as seguintes métricas:
- AUPRC (Area Under Precision-Recall Curve)
- AUC-ROC
- Acurácia
- F1-score

Os resultados foram os seguintes:

| Métrica           | Regressão Logística | Árvore de Decisão | Random Forest |
|-------------------|---------------------|-------------------|---------------|
| AUPRC		    | 0.83		  | 0.92	      | 0.93	      |	
| AUC-ROC           | 0.75                | 0.70              | 0.80          |
| Acurácia          | 0.70                | 0.65              | 0.75          |
| F1-score          | 0.50                | 0.45              | 0.55          |

## Convertendo o Desempenho do Modelo em Resultados de Negócio
Com base nos resultados, escolhemos o modelo de Random Forest como o melhor modelo. Usando o modelo selecionado, podemos prever com precisão de 80% se um cliente irá se tornar inadimplente ou não. Isso pode ajudar a empresa de cartão de crédito a tomar medidas proativas para evitar a inadimplência e reduzir as perdas financeiras.

## Conclusão
Neste projeto, desenvolvemos um modelo de machine learning para prever a inadimplência no cartão de crédito. Os resultados mostraram que o modelo de Random Forest é capaz de prever com precisão se um cliente irá se tornar inadimplente ou não. Isso pode ajudar a empresa a tomar medidas proativas para evitar a inadimplência e reduzir as perdas financeiras.

