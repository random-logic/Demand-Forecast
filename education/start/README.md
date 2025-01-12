# Prerequisites
[setup](/education/setup/README.md)

# Working for First Time
1. Open Terminal or Command Prompt where you want to save the project folder
2. Run: `git clone git@github.com:random-logic/Demand-Forecast.git`
3. Run: `cd Demand-Forecast`
4. Run: `conda activate Demand-Forecast`
5. Run: `pip install -r requirements.txt`

# Accessing Project After First Time
1. Open Terminal or Command Prompt in project folder
2. Run: `conda activate Demand-Forecast`

# After Switching to Different Git Branch
1. Run: `pip install -r requirements.txt`

# Install New Dependencies
1. Run: `pip install [dependency name]`
2. Run: `pip freeze > requirements.txt`

# Uninstall Dependencies
1. Run: `pip install [dependency name]`
2. Run: `pip freeze > requirements.txt`

# Creating New Code
* Create .py for Python Scripts or .ipynb for Jupyter Notebooks
* ALL CODE should go in [this directory](/src)
* When importing code from other scripts in src, use relative paths from repo
  * DO NOT use absolute paths or it won't work on other computers

# Execute Code
1. Run: `python3 [path to file]`
