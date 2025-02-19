import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split

class KNN:
    def __init__(self, k):
        self.k = k
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        return [self.pred(x) for x in X]
    
    def pred(self, x):
        distances = [np.linalg.norm(x - x_train) for x_train in self.X_train]
        k_ind = np.argsort(distances)[:self.k]
        k_labels = [self.y_train[i] for i in k_ind]
        most_common = Counter(k_labels).most_common(1)
        return most_common[0][0]

 
iris = load_iris()
X = iris.data
y = iris.target

 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.45, random_state=42)
 
k_values = [2,3,4,5,6,7,8,9,10,12,13,15,16]
accuracies = []

for k in k_values:
    knn = KNN(k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = np.mean(y_pred == y_test)
    accuracies.append(accuracy)

# Plot k vs accuracy
 
plt.plot(k_values, accuracies, marker='o', linestyle='-')
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.title('K vs Accuracy in KNN')
plt.grid(True)
plt.show()
