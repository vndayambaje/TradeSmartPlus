from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.metrics import accuracy_score

def train_random_forest(X_train, y_train, X_val, y_val):
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)
    
    y_val_pred = rf.predict(X_val)
    accuracy = accuracy_score(y_val, y_val_pred)
    
    return rf, accuracy

def train_xgboost(X_train, y_train, X_val, y_val):
    xgb = XGBClassifier(random_state=42, use_label_encoder=False)
    xgb.fit(X_train, y_train)
    
    y_val_pred = xgb.predict(X_val)
    accuracy = accuracy_score(y_val, y_val_pred)
    
    return xgb, accuracy

def train_lstm_model(X_train, y_train, X_val, y_val):
    X_train_reshaped = X_train.values.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_val_reshaped = X_val.values.reshape((X_val.shape[0], X_val.shape[1], 1))
    
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train_reshaped.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1, activation='sigmoid'))  # Binary classification
    
    model.compile(optimizer='adam', loss='binary_crossentropy')
    model.fit(X_train_reshaped, y_train, epochs=20, batch_size=32, validation_data=(X_val_reshaped, y_val))
    
    y_val_pred = model.predict(X_val_reshaped).flatten()
    y_val_pred_reshaped = (y_val_pred > 0.5).astype(int)
    
    accuracy = accuracy_score(y_val, y_val_pred_reshaped)
    
    return model, accuracy
