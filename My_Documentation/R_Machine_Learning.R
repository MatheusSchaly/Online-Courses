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

# Predicting
y_pred = predict(regressor, newdata = data.frame(x_col_name = predict_value))

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

## Naive Bayes

# Needs feature scaling
# Non-linear (unless if using the linear kernel)
# Continuous

# Encoding the label as factor
dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))

# Creating the model
library(e1071)
classifier = naiveBayes(x = training_set[-3],
                        y = training_set$Purchased)

# Predicting
y_pred = predict(regressor, newdata = data.frame(x_col_name = predict_value))

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

## Decision Tree

# No need for feature scaling
# Non-linear
# Non-continuous

# Encoding the label as factor
dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))

# Creating the model
library(rpart)
dt = rpart(formula = Purchased ~ .,
           data = training_set)

# Predicting
y_pred = predict(dt, newdata = test_set[-3], type = 'class')

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

# Plotting the decision tree
plot(classifier)
text(classifier)

## Random Forest

# No need for feature scaling
# Non-linear
# Non-continuous

# Encoding the label as factor
dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))

# Creating the model
library(randomForest)
rf = randomForest(x = training_set[-3],
                  y = training_set$Purchased,
                  ntree = 20)

# Predicting
y_pred = predict(dt, newdata = test_set[-3], type = 'class')

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
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(rf, newdata = grid_set, type = 'class')
plot(set[, -3],
     main = 'Random Forest Classification (Training set)',
     xlab = 'Age', ylab = 'Estimated Salary',
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
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(rf, newdata = grid_set, type = 'class')
plot(set[, -3], main = 'Random Forest Classification (Test set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

# k-Means

# Using the elbow method to find the optimal number of clusters
set.seed(6)
wcss = vector()
for (i in 1:10) wcss[i] <- sum(kmeans(X, i)$withinss)
plot(1:10, wcss, type = "b", main = paste('Clusters of clients'), xlab = 'Number of clusters', ylab = 'Number of clusters')

# Building the final model
set.seed(29)
kmeans = kmeans(X, 5, iter.max = 300, nstart = 10)

# Visualizing the clusters
library(cluster)
clusplot(X,
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         plotchar = FALSE,
         main = paste('Clusters of clinets'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')

# Hierarchical Clustering

# Using the dendrogram to find the optimal number of clusters
dendrogram = hclust(dist(X, method='euclidean'), method = 'ward.D')

plot(dendrogram,
     main = paste('Dendogram'),
     xlab = 'Customers',
     ylab = 'Euclidean distances')

# Fitting hierarchical clustering to the mall dataset
hc = hclust(dist(X, method='euclidean'), method = 'ward.D')
y_hc = cutree(hc, 5)

# Visualizing the clusters
library(cluster)
clusplot(X,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         plotchar = FALSE,
         main = paste('Clusters of clinets'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')

# Apriori

# Converting the dataset into a sparse matrix
# install.packages('arules')
library(arules)
dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)
itemFrequencyPlot(dataset, topN = 10)

# Training Apriori on the dataset
rules = apriori(data = dataset, parameter = list(support = 0.004, confidence = 0.2))

# Visualising the results
inspect(sort(rules, by = 'lift')[1:10])

# Eclat

# Converting the dataset into a sparce matrx
# install.packages('arules')
library(arules)
dataset = read.transactions('Market_Basket_Optimisation.csv', sep=',', rm.duplicates = TRUE)
summary(dataset)
itemFrequencyPlot(dataset, topN = 10)

# Training Eclat on the dataset
rules = eclat(data = dataset, parameter = list(support = 0.004, minlen=1))

# Visualising the reulsts
inspect(sort(rules, by='support')[1:10])

# Upper confidence bound

# Implementing UCB
N = 10000
d = 10
ads_selected = integer()
numbers_of_selections = integer(d)
sums_of_rewards = integer(d)
total_reward = 0

for (n in 1:N) {
  ad = 0
  max_upper_bound = 0
  for (i in 1:d) {
    if (numbers_of_selections[i] > 0) {
      average_reward = sums_of_rewards[i] / numbers_of_selections[i]
      delta_i = sqrt(3/2 * log(n) / numbers_of_selections[i])
      upper_bound = average_reward + delta_i
    } else {
      upper_bound = 1e400
    }
    if (upper_bound > max_upper_bound) {
      max_upper_bound = upper_bound
      ad = i
    }
  }
  ads_selected = append(ads_selected, ad)
  numbers_of_selections[ad] = numbers_of_selections[ad] + 1
  reward = dataset[n, ad]
  sums_of_rewards[ad] = sums_of_rewards[ad] + reward
  total_reward = total_reward + reward
}

# Visualising the results
hist(ads_selected,
     col = 'blue',
     main = 'Histogram of ads selections',
     xlab = 'Ads',
     ylab = 'Number of times each ad was selected by the algorithm')

# Thompson sampling

# Implementing Thompson Sampling
N = 10000
d = 10
ads_selected = integer()
number_of_rewards_1 = integer(d)
number_of_rewards_0 = integer(d)
total_reward = 0

for (n in 1:N) {
  ad = 0
  max_random_beta = 0
  for (i in 1:d) {
    random_beta = rbeta(n = 1,
                        shape1 = number_of_rewards_1[i] + 1,
                        shape2 = number_of_rewards_0[i] + 1)
    if (random_beta > max_random_beta) {
      max_random_beta = random_beta
      ad = i
    }
  }
  ads_selected = append(ads_selected, ad)
  reward = dataset[n, ad]
  if (reward == 1) {
    number_of_rewards_1[ad] = number_of_rewards_1[ad] + 1
  } else {
    number_of_rewards_0[ad] = number_of_rewards_0[ad] + 1
  }
  total_reward = total_reward + reward
}

# Visualising the results
hist(ads_selected,
     col = 'blue',
     main = 'Histogram of ads selections',
     xlab = 'Ads',
     ylab = 'Number of times each ad was selected by the algorithm')

# Natural Language Processing

# Importing the dataset
dataset_original = read.csv('Restaurant_Reviews.tsv', sep = '\t', quote = '', stringsAsFactors = FALSE)

# Cleaning the texts
# install.packages('tm')
library(tm)
corpus = VCorpus(VectorSource(dataset_original$Review))
corpus = tm_map(corpus, content_transformer(tolower))
corpus = tm_map(corpus, removeNumbers)
corpus = tm_map(corpus, removePunctuation)
corpus = tm_map(corpus, removeWords, stopwords())
corpus = tm_map(corpus, stemDocument)
corpus = tm_map(corpus, stripWhitespace)

# Creating the Bag of Words model
dtm = DocumentTermMatrix(corpus)
dtm = removeSparseTerms(dtm, 0.999)
dataset = as.data.frame(as.matrix(dtm))
dataset$Liked = dataset_original$Liked