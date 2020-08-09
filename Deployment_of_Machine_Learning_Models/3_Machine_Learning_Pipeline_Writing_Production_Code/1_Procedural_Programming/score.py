import preprocessing_functions as pf
import config

# =========== scoring pipeline =========

# impute categorical variables
def predict(data):
    
    # impute NA
    for var in config.CATEGORICAL_TO_IMPUTE:
        data[var] = pf.impute_na(data, var, replacement='Missing')
    
    data[config.NUMERICAL_TO_IMPUTE] = pf.impute_na(data,
           config.NUMERICAL_TO_IMPUTE,
           replacement=config.LOTFRONTAGE_MODE)
    
    
    # capture elapsed time
    data[config.YEAR_VARIABLE] = pf.elapsed_years(data,
           config.YEAR_VARIABLE, ref_var='YrSold')
    
    
    # log transform numerical variables
    for var in config.NUMERICAL_LOG:
       data[var] = pf.log_transform(data, var)
    
    
    # Group rare labels
    for var in config.CATEGORICAL_ENCODE:
        data[var] = pf.remove_rare_labels(data, var, config.FREQUENT_LABELS[var])
    
    # encode variables
    for var in config.CATEGORICAL_ENCODE:
        data[var] = pf.encode_categorical(data, var,
               config.ENCODING_MAPPINGS[var])
    
    
    # scale variables
    data = pf.scale_features(data[config.FEATURES],
                             config.OUTPUT_SCALER_PATH)
    
    # make predictions
    predictions = pf.predict(data, config.OUTPUT_MODEL_PATH)
    
    return predictions

# ======================================
    
# small test that scripts are working ok
    
if __name__ == '__main__':
    
    from math import sqrt
    import numpy as np
    
    from sklearn.metrics import mean_squared_error, r2_score
    
    import warnings
    warnings.simplefilter(action='ignore')
    
    # Load data
    data = pf.load_data(config.PATH_TO_DATASET)
    X_train, X_test, y_train, y_test = pf.divide_train_test(data,
                                                            config.TARGET)
    
    pred = predict(X_test)
    
    # determine mse and rmse
    print('test mse: {}'.format(int(
        mean_squared_error(y_test, np.exp(pred)))))
    print('test rmse: {}'.format(int(
        sqrt(mean_squared_error(y_test, np.exp(pred))))))
    print('test r2: {}'.format(
        r2_score(y_test, np.exp(pred))))
    print()
        