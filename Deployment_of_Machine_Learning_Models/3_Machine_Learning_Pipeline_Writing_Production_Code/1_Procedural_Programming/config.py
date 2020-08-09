# ====   PATHS ===================

PATH_TO_DATASET = "houseprice.csv"
OUTPUT_SCALER_PATH = 'scaler.pkl'
OUTPUT_MODEL_PATH = 'lasso_regression.pkl'



# ======= PARAMETERS ===============

# imputation parameters
LOTFRONTAGE_MODE = 60


# encoding parameters
FREQUENT_LABELS = {
    'MSZoning': ['FV', 'RH', 'RL', 'RM'],
    'Neighborhood': ['Blmngtn', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr',
                     'Crawfor', 'Edwards', 'Gilbert', 'IDOTRR', 'MeadowV',
                     'Mitchel', 'NAmes', 'NWAmes', 'NoRidge', 'NridgHt',
                     'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst',
                     'StoneBr', 'Timber'],
    'RoofStyle': ['Gable', 'Hip'],
    'MasVnrType': ['BrkFace', 'None', 'Stone'],
    'BsmtQual': ['Ex', 'Fa', 'Gd', 'Missing', 'TA'],
    'BsmtExposure': ['Av', 'Gd', 'Missing', 'Mn', 'No'],
    'HeatingQC': ['Ex', 'Fa', 'Gd', 'TA'],
    'CentralAir': ['N', 'Y'],
    'KitchenQual': ['Ex', 'Fa', 'Gd', 'TA'],
    'FireplaceQu': ['Ex', 'Fa', 'Gd', 'Missing', 'Po', 'TA'],
    'GarageType': ['Attchd', 'Basment', 'BuiltIn', 'Detchd', 'Missing'],
    'GarageFinish': ['Fin', 'Missing', 'RFn', 'Unf'],
    'PavedDrive': ['N', 'P', 'Y']}



ENCODING_MAPPINGS = {'MSZoning': {'Rare': 0, 'RM': 1, 'RH': 2, 'RL': 3, 'FV': 4},
                     'Neighborhood': {'IDOTRR': 0, 'MeadowV': 1, 'BrDale': 2, 'Edwards': 3,
                                      'BrkSide': 4, 'OldTown': 5, 'Sawyer': 6, 'SWISU': 7, 'NAmes': 8,
                                      'Mitchel': 9, 'SawyerW': 10, 'Rare': 11, 'NWAmes': 12, 'Gilbert': 13,
                                      'Blmngtn': 14, 'CollgCr': 15, 'Crawfor': 16, 'ClearCr': 17, 'Somerst': 18,
                                      'Timber': 19, 'StoneBr': 20, 'NridgHt': 21, 'NoRidge': 22},
                     'RoofStyle': {'Gable': 0, 'Rare': 1, 'Hip': 2},
                     'MasVnrType': {'None': 0, 'Rare': 1, 'BrkFace': 2, 'Stone': 3},
                     'BsmtQual': {'Missing': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4},
                     'BsmtExposure': {'Missing': 0, 'No': 1, 'Mn': 2, 'Av': 3, 'Gd': 4},
                     'HeatingQC': {'Rare': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4},
                     'CentralAir': {'N': 0, 'Y': 1},
                     'KitchenQual': {'Fa': 0, 'TA': 1, 'Gd': 2, 'Ex': 3},
                     'FireplaceQu': {'Po': 0, 'Missing': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
                     'GarageType': {'Missing': 0, 'Rare': 1, 'Detchd': 2, 'Basment': 3, 'Attchd': 4, 'BuiltIn': 5},
                     'GarageFinish': {'Missing': 0, 'Unf': 1, 'RFn': 2, 'Fin': 3},
                     'PavedDrive': {'N': 0, 'P': 1, 'Y': 2}}


# ======= FEATURE GROUPS =============
                     
# variable groups for engineering steps
TARGET = 'SalePrice'

CATEGORICAL_TO_IMPUTE = ['MasVnrType', 'BsmtQual', 'BsmtExposure',
                         'FireplaceQu', 'GarageType', 'GarageFinish']
NUMERICAL_TO_IMPUTE = 'LotFrontage'

YEAR_VARIABLE = 'YearRemodAdd'

# variables to transofmr
NUMERICAL_LOG = ['LotFrontage', '1stFlrSF', 'GrLivArea', 'SalePrice']


# variables to encode
CATEGORICAL_ENCODE = ['MSZoning', 'Neighborhood', 'RoofStyle',
                          'MasVnrType', 'BsmtQual', 'BsmtExposure',
                          'HeatingQC', 'CentralAir', 'KitchenQual',
                          'FireplaceQu', 'GarageType', 'GarageFinish',
                          'PavedDrive']


# selected features for training
FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood', 'OverallQual',
           'OverallCond', 'YearRemodAdd', 'RoofStyle', 'MasVnrType',
           'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
           '1stFlrSF', 'GrLivArea', 'BsmtFullBath', 'KitchenQual',
           'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageFinish',
           'GarageCars', 'PavedDrive', 'LotFrontage']
