#!/bin/bash

# --- COLORS FOR BEAUTIFICATION ---
BLUE='\033[0;34m'
TEAL='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# --- HEADER ---
clear
echo -e "${BLUE}================================================================${NC}"
echo -e "${BOLD}${TEAL}    CS531: FOUNDATIONS OF NEURAL NETWORKS - PRACTICE CODE GUIDE    ${NC}"
echo -e "${BLUE}================================================================${NC}"
echo -e "Instructor: ${BOLD}Prof. Paul A.${NC}"
echo -e "Platform:   ${BOLD}Google Colab / Python Notebooks${NC}"
echo -e ""

# --- PART 1 ---
echo -e "${BOLD}${BLUE}[Part 1] The Perceptron & Linear Separability${NC}"
echo -e "${TEAL}Filename suggestion:${NC} ${GREEN}01_perceptron_logic_gates.py${NC}"
echo -e "----------------------------------------------------------------"
echo -e "  ${BOLD}Concept:${NC} Demonstrates the limitation of the Single Layer Perceptron."
echo -e "  ${BOLD}What it does:${NC}"
echo -e "  1. Trains a Perceptron on AND data (Linearly Separable)."
echo -e "  2. Trains a Perceptron on XOR data (Non-Linearly Separable)."
echo -e "  3. Plots the 'Decision Boundary' (background color)."
echo -e "  ${BOLD}Key Takeaway for Students:${NC}"
echo -e "  Notice how the linear line CANNOT separate the red/green dots in the XOR plot."
echo -e ""

# --- PART 2 ---
echo -e "${BOLD}${BLUE}[Part 2] Activation Functions & Vanishing Gradient${NC}"
echo -e "${TEAL}Filename suggestion:${NC} ${GREEN}02_activation_derivatives.py${NC}"
echo -e "----------------------------------------------------------------"
echo -e "  ${BOLD}Concept:${NC} Why we switched from Sigmoid to ReLU in Deep Learning."
echo -e "  ${BOLD}What it does:${NC}"
echo -e "  1. Plots Sigmoid vs. ReLU functions (solid lines)."
echo -e "  2. Plots their DERIVATIVES (dashed lines)."
echo -e "  ${BOLD}Key Takeaway for Students:${NC}"
echo -e "  Look at the red dashed line for Sigmoid. The max value is 0.25."
echo -e "  Multiplying 0.25 many times results in zero (Vanishing Gradient)."
echo -e "  ReLU's derivative is 1.0, which keeps the signal alive."
echo -e ""

# --- PART 3 ---
echo -e "${BOLD}${BLUE}[Part 3] Gradient Descent Intuition${NC}"
echo -e "${TEAL}Filename suggestion:${NC} ${GREEN}03_gradient_descent_sim.py${NC}"
echo -e "----------------------------------------------------------------"
echo -e "  ${BOLD}Concept:${NC} How the network finds the minimum error."
echo -e "  ${BOLD}What it does:${NC}"
echo -e "  1. Defines a simple convex loss function L(w) = w^2."
echo -e "  2. Simulates a 'ball' rolling down the hill using the update rule."
echo -e "  3. Visualizes the steps as dots changing color over time."
echo -e "  ${BOLD}Key Takeaway for Students:${NC}"
echo -e "  Change the 'learning_rate' variable. If it's too high (e.g., 1.1),"
echo -e "  the ball will explode upwards! If too low, it moves too slowly."
echo -e ""

# --- PART 4 ---
echo -e "${BOLD}${BLUE}[Part 4] Capacity vs. Overfitting${NC}"
echo -e "${TEAL}Filename suggestion:${NC} ${GREEN}04_bias_variance_tradeoff.py${NC}"
echo -e "----------------------------------------------------------------"
echo -e "  ${BOLD}Concept:${NC} Bias-Variance Tradeoff using Polynomial Regression."
echo -e "  ${BOLD}What it does:${NC}"
echo -e "  1. Generates noisy sine wave data."
echo -e "  2. Fits a Line (Degree 1), a Curve (Degree 4), and a Wiggly Line (Degree 15)."
echo -e "  ${BOLD}Key Takeaway for Students:${NC}"
echo -e "  - Degree 1 is Underfitting (High Bias)."
echo -e "  - Degree 15 is Overfitting (High Variance) - it memorizes noise."
echo -e "  - Degree 4 is the 'Sweet Spot' (Capacity matches complexity)."
echo -e ""

# --- FOOTER ---
echo -e "${BLUE}================================================================${NC}"
echo -e "To run these, copy the code blocks into specific cells in Google Colab"
echo -e "and press ${BOLD}Shift + Enter${NC}."
echo -e "${BLUE}================================================================${NC}"
