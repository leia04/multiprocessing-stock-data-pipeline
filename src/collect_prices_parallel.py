import time
import FinanceDataReader as fdr
from multiprocessing import Pool

def merging_stock_data(code: str):
    merge_stock_list = []
    stock_list = fdr.DataReader(code, "2020").reset_index().values.tolist()
    for row in stock_list:
        row.append(code)
        merge_stock_list.append(row)
    return merge_stock_list

def collect_stock_parallel(code_list: list[str], n_procs: int = 32):
    start_time = time.time()

    with Pool(n_procs) as p:
        result = p.map(merging_stock_data, code_list)

    end_time = time.time()
    elapsed = end_time - start_time
    return result, elapsed  # result: list[list[rows]]

if __name__ == "__main__":
    from stock_codes import get_code_list

    codes = get_code_list("2020-01-01")
    result, elapsed = collect_stock_parallel(codes, n_procs=32)
    print(f"Companies processed: {len(result)}")
    print(f"Time taken (multiprocessing): {elapsed:.2f} seconds")
