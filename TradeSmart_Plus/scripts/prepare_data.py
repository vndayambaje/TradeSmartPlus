from sklearn.model_selection import train_test_split
import numpy as np

def prepare_data(ticker_data):
    X = ticker_data[['SMA_20', 'RSI']].dropna()
    y = np.where(ticker_data['Close'].shift(-1) > ticker_data['Close'], 1, 0)
    
    # Align y with X after dropping NA values
    y = pd.Series(y, index=X.index)
    
    # Split data into training, validation, and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)
    
    return X_train, X_val, X_test, y_train, y_val, y_test
