import numpy as np

import preprocessing_functions as pf
import config

import warnings
warnings.simplefilter(action='ignore')

# ================================================
# TRAINING STEP - IMPORTANT TO PERPETUATE THE MODEL

# Load data
data = pf.load_data(config.PATH_TO_DATASET)

# divide data set
X_train, X_test, y_train, y_test = pf.divide_train_test(data, config.TARGET)

# impute categorical variables
for var in config.CATEGORICAL_TO_IMPUTE:
    X_train[var] = pf.impute_na(X_train, var, replacement='Missing')


# impute numerical variable
X_train[config.NUMERICAL_TO_IMPUTE] = pf.impute_na(X_train,
       config.NUMERICAL_TO_IMPUTE,
       replacement=config.LOTFRONTAGE_MODE)


# capture elapsed time
X_train[config.YEAR_VARIABLE] = pf.elapsed_years(X_train,
       config.YEAR_VARIABLE, ref_var='YrSold')


# log transform numerical variables
for var in config.NUMERICAL_LOG:
    X_train[var] = pf.log_transform(X_train, var)


# Group rare labels
for var in config.CATEGORICAL_ENCODE:
    X_train[var] = pf.remove_rare_labels(X_train, var, config.FREQUENT_LABELS[var])


# encode categorical variables
for var in config.CATEGORICAL_ENCODE:
    X_train[var] = pf.encode_categorical(X_train, var,
           config.ENCODING_MAPPINGS[var])


# train scaler and save
scaler = pf.train_scaler(X_train[config.FEATURES],
                         config.OUTPUT_SCALER_PATH)

# scale train set
X_train = scaler.transform(X_train[config.FEATURES])

# train model and save
pf.train_model(X_train,
               np.log(y_train),
               config.OUTPUT_MODEL_PATH)

print('Finished training')