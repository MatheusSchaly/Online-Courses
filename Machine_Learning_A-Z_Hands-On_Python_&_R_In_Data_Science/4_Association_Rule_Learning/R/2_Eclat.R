# Importing the dataset
dataset = read.csv('Market_Basket_Optimisation.csv', header=FALSE)

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