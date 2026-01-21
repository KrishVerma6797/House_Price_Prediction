import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def preprocess_data(df,target_column):
    x = df.drop(columns=[target_column])
    y=df[target_column]

    num_cols=x.select_dtypes(include=['int64','float64']).columns
    cat_cols=x.select_dtypes(include=['object']).columns

    num_pipeline=Pipeline([
        ('imputer',SimpleImputer(strategy='median'))
    ])

    cat_pipeline=Pipeline([
        ('imputer',SimpleImputer(strategy='most_frequent')),
        ('encoder',OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor=ColumnTransformer([
        ('num',num_pipeline,num_cols),
        ('cat',cat_pipeline,cat_cols)
    ])

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    return preprocessor,x_train,x_test,y_train,y_test
