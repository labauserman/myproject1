# 🚢 Titanic Data Analyzer

A lightweight Python project exploring the Titanic dataset using **Pandas** and **Seaborn**. This project analyzes survival rates based on passenger class and gender. This is really an exploartion of using Gemini as a guide to getting uv setup on a new MacBook. 

## 🚀 Features
- **Data Ingestion:** Loads the classic Titanic dataset.
- **Statistical Analysis:** Calculates survival probabilities by category.
- **Visualization:** Generates a bar chart showing class/gender survival gaps.
- **Testing:** Includes a `pytest` suite to verify API connectivity.

## 🛠️ Tech Stack
- **Python 3.12+**
- **Environment Manager:** [uv](https://github.com/astral-sh/uv) (fastest Python package manager)
- **Libraries:** Pandas, Seaborn, Matplotlib, Requests, Pytest

## 📦 Installation & Setup
Since this project uses `uv`, setup is near-instant:

1. **Clone the repo:**
   ```zsh
   git clone https://github.com/labauserman/myproject1.git
   cd myproject1

2. **Sync the environment:**
   uv sync

3. **To run the analysis and generate the chart:**
   uv run python data_analyzer.py
