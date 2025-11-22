import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the processed dataset
df = pd.read_csv("processed_data.csv")

# Ensure date is correct
df["date"] = pd.to_datetime(df["date"], dayfirst=True)

# Sort by date
df = df.sort_values("date")

# Build the line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Daily Sales of Pink Morsels (Across All Regions)",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualizer", style={'textAlign': 'center'}),

    html.Div([
        dcc.Graph(id='sales-chart', figure=fig)
    ])
])

if __name__ == "__main__":
    app.run(debug=True)

