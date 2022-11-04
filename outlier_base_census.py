def outlier_base_census(base_census ):
     import plotly.express  as px
     from pyod.models.knn import KNN
     #Grafco Agexfinal-weight 
     #Grafco Income x Age
     #Grafco Agexfinal-weight
     grafico =px.scatter(base_census, x='age', y ='final-weight')
     grafico.write_image("outlier_base_census_age_vs_final.png")
     
    
     return(0)