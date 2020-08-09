import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Lasso

import joblib


# Individual pre-processing and training functions
# ================================================

def load_data(df_path):
    # Function loads data for training
    return pd.read_csv(df_path)



def divide_train_test(df, target):
    # Function divides data set in train and test
    X_train, X_test, y_train, y_test = train_test_split(df,
                                                        df[target],
                                                        test_size=0.1,
                                                        random_state=0)
    return X_train, X_test, y_train, y_test



def impute_na(df, var, replacement='Missing'):
    # function replaces NA by value entered by user
    # or by string Missing (default behaviour)
    return df[var].fillna(replacement)



def elapsed_years(df, var, ref_var='YrSold'):
    # captures difference between a year variable
    # and a reference variable 
    #(year in which the house was sold by default)
    
    df[var] = df[ref_var] - df[var]
    return df



def log_transform(df, var):
    # apply logarithm transformation to variable
    return np.log(df[var])



def remove_rare_labels(df, var, frequent_labels):
    # groups labels that are not in the frequent list into the umbrella
    # group Rare
    return np.where(df[var].isin(frequent_labels), df[var], 'Rare')



def encode_categorical(df, var, mappings):
    # replaces strings by numbers using mappings dictionary
    return df[var].map(mappings)



def train_scaler(df, output_path):
    scaler = MinMaxScaler()
    scaler.fit(df)
    joblib.dump(scaler, output_path)
    return scaler
  
    

def scale_features(df, scaler):
    scaler = joblib.load(scaler) # with joblib probably
    return scaler.transform(df)



def train_model(df, target, output_path):
    # initialise the model
    lin_model = Lasso(alpha=0.005, random_state=0)
    
    # train the model
    lin_model.fit(df, target)
    
    # save the model
    joblib.dump(lin_model, output_path)
    
    return None



def predict(df, model):
    model = joblib.load(model)
    return model.predict(df)

