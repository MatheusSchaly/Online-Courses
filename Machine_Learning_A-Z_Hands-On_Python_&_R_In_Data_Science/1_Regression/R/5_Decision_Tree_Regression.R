# Decision Tree Regression

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Training the Decision Tree Regressor
# install.packages('rpart')
library(rpart)
regressor = rpart(formula = Salary ~ .,
                  data = dataset,
                  control = rpart.control(minsplit = 1))

# Predict a new value
y_pred = predict(regressor, newdata = data.frame(Level = 6.5))

# Plotting the Decision Tree Regressor (lower resolution (WRONG))
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)), colour = 'blue') +
  ggtitle('Salary vs Level (Decision Tree Regression)') +
  ylab('Salary') +
  xlab('Level')

# Plotting the Decision Tree Regressor (higher resolution (RIGHT))
x_grid = seq(from = min(dataset$Level), to = max(dataset$Level), by = 0.01)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))), colour = 'blue') +
  ggtitle('Salary vs Level (Decision Tree Regression)') +
  ylab('Salary') +
  xlab('Level')
