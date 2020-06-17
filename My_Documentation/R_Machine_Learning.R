### Data Preprocessing

# Importing the dataset
dataset = read.csv('name.csv')

# Missing data
dataset$col_name = ifelse(is.na(dataset$col_name),
                          ave(dataset$col_name, FUN = function(x) mean(x, na.rm = TRUE)),
                          dataset$col_name)

# Encoding categorical data
dataset$col_name = factor(dataset$col_name,
                         levels = c('string_name_1', 'string_name_2'),
                         labels = c(1, 2))

# Encoding the label
dataset$y_col_name = factor(dataset$y_col_name, level = c(0, 1))

# Splitting the dataset into the Training set and Test set
library(caTools)
split = sample.split(dataset$y_col_name, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
training_set[, col_index_1:col_index_2] = scale(training_set[, col_index_1:col_index_2])
test_set[, col_index_1:col_index_2] = scale(test_set[, col_index_1:col_index_2])

# Retrieving model summary after fitting it
summary(model_name)

### Machine Learning models

## Simple/Multiple Linear Regression

# No need for feature scaling
# Linear
# Continuous

# Fitting
regressor = lm(formula = y_col_name ~ .,
               data = training_set)

# Predicting
y_pred = predict(regressor, newdata = test_set)

# Visualising the training set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$x, y = training_set$y),
             colour = 'red') +
  geom_line(aes(x = training_set$x, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('y vs x (Training set)') +
  xlab('x') +
  ylab('y')

# Visualising the test set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$x, y = test_set$y),
             colour = 'red') +
  geom_line(aes(x = training_set$x, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('y vs x (Test set)') +
  xlab('x') +
  ylab('y')

# Predicting a new value
y_pred = predict(lin_reg, newdata = data.frame(x_col_name = predict_value))

## Polynomial Linear Regression

# No need for feature scaling
# Non-linear
# Continuous

# Fitting

dataset$col_name_2 = dataset$col_name^2
dataset$col_name_3 = dataset$col_name^3
regressor = lm(formula = y_col_name ~ .,
               data = training_set)

# Predicting a new value
y_pred = predict(regressor, newdata = data.frame(x_col_name_1 = predict_value,
                                                 x_col_name_2 = predict_value^2,
                                                 x_col_name_3 = predict_value^3,
                                                 x_col_name_4 = predict_value^4))

## Support Vector Regression

# Needs feature scaling
# Non-linear
# Continuous

# Fitting
library(e1071)
regressor = svm(formula = y_col_name ~ .,
                data = training_set,
                type = 'eps-regression',
                kernel = 'radial')

# Predicting
y_pred = predict(regressor, newdata = data.frame(x_col_name = predict_value))

## Decision Tree Regressor

# No need for feature scaling
# Non-linear
# Non-continuous

# Fitting
library(rpart)
regressor = rpart(formula = y_col_name ~ .,
                  data = training_set)

# Predicting
y_pred = predict(regressor, newdata = data.frame(x_col_name = predict_value))

# Visualising the training set results (high resolution)
library(ggplot2)
x_grid = seq(min(training_set$x), max(training_set$y), 0.01)
ggplot() +
  geom_point(aes(x = dataset$x, y = dataset$y), colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(x = x_grid))), colour = 'blue') +
  ggtitle('y vs x (Decision Tree Regression)') +
  ylab('y') +
  xlab('x')

## Random Forest Regressor

# No need for feature scaling
# Non-linear
# Non-continuous

# Fitting
library(randomForest)
regressor = randomForest(x = dataset[x_col_indexes],
                         y = dataset$y)

# Predicting
y_pred = predict(regressor, newdata = data.frame(x_col_name = predict_value))

# Visualising the training set results (high resolution)
library(ggplot2)
x_grid = seq(min(training_set$x), max(training_set$y), 0.01)
ggplot() +
  geom_point(aes(x = dataset$x, y = dataset$y), colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(x = x_grid))), colour = 'blue') +
  ggtitle('y vs x (Decision Tree Regression)') +
  ylab('y') +
  xlab('x')

## Logistic Regression Classifier

# Needs feature scaling
# Linear
# Continuous

# Fitting
classifier = glm(formula = y_col_name ~ .,
                 data = training_set,
                 family = binomial)

# Predicting
prob_pred = predict(classifier, type = 'response', newdata = test_set[x_col_indexes])
y_pred = ifelse(prob_pred > 0.5, 1, 0)

# Evaluating
cm = table(test_set[, y_label_index], y_pred)

# Visualising the Training set results
library(ElemStatLearn)
set = training_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('x_col_name_1', 'x_col_name_2')
prob_set = predict(classifier, type = 'y_col_name', newdata = grid_set)
y_grid = ifelse(prob_set > 0.5, 1, 0)
plot(set[, -3],
     main = 'Logistic Regression (Training set)',
     xlab = 'x_col_name_1', ylab = 'x_col_name_2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

# Visualising the Test set results
library(ElemStatLearn)
set = test_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('x_col_name_1', 'x_col_name_2')
prob_set = predict(classifier, type = 'y_col_name', newdata = grid_set)
y_grid = ifelse(prob_set > 0.5, 1, 0)
plot(set[, -3],
     main = 'Logistic Regression (Test set)',
     xlab = 'x_col_name_1', ylab = 'x_col_name_2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

## KNN Classifier

# Needs feature scaling
# Non-linear
# Continuous

# Fitting and predicting
library(class)
y_pred = knn(train = training_set[, 1:2],
             test = test_set[, 1:2],
             cl = training_set[, 3],
             k = 5)

# Evaluating
cm = table(test_set[, y_label_index], y_pred)

# Visualising the Training set results
library(ElemStatLearn)
set = training_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('x_col_name_1', 'x_col_name_2')
y_grid = knn(train = training_set[, 1:2],
             test = grid_set,
             cl = training_set[, 3],
             k = 5) # - means removing the column
plot(set[, -3],
     main = 'KNN (Training set)',
     xlab = 'x_col_name_1', ylab = 'x_col_name_2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

# Visualising the Test set results
library(ElemStatLearn)
set = test_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('x_col_name_1', 'x_col_name_2')
y_grid = knn(train = training_set[, 1:2],
             test = grid_set,
             cl = training_set[, 3],
             k = 5) # - means removing the column
plot(set[, -3],
     main = 'KNN (Test set)',
     xlab = 'x_col_name_1', ylab = 'x_col_name_2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

## SVM Classifier

# Needs feature scaling
# Non-linear (unless if using the linear kernel)
# Continuous

# Creating the model
library(e1071)
classifier = svm(formula = Purchased ~ .,
                 data = training_set,
                 type = 'C-classification',
                 kernel = 'kernel_name')

# Evaluating the model
cm = table(test_set[, 3], y_pred)
diag = diag(cm)
rowsums = apply(cm, 1, sum)
colsums = apply(cm, 2, sum)
accuracy = sum(diag) / sum(cm)
precision = diag / colsums
recall = diag / rowsums
f1 = 2 * precision * recall / (precision + recall)
data.frame(accuracy, precision, recall, f1) # Look at the positive class when dealing with binary classification

# Alternative way
cm = table(test_set[, 3], y_pred)
tn = cm[1]
fn = cm[2]
fp = cm[3]
tp = cm[4]
n = sum(cm)
accuracy = (tp + tn) / n
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * (precision * recall) / (precision + recall)

# Visualising the Training set results
library(ElemStatLearn)
set = training_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('x_col_name_1', 'x_col_name_2')
y_grid = predict(classifier, newdata = grid_set)
plot(set[, -3],
     main = 'SVM (Training set)',
     xlab = 'x_col_name_1', ylab = 'x_col_name_2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

# Visualising the Test set results
library(ElemStatLearn)
set = test_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('x_col_name_1', 'x_col_name_2')
y_grid = predict(classifier, newdata = grid_set)
plot(set[, -3],
     main = 'SVM (Test set)',
     xlab = 'x_col_name_1', ylab = 'x_col_name_2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))
