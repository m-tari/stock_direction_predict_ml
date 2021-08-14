### status: under development
## Motivation
Is there any pattern in the day to day movement of the stock prices? Can we build a successful trading strategy based on this insight?
The motivation of this project is to replicate the results of the [repository of Buffalo Capital Management](https://github.com/wzchen/stock_market_prediction) and see if markets are still predictable in 2021. The original Kaggle competition is [here](https://www.kaggle.com/c/boston-data-festival-hackathon).
 - Given the opening, closing, min, max, and volume of a stock in the previous 9 days (and given the opening price of a stock on day 10) can we predict the directional movement of a stock on day 10?

Web-App: [https://stock-web-app-ml.herokuapp.com/](https://stock-web-app-ml.herokuapp.com/)

## Files
- **process.ipynb**: A Jupyter Notebook describing my work.
- **datasets/ohlc_data.csv**: A csv file containing opening, closing, min, max, and volume of 94 stock in 500 days. The first opening date price is scaled to 1.
Here is the closing price data of the 94 tickers in 500 days:
![ohlc_data](./images/stocks_closePrice.png)

## Installation

Install the requiremnts of this project with pip

```bash
pip install -r requirements.txt
```
    
And then run `jupyter notebook`

```bash
cd stock_direction_predict_ml
jupyter notebook process.ipynb
```  
## Insights
It seems that the closing price is negatively correlated to the upward/downward movement of the last day's price.
![correlation_interday_intraday](./images/correlation_interday_intraday.png)

## Performance

![graph_statistics](./images/graph_statistics.png)


## Next steps
- Comparing multiple machine learning models
- What happens if we change the number of previous days (n) from 10 to other numbers?
- Is there subsets of data that represents industries with correlations? How would dividing the dataset change the performance of the model?
- Will tuning the hyperparameteres improve the model?
- What is the predictive power of the model applied to the recent years of the US and other countries data?
