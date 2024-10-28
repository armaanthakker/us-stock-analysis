# us-stock-analysis

## Introduction
In this project, I worked on a data research task focused on analyzing daily stock returns for U.S. stocks using daily time series log returns. The goal was to independently gather stock data using the Finnhub and Yahoo Finance APIs, process it, and then analyze it to pull out meaningful insights. Using Python libraries like pandas for data manipulation and matplotlib for visualization, I retrieved the data, calculated daily log returns, and ran some descriptive statistics to get a clearer picture of stock trends and patterns over the selected timeframe. This process allowed me to dive into time series analysis and get hands-on with applied data processing techniques.

Data Preprocessing/Processing
In tackling the dataset’s over 500,000 observations, identifying patterns within the noise was challenging, and processing times were considerable. To streamline the data, I decided to randomly sample by ticker symbol and group daily returns into two-day periods, which reduced the data volume and allowed trends to emerge more clearly. I also considered removing NA and zero values, but given that many low-volume stocks in the U.S. markets often show zero trading volume, excluding these would have compromised the integrity of the dataset. To manage the heavy processing load, I implemented batch processing, which further optimized setup and processing efficiency. Altogether, these adjustments allowed for a more practical and focused analysis while preserving the dataset’s true market representation.

Aggregate Analysis
1. Distribution of Mean Log Returns Across All Stocks
Screenshot 2024-10-27 at 9 16 22 PM

The distribution of mean log returns is heavily concentrated around zero, indicating that most stocks in the dataset have an average return close to zero. This pattern suggests that, overall, the stocks tend to neither gain nor lose significantly on average, reflecting a market state where returns are balanced with few extreme values. This type of distribution may be typical in a diversified portfolio, where individual extremes are muted by the aggregation.

2. Volatility (Standard Deviation of Log Returns) Across Stocks
Screenshot 2024-10-27 at 9 17 25 PM

The volatility plot, represented by the standard deviation of log returns, shows that most stocks experience low to moderate volatility, with a few stocks displaying significantly higher values as outliers. This concentration of lower volatility stocks aligns with the general risk-averse nature of many market participants, who seek stable returns. However, the presence of outliers suggests that there are a few highly volatile stocks, which could represent higher-risk opportunities or unstable market conditions for those particular stocks.

3. Min vs. Max Log Returns for Each Stock
Screenshot 2024-10-27 at 9 19 57 PM

The min vs. max log returns plot reveals that most stocks are clustered within a narrow range, indicating relatively stable performance with limited extremes. However, there are outliers with exceptionally high maximum or low minimum returns, suggesting that certain stocks experience more pronounced fluctuations. This plot highlights the variation in individual stock behavior, where some stocks may be prone to extreme gains or losses, reflecting high-risk, high-reward dynamics.

4. Mean Log Return vs. Volatility (Standard Deviation of Log Return) for Each Stock
Screenshot 2024-10-27 at 9 20 33 PM

The relationship between mean log return and volatility shows that most stocks have low average returns and low volatility, with a few outliers that have both higher volatility and varying mean returns. This distribution is consistent with the risk-return tradeoff principle, where higher returns are often associated with higher risk (volatility). The clustering at low mean and low volatility indicates a significant portion of stable stocks, while the outliers suggest that a few stocks offer potential for higher gains at the cost of greater uncertainty.

5. Correlation Matrix of Summary Statistics
Screenshot 2024-10-27 at 9 21 00 PM

The correlation matrix provides insights into how different summary statistics are related:

Mean Log Return and Volatility: A low or negative correlation suggests that stocks with high average returns do not necessarily exhibit higher volatility, indicating that high returns can be achieved without excessive risk. Minimum and Maximum Returns: The strong positive correlation between minimum and maximum returns reflects that stocks with extreme high values also tend to have extreme low values, signifying volatility. Additional Things: The negative correlation between standard deviation and minimum returns suggests that more volatile stocks tend to experience lower minimum returns, underlining the downside risk associated with volatility. Overall, this matrix gives an understanding of how volatility, returns, and risk measures interact within the dataset.

Time Series Analysis
1. Autocorrelation Analysis
Screenshot 2024-10-27 at 9 27 52 PM

To understand the persistence of returns over time, I calculated and plotted the average autocorrelation across all stocks for lags from 1 to 30 days. The average autocorrelation plot indicates that while there is some short-term autocorrelation within the first few lags, it rapidly diminishes and stabilizes near zero for longer lags.

This finding aligns with the weak-form efficient market hypothesis, which posits that stock returns should be largely uncorrelated over time in an efficient market. The slight initial autocorrelation might be due to microstructure effects or delayed responses to market news.

2. Rolling Mean and Volatility
Screenshot 2024-10-27 at 9 28 34 PM

To explore the time-varying nature of returns and volatility, I used a 20-day rolling window to calculate both the rolling mean and rolling standard deviation of log returns for selected stocks.

The mean fluctuates around zero, consistent with the expectation that average stock returns are zero over short intervals. Rolling Standard Deviation: This measure, also known as rolling volatility, reflects periods of increased market activity and investor uncertainty. For instance, spikes in volatility suggest periods where stocks experienced rapid price fluctuations.

The rolling volatility plot indicates clusters of high and low volatility, a common phenomenon in financial markets often described as "volatility clustering." This effect suggests that large changes in returns are likely to be followed by more large changes, and small changes by more small changes.

3. Day-of-Week Effect
Screenshot 2024-10-27 at 9 30 07 PM

To investigate potential seasonal effects, I calculated the average log return for each day of the week across all stocks. The results are visualized in Figure 3. Interestingly, there appears to be a day-of-the-week effect:

Wednesday shows the highest positive average log return. Friday and Thursday exhibit slightly negative returns on average.

The "day-of-the-week effect" is a well-documented anomaly in financial literature, where certain days consistently yield higher or lower returns. Here, Wednesday’s positive returns and Friday’s slightly negative returns could reflect trading behaviors influenced by mid-week optimism or end-of-week caution.

4. 30-Day Rolling Volatility Across All Stocks
Screenshot 2024-10-27 at 9 30 52 PM


I calculated the average 30-day rolling standard deviation across all stocks to analyze overall market volatility trends (Figure 4). This plot offers insights into periods of heightened or reduced market volatility, which could correspond to macroeconomic events or shifts in investor sentiment.

The 30-day average rolling volatility curve shows periods of increased volatility that likely align with significant market events. Higher rolling volatility signals periods of uncertainty or market stress, while lower volatility periods suggest stability.

Conclusion
In short, this project gave a closer look at U.S. stock behavior, from spotting volatility waves to seeing a mid-week boost in returns. By sampling and using batch processing, I could make sense of a huge dataset without losing key trends in the noise. While the results align with known market patterns, this deep dive highlighted both the challenges and rewards of working with real-world financial data on a big scale.
