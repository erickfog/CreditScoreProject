<div align="center">

![CreditScoreProject](https://github.com/erickfog/CreditScoreProject/blob/main/img/creditcard.jpg)
</div>

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

## Algortimos de Machine Learning Aplicados
Foram treinados os seguintes algortimos de machine learning:
1. Regressão Logística
2. Árvore de Decisão
3. Floresta Aleatória
4. XGBoost Classifier
5. Extra Trees Classifier
6. AdaBoost
7. KNN Classifier
8. Gradient Boosting
9. GaussianNB

Os modelos foram treinados de três formas diferentes: 
1. Utilizando o dataset desbalanceado. 
2. Utilizando o dataset balanceado com oversampling usando SMOTE. 
3. Utilizando o dataset balanceado com oversampling usando ADASYN. 

As performances do modelos serão apresentadas para as três diferentes formas que os modelos foram treinados.

## Machine Learning Model Performance (Unbalanced Dataset)
Os modelos foram avaliados utilizando as seguintes métricas:
- Average Precision Recall(AP)
- Precision Recall Curve

Os resultados foram os seguintes:


| Modelo              | Métrica (Average Precision Recall)|
|---------------------|-----------------------------------|
| Logistic Regression |	0.480149                          |
| KNN	              | 0.315004                          |
| Decision Tree	      | 0.300951                          |
| Random Forest	      | 0.530445			  |     
| Gradient Boosting   |	0.554870			  |
| AdaBoostClassifier  |	0.539499			  |
| GaussianNB	      | 0.482155                          |
| Extra Trees	      |	0.511844                          |
| XGBoosting	      |	0.527110                          |

## Machine Learning Model Performance (Balanced Dataset - SMOTE)

| Modelo              | Métrica (Average Precision Recall)|
|---------------------|-----------------------------------|
| Logistic Regression |	0.722913                  |
| KNN	              | 0.744800                  |
| Decision Tree	      | 0.699038                  |
| Random Forest	      | 0.919042            	  |     
| Gradient Boosting   |	0.848321		  |
| AdaBoostClassifier  |	0.811769		  |
| GaussianNB	      | 0.703378                  |
| Extra Trees	      |	0.927824                  |
| XGBoosting	      |	0.896304                  |


## Machine Learning Model Performance (Balanced Dataset - ADASYN)


| Modelo              | Métrica (Average Precision Recall)|
|---------------------|-----------------------------------|
| Logistic Regression |	0.703459                  |
| KNN	              | 0.732704                  |
| Decision Tree	      | 0.691625                  |
| Random Forest	      | 0.913831            	  |     
| Gradient Boosting   |	0.838238		  |
| AdaBoostClassifier  |	0.798553		  |
| GaussianNB	      | 0.683018                  |
| Extra Trees	      | 0.923480                  |
| XGBoosting	      |	0.891426                  |


## Convertendo o Desempenho do Modelo em Resultados de Negócio
Com base nos resultados, escolhemos o modelo de Random Forest como o melhor modelo. Usando o modelo selecionado, podemos prever com precisão de 90% se um cliente irá se tornar inadimplente ou não. Isso pode ajudar a empresa de cartão de crédito a tomar medidas proativas para evitar a inadimplência e reduzir as perdas financeiras, além de auxiliar no direcionamento das políticas de crédito.

## Conclusão
Neste projeto, desenvolvemos um modelo de machine learning para prever a inadimplência no cartão de crédito. Os resultados mostraram que o modelo de Random Forest treinado com os dados balanceados através de oversampling utilizando o SMOTE é capaz de prever com precisão se um cliente irá se tornar inadimplente ou não. Isso deve  ajudar a empresa a fazer o direcionamento de suas políticas de crédito e reduzir as perdas financeiras e ainda construir um score de crédito para cada cliente.

