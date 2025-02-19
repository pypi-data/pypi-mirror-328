import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost(X, y, weight):
    m = len(y)
    z = np.dot(X, weight)
    h = sigmoid(z)
    cost = (-1/m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    return cost

def lr(X, y):
    weight = np.zeros(X.shape[1])
    for i in range(1000):
        z = np.dot(X, weight)
        h = sigmoid(z)
        grad = np.dot(X.T, (h - y)) / len(y)
        weight -= 0.01 * grad

        if i % 100 == 0:  # Print cost every 100 iterations
            cost = compute_cost(X, y, weight)
            print(f"Iteration {i}: Cost = {cost:.4f}")

    return weight

 
X=iris.data[:,:2]
y=(iris.target!=0)*1

weights = lr(X, y)
print("Final Weights:", weights)
