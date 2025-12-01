# CS531: Foundations of Neural Networks - Practice Code Guide

**Instructor:** Prof. Paul A.  
**Platform:** Google Colab / Python Notebooks

---

## 🔹 [Part 1] The Perceptron & Linear Separability
**Filename suggestion:** `01_perceptron_logic_gates.py`

* **Concept:** Demonstrates the limitation of the Single Layer Perceptron.
* **What it does:**
    1.  Trains a Perceptron on AND data (Linearly Separable).
    2.  Trains a Perceptron on XOR data (Non-Linearly Separable).
    3.  Plots the 'Decision Boundary' (background color).
* **Key Takeaway for Students:**
    > Notice how the linear line CANNOT separate the red/green dots in the XOR plot.

---

## 🔹 [Part 2] Activation Functions & Vanishing Gradient
**Filename suggestion:** `02_activation_derivatives.py`

* **Concept:** Why we switched from Sigmoid to ReLU in Deep Learning.
* **What it does:**
    1.  Plots Sigmoid vs. ReLU functions (solid lines).
    2.  Plots their DERIVATIVES (dashed lines).
* **Key Takeaway for Students:**
    > Look at the red dashed line for Sigmoid. The max value is 0.25. Multiplying 0.25 many times results in zero (Vanishing Gradient). ReLU's derivative is 1.0, which keeps the signal alive.

---

## 🔹 [Part 3] Gradient Descent Intuition
**Filename suggestion:** `03_gradient_descent_sim.py`

* **Concept:** How the network finds the minimum error.
* **What it does:**
    1.  Defines a simple convex loss function $L(w) = w^2$.
    2.  Simulates a 'ball' rolling down the hill using the update rule.
    3.  Visualizes the steps as dots changing color over time.
* **Key Takeaway for Students:**
    > Change the `learning_rate` variable. If it's too high (e.g., 1.1), the ball will explode upwards! If too low, it moves too slowly.

---

## 🔹 [Part 4] Capacity vs. Overfitting
**Filename suggestion:** `04_bias_variance_tradeoff.py`

* **Concept:** Bias-Variance Tradeoff using Polynomial Regression.
* **What it does:**
    1.  Generates noisy sine wave data.
    2.  Fits a Line (Degree 1), a Curve (Degree 4), and a Wiggly Line (Degree 15).
* **Key Takeaway for Students:**
    * **Degree 1** is Underfitting (High Bias).
    * **Degree 15** is Overfitting (High Variance) - it memorizes noise.
    * **Degree 4** is the 'Sweet Spot' (Capacity matches complexity).

---

### 🚀 How to Run
To run these, copy the code blocks into specific cells in Google Colab and press **Shift + Enter**.
