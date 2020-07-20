# Importing the dataset
dataset = read.csv('Churn_Modelling.csv')
dataset = dataset[4:14]

# Econding the categorical variables as factor
dataset$Geography = as.numeric(factor(dataset$Geography),
                               levels = c('France', 'Spain', 'Germany'),
                               labels = c(1, 2, 3))
dataset$Gender = as.numeric(factor(dataset$Gender),
                            levels = c('Female', 'Male'),
                            labels = c(1, 2))

# Spltting the dataset
library(caTools)
set.seed(123)
split = sample.split(dataset$Exited, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature scaling
training_set[-11] = scale(training_set[-11])
test_set[-11] = scale(test_set[-11])

# Fitting Deep Feed Forward (DFF) Neural Network (NN)
# install.packages('h2o')
library(h2o)
h2o.init(nthreads = -1)
classifier = h2o.deeplearning(y = 'Exited',
                              training_frame = as.h2o(training_set),
                              activation = 'Rectifier',
                              hidden = c(6, 6),
                              epochs = 100,
                              train_samples_per_iteration = -2)

# Predicting using the test set
prob_pred = h2o.predict(classifier, newdata = as.h2o(test_set[-11]))
y_pred = (prob_pred > 0.5)
y_pred = as.vector(y_pred)

# Evaluating the model
cm = table(test_set[, 11], y_pred > 0.5)

# Disconnect from the h2o server
h2o.shutdown()
