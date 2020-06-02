# Random Forest Regression

# Loading the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Building the model
# install.packages('randomForest')
library(randomForest)
regressor = randomForest(x = dataset[1],
                         y = dataset$Salary,
                         ntree = 100)

# Predicting a new value
y_pred = predict(regressor, newdata = data.frame(Level = 6.5))

# Plotting with high resolution
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))), colour = 'blue') +
  ggtitle('Salary vs Level (Random Forest)') +
  ylab('Salary') +
  xlab('Level')
