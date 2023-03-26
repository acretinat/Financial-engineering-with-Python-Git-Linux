import dash
from dash import Dash, dcc, html, Output, Input
import dash.dependencies as dd
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px

app = dash.Dash(__name__)

def get_last_price():
    df = pd.read_csv("stock_price.txt", delimiter=',', header=None)
    last_price = df.tail(1).values[0][0]
    return last_price

def get_time_series():
    df = pd.read_csv("stock_price.txt", delimiter=',')
    df.columns = ['price', 'time']
    df['time'] = pd.to_datetime(df['time'])
    return df
  
def get_stock_stats():
    with open("stock_stats.txt", "r") as f:
        stock_stats =  f.read()
    return stock_stats

app.layout = html.Div([
    html.H1('LVMH Moët Hennessy - Louis Vuitton, Société Européenne (MC.PA)'),
    html.P([
        html.Span('Paris - Paris Prix différé. '),
        html.Span('Devise en EUR')
    ]),
    html.P(
        [html.Span('Last Price: ', style={'font-size': '2em'}),
        html.Span(id='last-price', style={'font-weight': 'bold','font-size': '2em'})]
    ),
    html.Div(id='stock-stats'),
    dcc.Graph(
        id='time-series-graph'),

    dcc.Interval(
        id='interval-component',
        interval=5*60*1000, # 5 minutes in milliseconds
        n_intervals=0
    )
])

@app.callback(dd.Output('last-price', 'children'), dd.Input('interval-component', 'n_intervals'))
def update_last_price(n):
    last_price = get_last_price()
    return f"{last_price}"

@app.callback(
    dd.Output('stock-stats', 'children'),
    dd.Input('interval-component', 'n_intervals'))
def update_stock_stats(n):
    stock_stats = get_stock_stats()
    lines = stock_stats.splitlines()
    return [html.P(line, style={'font-weight': 'bold', 'font-size': 'larger'}) if i == 0 else html.P(line) for i, line in enumerate(lines)]

@app.callback(
    dd.Output('time-series-graph', 'figure'),
    dd.Input('interval-component', 'n_intervals'))
def update_time_series_graph(n):
    df = pd.read_csv('stock_price.txt', delimiter=',', header=None)
    df.columns = ['price', 'time']
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    fig = px.line(df, x=df.index, y='price', line_shape ='linear', markers=True)
    fig.update_layout(title='Stock Evolution', xaxis_title='French Time', yaxis_title='Stock Price', xaxis_tickangle=-90)
    return fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port='8050', debug=True)
