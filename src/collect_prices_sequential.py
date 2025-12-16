import time
from tqdm import tqdm
import FinanceDataReader as fdr

def collect_one_code(code: str, start: str = "2020"):
    rows = []
    stock_list = fdr.DataReader(code, start).reset_index().values.tolist()
    for row in stock_list:
        row.append(code)
        rows.append(row)
    return rows

def collect_stock_sequential(code_list: list[str], start: str = "2020"):
    start_time = time.time()
    merged = []
    for code in tqdm(code_list, desc="Collecting (sequential)"):
        merged.extend(collect_one_code(code, start=start))
    end_time = time.time()
    return merged, (end_time - start_time)

if __name__ == "__main__":
    from stock_codes import get_code_list

    codes = get_code_list("2020-01-01")
    data, elapsed = collect_stock_sequential(codes, start="2020")
    print(f"Rows collected: {len(data)}")
    print(f"Time taken (sequential): {elapsed:.2f} seconds")
