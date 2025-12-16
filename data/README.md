# Data Source

This project uses stock market data collected from publicly available sources.  
Company ticker information is obtained directly from the **Korea Exchange (KRX)**.


## Company Ticker Data
Company ticker codes are retrieved by crawling the KRX corporate list using the following code:

```python
code_data = pd.read_html(
    "http://kind.krx.co.kr/corpgeneral/corpList.do?method=download", header=0)[0]
```
