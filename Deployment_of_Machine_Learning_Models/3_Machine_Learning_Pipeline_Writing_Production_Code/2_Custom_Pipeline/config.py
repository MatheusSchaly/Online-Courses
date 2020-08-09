PATH_TO_DATASET = "houseprice.csv"
                     
TARGET = 'SalePrice'

CATEGORICAL_TO_IMPUTE = ['MasVnrType', 'BsmtQual', 'BsmtExposure',
                         'FireplaceQu', 'GarageType', 'GarageFinish']

NUMERICAL_TO_IMPUTE = ['LotFrontage']

YEAR_VARIABLE = 'YearRemodAdd'

NUMERICAL_LOG = ['LotFrontage', '1stFlrSF', 'GrLivArea', 'SalePrice']

CATEGORICAL_ENCODE = ['MSZoning', 'Neighborhood', 'RoofStyle',
                      'MasVnrType', 'BsmtQual', 'BsmtExposure',
                      'HeatingQC', 'CentralAir', 'KitchenQual',
                      'FireplaceQu', 'GarageType', 'GarageFinish',
                      'PavedDrive']

FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood', 'OverallQual',
           'OverallCond', 'YearRemodAdd', 'RoofStyle', 'MasVnrType',
           'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
           '1stFlrSF', 'GrLivArea', 'BsmtFullBath', 'KitchenQual',
           'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageFinish',
           'GarageCars', 'PavedDrive', 'LotFrontage']
