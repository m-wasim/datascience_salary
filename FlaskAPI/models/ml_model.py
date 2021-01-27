import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer


def pipeline_transformer(data):
    
    num_attribs=['Carpet Area (ft²)','Maintenance (Monthly)','Total floor','bedroom','bathroom']
    cat_attribs=['Type','furnishing','facing','state']
    #num_attrs, num_pipeline = num_pipeline_transformer(data)
    num_pipeline=Pipeline([('std_scaler',StandardScaler())])
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
        ])
    full_pipeline.fit(data)
    return full_pipeline

def predict_rent(config, model):
    
    if type(config) == dict:
        df = pd.DataFrame(config)
    else:
        df = config

    pipeline = pipeline_transformer(df)
    prepared_df = pipeline.transform(df)
    #print(len(prepared_df[0]))
    #print(full_pipeline.named_transformers_['cat'].get_feature_names())
    y_pred = model.predict(prepared_df)
    return y_pred    