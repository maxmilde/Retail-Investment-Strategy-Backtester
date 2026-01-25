# Retail Investment Strategy Backtester
This project is an interactive backtestng application that can be used to compare common retail investment strategies over historical equity data. The app allows the user to simulate and evaluate different controbution, timing, and portfolio construction rules using a graphical interface built with Panel.
The tool is intended for educational and anaytical purposes with the purpose to provide insight into how different systematic investment approaches perform over time.


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
The following strategies are implemented and can be selected simultaneously for comparison:

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