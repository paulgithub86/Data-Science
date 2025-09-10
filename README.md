
# Data Science Course: A Comprehensive Guide

> A modular, end‑to‑end learning path for mastering data analysis, data visualization, and machine learning with Python.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](#prerequisites)
[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange.svg)](#how-to-run-the-code)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#how-to-run-the-code)

---

## Overview

Welcome! This guide provides a structured roadmap to build a strong foundation in data science using Python. It starts from first principles and advances to practical, industry‑ready skills. The curriculum is **modular**—follow the full path or jump to the module you need.

**You will learn to:**
- Set up a robust Python environment for reproducible work.
- Manipulate and clean tabular data at scale.
- Explore and visualize data for insight (exploratory data analysis, **EDA**).
- Train, evaluate, and interpret fundamental machine learning (**ML**) models.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Environment Setup](#environment-setup)
- [Repository Structure](#repository-structure)
- [Course Structure & Modules](#course-structure--modules)
- [How to Run the Code](#how-to-run-the-code)
- [Recommended Learning Path](#recommended-learning-path)
- [Datasets](#datasets)
- [Exercises & Assessments](#exercises--assessments)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

---

## Prerequisites

To get the most out of the course, it is helpful (not strictly required for Module 1) to have:

- **Basic Python knowledge**: variables, data types, conditionals, loops, functions, and modules.
- **Core math intuition**: algebra, statistics, and linear algebra (vectors/matrices). A refresher is included inside.
- **Software**: a Python 3.11+ environment. We recommend **Anaconda** for painless dependency management.

**Core libraries** used in the course:
- `pandas` · `numpy` · `matplotlib` · `seaborn` · `scikit-learn` · `jupyter` (or Spyder)

> If you are brand new to Python, start with Module 1 and the warm‑up notebooks.

---

## Quick Start

```bash
# 1) Clone
git clone https://github.com/your-org/your-repo.git
cd your-repo

# 2) Create an isolated environment (Conda)
conda create -n ds-course python=3.11 -y
conda activate ds-course

# 3) Install dependencies
pip install -r requirements.txt

# 4) Launch Jupyter
jupyter lab
```

Or use **Google Colab**: upload a notebook from `notebooks/` and run it in the cloud. No local setup needed.

---

## Environment Setup

Minimal `requirements.txt`:

```
pandas>=2.2
numpy>=1.26
matplotlib>=3.8
seaborn>=0.13
scikit-learn>=1.5
jupyterlab>=4.0
```

Optional (later modules): `tensorflow`, `torch`, `xgboost`.

**Conda environment (alternative):**

```yaml
# environment.yml
name: ds-course
channels: [conda-forge, defaults]
dependencies:
  - python=3.11
  - pandas>=2.2
  - numpy>=1.26
  - matplotlib>=3.8
  - seaborn>=0.13
  - scikit-learn>=1.5
  - jupyterlab>=4.0
  - pip
  - pip:
      - ipywidgets
```

Create it with:

```bash
conda env create -f environment.yml
conda activate ds-course
```

---

## Repository Structure

```
your-repo/
├─ data/                 # small sample datasets (CSV/JSON) 
├─ notebooks/            # Jupyter notebooks per module
│  ├─ 01_setup.ipynb
│  ├─ 02_pandas_numpy.ipynb
│  ├─ 03_visualization.ipynb
│  └─ 04_ml_fundamentals.ipynb
├─ src/                  # reusable Python modules/utilities
│  ├─ eda.py
│  ├─ viz.py
│  └─ models.py
├─ tests/                # optional: simple unit tests for utils
├─ exercises/            # practice tasks with solutions
├─ README.md             # this file
├─ requirements.txt
└─ environment.yml
```

> Keep datasets small and public-domain. Larger data should be linked, not committed.

---

## Course Structure & Modules

### Module 1 — Python & Environment Setup
- The Python ecosystem for data science.
- Installing Anaconda. Creating and activating environments.
- Using Jupyter Notebook and JupyterLab. Spyder as an alternative.
- Python fundamentals refresher: lists, dictionaries, functions, file I/O.

**Outcome:** You can run notebooks, import libraries, and write basic scripts.

---

### Module 2 — Data Manipulation with pandas & NumPy
- `pandas` essentials: `Series`, `DataFrame`, indexes.
- **Data Loading:** CSV, Excel, JSON; reading from URLs.
- **Cleaning & Preprocessing:** missing values, duplicates, type conversion.
- **Aggregation:** `groupby`, summarization, pivot tables.
- `NumPy` arrays for fast vectorised operations.

**Outcome:** You can clean messy data and produce tidy tables ready for analysis.

---

### Module 3 — Data Visualization
- Choosing the right chart for the question (comparison, distribution, relationship).
- **Matplotlib** basics: line, scatter, bar, histogram.
- **Seaborn**: box plot, violin plot, pair plot, heatmap; styling and palettes.
- Visual storytelling: annotations, labels, titles, legends, and layout.

**Outcome:** You can create clear, persuasive charts to communicate insights.

---

### Module 4 — Machine Learning Fundamentals
- Supervised versus unsupervised learning.
- The **ML workflow**: train/validation/test split, model training, evaluation.
- `scikit-learn` API: estimators, transformers, pipelines.
- **Supervised learning**
  - Regression (predict continuous targets): LinearRegression, Ridge.
  - Classification (predict categories): LogisticRegression, DecisionTree.
- **Unsupervised learning**
  - Clustering: KMeans; dimensionality reduction: Principal Component Analysis (PCA).

**Outcome:** You can fit baseline models and interpret core evaluation metrics.

---

## How to Run the Code

You have three main options:

1. **Google Colab** (easiest): upload `.ipynb` notebooks from `notebooks/` and run them—no installation required.
2. **Jupyter Notebook/Lab** (local): launch `jupyter lab` and open any notebook.
3. **Local IDE** (e.g., Spyder, VS Code): run `.py` scripts from the `src/` folder or open notebooks with an extension.

> Tip: For reproducibility, set random seeds where relevant and record package versions (`pip freeze > versions.txt`).

---

## Recommended Learning Path

1. Module 1 → 2 → 3 → 4 (in order).
2. After each module, complete the exercises in `exercises/`.
3. For the machine learning module, start with small datasets first, then try a larger, realistic dataset.

**Milestones:**
- **M1:** Environment is set up; you can run a notebook.
- **M2:** You can import, clean, and summarise a dataset.
- **M3:** You can produce three charts that answer a business or research question.
- **M4:** You can train a classifier and report accuracy, precision, recall, and F1 score.

---

## Datasets

Small, open datasets are included under `data/` for convenience (for example: Iris, Titanic). For larger datasets, use links provided in notebooks (Kaggle, UCI ML Repository, or open government portals).

> Always check licences and cite sources in your reports.

---

## Exercises & Assessments

Each module includes:
- **Hands‑on tasks** (fill in the notebook cells).
- **Short quizzes** to check understanding (multiple‑choice questions, MCQs).
- **Mini projects** (optional): explore a dataset end‑to‑end and present findings.

Rubrics emphasise clarity, correctness, and reproducibility.

---

## Troubleshooting

- **Package version conflicts**: create a fresh Conda environment; avoid mixing `pip` and `conda` unless necessary.
- **Matplotlib plots not showing**: ensure `%matplotlib inline` is at the top of the notebook or call `plt.show()` in scripts.
- **Memory errors with large CSVs**: read in chunks (`pd.read_csv(..., chunksize=...)`) or sample rows for prototyping.

---

## FAQ

**Q:** Do I need a GPU?  
**A:** No. All core modules run comfortably on CPU. Optional deep learning experiments benefit from a GPU but are not required.

**Q:** Can I use VS Code instead of Jupyter/Spyder?  
**A:** Yes. Use the Python and Jupyter extensions for a similar experience.

**Q:** Where do I ask questions?  
**A:** Open a GitHub Issue in this repository or start a discussion in the Discussions tab.

---

## Resources

- *Python for Data Analysis* — Wes McKinney  
- *Data Science from Scratch* — Joel Grus  
- scikit‑learn User Guide: https://scikit-learn.org/stable/user_guide.html  
- seaborn Tutorials: https://seaborn.pydata.org/tutorial.html  
- Matplotlib Gallery: https://matplotlib.org/stable/gallery/index.html  

---

## Contributing

Pull requests are welcome. Please format code with `black` and ensure notebooks run top‑to‑bottom before submitting.

---

## License

This course is released under the MIT License. See `LICENSE` for details.
