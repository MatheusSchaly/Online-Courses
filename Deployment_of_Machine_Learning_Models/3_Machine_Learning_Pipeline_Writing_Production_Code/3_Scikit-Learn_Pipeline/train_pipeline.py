import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
import joblib

import pipeline
import config


def run_training():
    """Train the model."""

    # read training data
    data = pd.read_csv(config.TRAINING_DATA_FILE)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.1,
        random_state=0)  # we are setting the seed here

    # transform the target
    y_train = np.log(y_train)
    y_test = np.log(y_test)

    pipeline.price_pipe.fit(X_train[config.FEATURES], y_train)
    joblib.dump(pipeline.price_pipe, config.PIPELINE_NAME)


if __name__ == '__main__':
    run_training()
