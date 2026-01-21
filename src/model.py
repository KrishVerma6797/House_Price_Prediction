from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

def train_model(preprocessor,x_train,y_train):
    model=Pipeline([
        ('preprocessing',preprocessor),
        ('regressor',LinearRegression())
    ])
    model.fit(x_train,y_train)
    return model


from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_model(model,x_test,y_test):
    predictions=model.predict(x_test)
    mae=mean_absolute_error(y_test,predictions)
    rmse=np.sqrt(mean_squared_error(y_test,predictions))
    return mae,rmse