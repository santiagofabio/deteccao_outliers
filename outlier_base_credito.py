def outlier_base_credito(base_credit):
     import plotly.express  as px
     import matplotlib.pyplot as plt
     from pyod.models.knn import KNN
     import matplotlib as mpl
     import pandas as pd 
     import numpy as np
     import os 
     mpl.rcParams['figure.figsize']=[10,6]
     
     print(base_credit.head(10))
     print(base_credit.isnull().sum())
 
     base_credit.dropna(inplace=True)
     print(base_credit.isnull().sum())
   
     #Grafco Age
     grafico =px.box(base_credit['age'] )
     grafico.write_image("outlier_base_credit_age.png")
     outliers_age = base_credit[base_credit["age"]<-20 ]
     print('Outliers Age:')
     print(outliers_age)
     
     grafico =px.box(base_credit['income'] )
     grafico.write_image("outlier_base_credit_income.png")
     
     grafico =px.box(base_credit['loan'] )
     grafico.write_image("outlier_base_credit_loan.png")
     print('Outliers Loan:')
     outliers_loan = base_credit[base_credit["loan"]>13300 ] 
     print(outliers_loan)
     
     
     #Grafco Income x Age
     grafico =px.scatter(base_credit,  x ="income", y="age")
     grafico.write_image("outlier_base_credit_income_vs_age.png")
    

     #Grafco Income x loan 
     grafico =px.scatter(base_credit, x="age", y="loan")
     grafico.write_image("outlier_base_credit_age_vs_loan.png")
     
     detector =KNN()
     detector.fit(base_credit.iloc[:,1:4])
     previsoes = detector.labels_

     print(np.unique(previsoes, return_counts=True ))

     cofianca_previsoes =detector.labels_
     print(cofianca_previsoes)

     outlier = list()

     n_registros =len(previsoes)

     for i in range(n_registros):
           if previsoes[i]==1:
               outlier.append(i)

     lista_outliers = base_credit.iloc[ outlier,: ]
     print(lista_outliers )
     
     
     return(0)


