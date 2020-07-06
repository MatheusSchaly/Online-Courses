# Importing the dataset
dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]

# Using the dendogram to find the optimal number of clusters
dendogram = hclust(dist(X, method='euclidean'), method='ward.D')

plot(dendogram,
     main = paste('Dendogram'),
     xlab = 'Customers',
     ylab = 'Euclidean distances')

# Building the hierarchical clustering
hc = hclust(dist(X, method='euclidean'), method='ward.D')
y_hc = cutree(hc, 5)

# Visualising the clusters
library(cluster)
clusplot(X,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         plotchar = FALSE,
         main = paste('Clusters of clients'),
         xlab = 'Annual Income',
         ylab = 'Spending Score')