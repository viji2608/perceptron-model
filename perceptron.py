import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=1000):
        self.weights = np.zeros(input_size + 1)  # +1 for bias
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        x = np.insert(x, 0, 1)  # Add bias term
        weighted_sum = np.dot(self.weights, x)
        return self.activation(weighted_sum)

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                xi = np.insert(xi, 0, 1)  # Add bias term
                prediction = self.predict(xi[1:])
                error = target - prediction
                self.weights += self.learning_rate * error * xi

# Example usage
if __name__ == "__main__":
    # Training data: logical AND
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])

    perceptron = Perceptron(input_size=2)
    perceptron.train(X, y)

    print("Predictions:")
    for x in X:
        print(f"{x} => {perceptron.predict(x)}")
