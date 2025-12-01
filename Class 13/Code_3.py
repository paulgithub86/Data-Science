# The Loss Function: L(w) = w^2
def loss_func(w): return w**2
def gradient(w): return 2*w

# Hyperparameters
w_start = 4.0      # Starting position on the hill
learning_rate = 0.1 # Size of the steps (eta)
epochs = 15

# Training Loop
weights = [w_start]
losses = [loss_func(w_start)]

w = w_start
for _ in range(epochs):
    grad = gradient(w)
    w = w - learning_rate * grad # The Update Rule
    weights.append(w)
    losses.append(loss_func(w))

# Visualization
w_range = np.linspace(-4.5, 4.5, 100)
plt.figure(figsize=(8, 6))
plt.plot(w_range, loss_func(w_range), 'k-', alpha=0.3, label="Loss Landscape")
plt.scatter(weights, losses, c=np.arange(len(weights)), cmap='cool', s=100, zorder=5)
plt.plot(weights, losses, 'r--', alpha=0.5)

plt.title(f"Gradient Descent Steps (Learning Rate: {learning_rate})")
plt.xlabel("Weight (w)")
plt.ylabel("Loss L(w)")
plt.grid(True)
plt.show()
