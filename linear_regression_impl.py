import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        self.m = None  # slope
        self.b = None  # intercept

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)

        # means
        x_mean = np.mean(X)
        y_mean = np.mean(y)

        # slope (m)
        self.m = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean)**2)

        # intercept (b)
        self.b = y_mean - self.m * x_mean

    def predict(self, X):
        return self.m * np.array(X) + self.b
    
    def mse_loss(self, X, y):
        y_pred = self.predict(X)
        return np.mean((y - y_pred) ** 2)
    
    # def r2_score(self, X, y):
    # y = np.array(y)
    # y_pred = predict(X)
    # ss_res = np.sum((y - y_pred) ** 2)
    # ss_tot = np.sum((y - np.mean(y)) ** 2)
    # return 1 - (ss_res / ss_tot)


# Example usage
X = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

model = SimpleLinearRegression()
model.fit(X, y)

print("Slope (m):", model.m)
print("Intercept (b):", model.b)

print("Predictions:", model.predict([6, 7]))
print("MSE Loss:", model.mse_loss(X, y))