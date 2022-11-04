import pandas as pd
import numpy as np
import plotly.express  as px
import matplotlib.pyplot as plt
import seaborn as sns 
from outlier_base_credito import  outlier_base_credito 
from outlier_base_census import outlier_base_census

# Base credito
file_credit_data ='credit_data.csv'
base_credit =pd.read_csv(file_credit_data,sep =',', encoding ='utf-8' )
outlier_base_credito(base_credit)


# Base census

file_census ='census.csv'
base_census =pd.read_csv(file_census,sep =',', encoding ='utf-8')
outlier_base_census(base_census)

