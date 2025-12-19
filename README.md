# Python Calculator with CI/CD

![Python CI Unit Tests](https://github.com/DevOpswithDevik/Python-Calculator/actions/workflows/python-app.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

A simple Python-based calculator application demonstrating modular code structure, unit testing, and automated CI/CD workflows using GitHub Actions.

## 🚀 Features
* **Modular Design:** Calculation logic is separated into `calculator.py`.
* **Unit Testing:** Comprehensive tests implemented in `test_calculator.py`.
* **CI/CD Integration:** Automatically runs tests on every push or pull request to the main branch.
* **Easy Execution:** Includes a `main.py` script for quick demonstration.

## 📁 Project Structure
```text
Python-Calculator/
├── .github/workflows/  # GitHub Actions CI configuration
├── calculator.py       # Core logic for mathematical operations
├── main.py             # Script to demonstrate usage
├── test_calculator.py  # Unit tests for the calculator
└── requirements.txt    # Project dependencies

🛠️ Installation & Setup
Clone the repository:

Bash

git clone [https://github.com/DevOpswithDevik/Python-Calculator.git](https://github.com/DevOpswithDevik/Python-Calculator.git)
cd Python-Calculator
(Optional) Create a virtual environment:

Bash

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash

pip install -r requirements.txt
💻 Usage
To run the calculator demonstration:

Bash

python main.py
🧪 Running Tests
This project uses unit tests to ensure code quality. To run them manually:

Bash

python -m unittest test_calculator.py
⚙️ CI/CD Workflow
The project includes a GitHub Actions pipeline that automatically:

Sets up a Python environment.

Installs dependencies from requirements.txt.

Executes the unit tests.

Created by DevOpswithDevik