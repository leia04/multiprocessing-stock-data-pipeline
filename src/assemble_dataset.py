import pandas as pd

COLUMNS = ["Timestamp", "Open", "High", "Low", "Close", "Volume", "Change", "Code"]

def flatten_result(result: list[list[list]]):
    # result: [ [row,row,...], [row,row,...], ... ]
    return [item for sublist in result for item in sublist]

def build_stock_df(flat_rows: list[list]) -> pd.DataFrame:
    stock_df = pd.DataFrame(flat_rows, columns=COLUMNS)
    stock_df["Timestamp"] = pd.to_datetime(stock_df["Timestamp"])
    return stock_df

if __name__ == "__main__":
    # quick self-test (expects user to pass real data)
    print("build_dataframe.py is ready.")
