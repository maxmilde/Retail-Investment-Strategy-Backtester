import panel as pn
import pandas as pd
pn.extension()
import hvplot.pandas

from dca_simulator.data_loader import load_price_data
from dca_simulator.strategies import (dca_standard, dca_DD, lump_sum, dca_sma, value_averaging)


#Widgets
##text box for ticker
ticker = pn.widgets.TextInput(name="Ticker", value="AAPL", width=150)

##date picker
start_date = pn.widgets.DatePicker(name="Start Date", value=pd.to_datetime("2010-01-01"))
end_date = pn.widgets.DatePicker(name="End Date", value=pd.to_datetime("2025-01-01"))

##sliders for strategy parameters
monthly_contrib = pn.widgets.IntSlider(name="Monthly Contribution ($)", start=50, end=1000, step=50, value=150)
growth_slider = pn.widgets.FloatSlider(name="Desired Monthly Growth rate (SMA)", start=0.001, end=0.01, step=0.001, value=0.006)
sma_period_slider = pn.widgets.IntSlider(name="SMA period", start=10, end=300, step=10, value=90)
DD_treshold_slider = pn.widgets.FloatSlider(name="Double Down Treshold", start=0.05, end=0.6, step=0.05, value=0.15)


##box checker for strategy selection
strategy_selector = pn.widgets.CheckBoxGroup(name="Strategies", 
                                             options=["DCA",  
                                                      "Double Down DCA", 
                                                       "Lump Sum", 
                                                       "Simple Moving Average DCA", 
                                                       "Value Averaging"],
                                                       value=["DCA"],
                                                       inline=False)

##dropdown for var plotting
plot_var = pn.widgets.Select(name="Variable to plot",
                             options=["portf_value", "invested_total", "shares_total", "profit_loss"],
                             value="portf_value")

##run button
run_button = pn.widgets.Button(name="Run Simulation", button_type="primary")




#Output
##plot
preview_pane = pn.pane.Markdown("*(Data preview will appear here after pressing running simulation)*")

plot_pane = pn.pane.HoloViews(None, sizing_mode="fixed")

##metrics comparison table
metrics_pane = pn.pane.Markdown("*(Metrics table will appear here after running simulation)*")



#Layout
template = pn.template.FastListTemplate(title = "Retail Investment Strategy Backtester",
    sidebar=[ticker, 
             start_date, 
             end_date, 
             monthly_contrib, 
             growth_slider,
             sma_period_slider,
             DD_treshold_slider,
             pn.pane.Markdown("### Strategies"), 
             strategy_selector, 
             pn.pane.Markdown("### Plot Settings"), 
             plot_var, 
             run_button],

    main=[pn.pane.Markdown("## Data Preview"),
          preview_pane,
          pn.pane.Markdown("## Strategy Plot"),
          pn.Column(plot_pane),
          pn.pane.Markdown("## Key Metrics Comparison"),
          metrics_pane])

template.servable()



def run_simulation(simulation):
    """Run the simulation with the specified parameters from the "Run Simulation" button"""

    selected_ticker = ticker.value
    selected_strategies = strategy_selector.value
    selected_var = plot_var.value
    start = start_date.value
    end = end_date.value
    monthly_c = monthly_contrib.value
    growth = growth_slider.value
    sma_p = sma_period_slider.value
    dd_tresh = DD_treshold_slider.value

    #Data loading
    try:    
        df = load_price_data(selected_ticker, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"))

        preview_pane.object = f'### Data Preview for {selected_ticker}\n{df.tail().to_markdown()}'
    
        metrics_pane.object = "*(metrics to be computed)*"

    except Exception as e:
        plot_pane.object = f"**Error loading the data:** {str(e)}"
        metrics_pane.object = ""


    #Strategies
    results = {}

    for strat in selected_strategies:
        if strat == "DCA":
            results["DCA"] = dca_standard(df, monthly_c)
        
        elif strat == "Double Down DCA":
            results["Double Down DCA"] = dca_DD(df, monthly_c, dd_tresh)

        elif strat == "Lump Sum":
            results["Lump Sum"] = lump_sum(df, monthly_c)

        elif strat == "Simple Moving Average DCA":
            results["Simple Moving Average DCA"] = dca_sma(df, monthly_c, sma_p)
        
        elif strat == "Value Averaging":
            results["Value Averaging"] = value_averaging(df, growth, monthly_c)




    #Plotting
    if len(results) == 0:
        plot_pane.object = "**No strategies were selected**"
        return
    
    plots = []

    for name, df_result in results.items():
        curve = df_result.hvplot(x="Date", y=selected_var, label=name, width=900, height=400, interactive=True)
        plots.append(curve)

    interact_plot = plots[0]
    for curve in plots[1:]:
        interact_plot *= curve #add the curves on top of each other

    plot_pane.object = interact_plot


#connecting button with run_simulation
run_button.on_click(run_simulation)