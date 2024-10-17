import os

# Define the directory structure
dirs = [
    "TradeSmart_Plus/data",
    "TradeSmart_Plus/notebooks",
    "TradeSmart_Plus/reports",
    "TradeSmart_Plus/scripts",
    "TradeSmart_Plus/tests"
]

# Create the directory structure
for dir_path in dirs:
    os.makedirs(dir_path, exist_ok=True)

# Create placeholder files like README.md and requirements.txt
with open("TradeSmart_Plus/README.md", "w") as f:
    f.write("# TradeSmart Plus\n\nA trading strategy powered by machine learning and reinforcement learning.")
    
with open("TradeSmart_Plus/requirements.txt", "w") as f:
    f.write("""pandas
numpy
matplotlib
seaborn
scikit-learn
tensorflow==2.12.0
xgboost
ta-lib
yfinance
vaderSentiment
stable-baselines3
gym
alpaca-trade-api
fpdf""")

# Create empty Python scripts in the scripts folder
script_files = [
    "fetch_stock_data.py",
    "models.py",
    "backtest_strategy.py",
    "sentiment_analysis.py",
    "generate_report.py",
    "rl_trading_env.py"
]

for script in script_files:
    open(f"TradeSmart_Plus/scripts/{script}", 'w').close()

# Create an empty test file
open("TradeSmart_Plus/tests/test_backtest.py", 'w').close()

print("Directory structure created successfully!")
