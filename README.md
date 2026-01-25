# Retail Investment Strategy Backtester
This project is an interactive backtesting engine that can be used to compare common retail investment strategies over historical equity data. The app allows the user to simulate and evaluate different contribution, timing, and portfolio construction rules using a graphical interface built with Panel.

The tool is intended for educational and anaytical purposes with the purpose to provide insight into how different systematic investment approaches perform over time.


## To launch the app:
`panel serve interface.py --autoreload --show`
This will start a local server and open the app in your browser.


## Features
- Interactive dashboard built with **Panel**, **HoloViews**, and **hvPlot**
- Support for **single asset** and **multi-asset portfolios**
- Multiple stock selection modes:
    - Pre-defined ticker list
    - GICS Sector selection
    - Manual ticker input
- Strategy comparison
- Key performance metrics


## Available Strategies
The following strategies can be selected simultaneously for comparison:

- **Dollar-Cost Averaging (DCA)**  
  Invests a fixed amount at regular monthly intervals, regardless of price.

- **Double Down DCA**  
  Increases investment when prices fall beyond a user-defined threshold.

- **Lump Sum Investment**  
  Invests the entire capital at the start of the investment period.

- **Simple Moving Average (SMA) DCA – Momentum**  
  Invests only when prices are above the SMA, following momentum.

- **Simple Moving Average (SMA) DCA – Mean Reversion**  
  Invests only when prices are below the SMA, assuming mean reversion.

- **Value Averaging**  
  Targets a predefined portfolio growth path, investing more when the portfolio underperforms the target and less when it overperforms.


### Strategy parameters (rules)
- Monthly Contribution ($)
    The fixed amount invested each month. 

- Double Down Threshold
    The relative price decline required to trigger an increased contribution under the Double Down DCA strategy. For example, a value of 0.15 implies that the monthly investment is increased when the asset price has fallen by at least 15% from the rolling 52-week-high.

- SMA Period
    The number of past trading days used to compute the Simple Moving Average. 

- Desired Monthly Growth Rate (Value Averaging)
    The target monthly growth rate of the portfolio under the Value Averaging strategy. Contributions are dynamically adjusted to keep the portfolio value close to a predefined growth path.


## Key Metrics
For each strategy, the application computes and displays:
- Total invested capital
- Final portfolio value
- Return on Investment (ROI)
- Internal Rate of Return (IRR)
- Compound Annual Growth Rate (CAGR)
- Maximum drawdown
- Calmar ratio
- Investment horizon (years)


## Project Structure



## Notes
The app is designed to run locally and does not require cloud deployment.
Results depend on historical price data and do not constitute investment advice.


## Authors
Maxim Milde & Zahid Pashayev
Developed as a university project on Data Processing with Python