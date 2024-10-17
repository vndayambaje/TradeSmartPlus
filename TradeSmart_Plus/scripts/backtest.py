import pandas as pd

def generate_signals(data):
    signals = pd.DataFrame(index=data.index)
    signals['Signal'] = 0
    
    signals.loc[(data['RSI'] < 30) & (data['Close'] > data['SMA_20']), 'Signal'] = 1  # Buy
    signals.loc[(data['RSI'] > 70) & (data['Close'] < data['SMA_20']), 'Signal'] = -1  # Sell
    
    return signals

def backtest_strategy(data, signals, initial_balance=10000):
    data = data.loc[signals.index]  # Align data to signals
    balance = initial_balance
    position = 0
    balance_history = []

    for i in range(len(signals)):
        if signals['Signal'][i] == 1 and position == 0:  # Buy
            position = balance / data['Close'][i]
            balance = 0
        elif signals['Signal'][i] == -1 and position > 0:  # Sell
            balance = position * data['Close'][i]
            position = 0
        balance_history.append(balance if balance > 0 else position * data['Close'][i])

    data['Balance'] = balance_history
    return data


