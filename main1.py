import pandas as pd
import numpy as np
df=pd.read_csv('data/Housing.csv')
# print(df.head())
# print(df.info())
# print(df.isnull().sum())

from src.preprocessing import preprocess_data
from src.model import train_model,evaluate_model
from src.predict import predict_price

preprocessor,x_train,x_test,y_train,y_test=preprocess_data(df,target_column='price')
model=train_model(preprocessor,x_train,y_train)
mae,rmse=evaluate_model(model,x_test,y_test)
print(f'Mean Absolute Error: {mae}')
print(f'Root Mean Squared Error: {rmse}')
predict_price(model)