def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_prime(x): return sigmoid(x) * (1 - sigmoid(x))

def relu(x): return np.maximum(0, x)
def relu_prime(x): return np.where(x > 0, 1.0, 0.0)

x = np.linspace(-5, 5, 200)

plt.figure(figsize=(14, 6))

# Plot Sigmoid
plt.subplot(1, 2, 1)
plt.plot(x, sigmoid(x), label="Sigmoid $\sigma(x)$", color='blue', linewidth=2)
plt.plot(x, sigmoid_prime(x), label="Derivative $\sigma'(x)$", color='red', linestyle='--')
plt.title("Sigmoid: Max Derivative is 0.25\n(Causes Vanishing Gradient)", fontsize=12)
plt.grid(True)
plt.legend()

# Plot ReLU
plt.subplot(1, 2, 2)
plt.plot(x, relu(x), label="ReLU $f(x)$", color='green', linewidth=2)
plt.plot(x, relu_prime(x), label="Derivative $f'(x)$", color='orange', linestyle='--')
plt.title("ReLU: Derivative is 1.0\n(Solves Vanishing Gradient)", fontsize=12)
plt.ylim(-0.5, 2)
plt.grid(True)
plt.legend()

plt.show()
