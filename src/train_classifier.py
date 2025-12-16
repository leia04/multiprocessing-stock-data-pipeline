import time
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss

def train_xgb_classifier(stock_df):
    stock_df = stock_df.copy()

    stock_df["up"] = (stock_df["Change"] > 0).astype(int)

    X = stock_df[["Open", "High", "Low", "Close", "Volume"]]
    y = stock_df["up"]

    train_input, test_input, train_target, test_target = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    param_fixed = {
        "learning_rate": 0.1,
        "max_depth": 10,
        "n_estimators": 150,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "gamma": 0.2,
    }

    start_time = time.time()

    model = xgb.XGBClassifier(objective="binary:logistic", random_state=42, **param_fixed)
    model.fit(train_input, train_target)

    train_score = model.score(train_input, train_target)
    test_score = model.score(test_input, test_target)

    probabilities = model.predict_proba(test_input)
    loss = log_loss(test_target, probabilities)

    elapsed = time.time() - start_time

    return {
        "train_score": train_score,
        "test_score": test_score,
        "log_loss": float(loss),
        "train_time_sec": elapsed,
        "model": model,
    }

if __name__ == "__main__":
    print("train_model.py is ready. Pass a prepared stock_df to train_xgb_classifier().")
