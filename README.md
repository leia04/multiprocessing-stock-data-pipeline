# High-Throughput Stock Data Pipeline & Prediction

## Abstract
This project focuses on accelerating large-scale stock data collection using **multiprocessing** rather than optimizing model performance.  
Using stock price data from all Korean listed companies since 2020, the primary goal was to identify and resolve data collection bottlenecks by applying parallel processing techniques.


## Problem
- Collect daily stock price data for **all listed Korean companies** from 2020 to the present.
- Sequential data collection required thousands of API calls, resulting in long execution times.
- The project required a scalable solution to reduce data ingestion time while maintaining data integrity.

## Key Findings
- Approximately **2,160 company tickers** were collected.
- The final dataset contained roughly **2.1 million rows** of stock price data.
- Execution time was reduced from **~205 seconds to ~46 seconds** using multiprocessing.
- Parallel processing achieved an approximate **77% reduction in data collection time**, confirming that I/O-bound workloads benefit significantly from multiprocessing.


## Approach
- Retrieved listed company codes by crawling the Korea Exchange (KRX) corporate list.
- Collected stock price data using the **FinanceDataReader** library.
- Implemented two data collection strategies:
  - **Sequential processing** as a baseline.
  - **Multiprocessing-based parallel processing** using a process pool.
- Optimized in-memory data handling by converting DataFrames to lists during collection.
- Measured execution time before and after parallelization to quantify performance improvements.
- Built a simple classification model to predict whether the stock price change would be positive or negative, as a downstream use case.



## Code
- Stock ticker collection and preprocessing from KRX-listed companies.
- Sequential stock data collection as a performance baseline.
- Parallel stock data collection using a multiprocessing pool.
- Transformation of nested lists into a unified DataFrame.
- Binary classification model for predicting stock price direction.


## Tools and Libraries
- Python
- pandas
- FinanceDataReader
- tqdm
- multiprocessing (Python standard library)
- XGBoost
- scikit-learn



## Contribution
- Designed and implemented a large-scale stock data ingestion pipeline.
- Identified performance bottlenecks in sequential data collection.
- Applied multiprocessing to significantly reduce execution time.
- Quantitatively evaluated performance improvements.
- Integrated data collection results into a machine learning workflow.
