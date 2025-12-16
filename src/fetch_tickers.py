import pandas as pd

KRX_CORP_LIST_URL = "http://kind.krx.co.kr/corpgeneral/corpList.do?method=download"

def make_code(x) -> str:
    x = str(x)
    return "0" * (6 - len(x)) + x

def load_code_data(url: str = KRX_CORP_LIST_URL) -> pd.DataFrame:
    # 원본 코드와 동일: read_html로 KRX 종목 리스트 확보 :contentReference[oaicite:2]{index=2}
    return pd.read_html(url, header=0)[0]

def get_code_list(listed_before: str = "2020-01-01") -> list[str]:
    code_data = load_code_data()
    code_data["종목코드"] = code_data["종목코드"].apply(make_code)
    code_list = code_data[code_data["상장일"] < listed_before]["종목코드"]
    return code_list.tolist()

if __name__ == "__main__":
    codes = get_code_list("2020-01-01")
    print(f"Number of tickers: {len(codes)}")
    print(codes[:10])
