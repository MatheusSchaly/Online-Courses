# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Fitting our model
library(e1071)
regressor = svm(formula = Salary ~ .,
                data = dataset,
                type = 'eps-regression',
                kernel = 'radial')

# Predict a value
y_pred = predict(regressor, newdata = data.frame(Level = 6.5))

# Plotting a graph
library(ggplot2)
ggplot() +
  geom_point(aes(dataset$Level, dataset$Salary),
             colour = 'red') +
  geom_line(aes(dataset$Level, predict(regressor, newdata = dataset)),
            colour = 'blue') +
  ggtitle('Salary vs Level (SVR)') +
  xlab('Level') +
  ylab('Salary')