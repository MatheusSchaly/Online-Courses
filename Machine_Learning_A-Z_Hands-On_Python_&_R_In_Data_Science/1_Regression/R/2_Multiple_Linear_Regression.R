# Multiple Linear Regression

# Importing the dataset
dataset = read.csv('50_Startups.csv')

# Encoding the categorical column
dataset$State = factor(dataset$State,
                      levels = c('New York', 'California', 'Florida'),
                      labels = c(1, 2, 3))

# Split our data
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting our model
regressor = lm(formula = Profit ~ .,
               data = training_set)
summary(regressor)

# Backward Selection
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
               data = training_set)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
               data = training_set)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend,
               data = training_set)
summary(regressor)