from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

import preprocessors as pp
import config


titanic_pipe = Pipeline([
	('extract_first_letter', pp.ExtractFirstLetter(variables=config.CABIN)),
	('missing_indicator', pp.MissingIndicator(variables=config.NUMERICAL_VARS)),
	('numerical_imputer', pp.NumericalImputer(variables=config.NUMERICAL_VARS)),
	('categorical_imputer', pp.CategoricalImputer(variables=config.CATEGORICAL_VARS)),
	('rare_labels_categorical_encoder', pp.RareLabelCategoricalEncoder(variables=config.CATEGORICAL_VARS, tol=0.05)),
	('categorical_encoder', pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
	('standard_scaler', StandardScaler()),
	('logistic_regression', LogisticRegression(C=0.0005, random_state=0))
])