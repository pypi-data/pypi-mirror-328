from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

def kmean(X, k):
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]

    for _ in range(1000):
        distances = np.linalg.norm(X[:, None] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
    
   
    inertia = sum(np.sum((X[labels == i] - centroids[i])**2) for i in range(k))

    return centroids, labels, inertia

 
iris = load_iris()
X = iris.data

colors=['r','g','b']


k_values = range(1, 11)
centroid,label,_=kmean(X,3)
inertia_values = [kmean(X, k)[2] for k in k_values]  
for i in range(3):
    plt.scatter(X[label==i,0],X[label==i,1],c=colors[i])


plt.scatter(centroid[:,0],centroid[:,1],marker='x',c='black')

# Plot Inertia vs k
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia_values, marker='o', linestyle='-')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia (WCSS)")
plt.title("Elbow Method: Inertia vs. Number of Clusters")
plt.xticks(k_values)
plt.show()
