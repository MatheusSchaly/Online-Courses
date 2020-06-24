# Importing the dataset
dataset = read.csv('Mall_Customers.csv')
X = dataset[, 4:5]

# Elbow method
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