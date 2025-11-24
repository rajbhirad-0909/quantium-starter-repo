import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv("processed_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

# Create Dash app
app = Dash(__name__)
server = app.server   # IMPORTANT for deployment

# ---------------------------
# APP LAYOUT
# ---------------------------
app.layout = html.Div(
    style={
        "backgroundColor": "#f5f7fa",
        "fontFamily": "Arial",
        "padding": "30px"
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualizer",
            style={"textAlign": "center", "color": "#E91E63"}
        ),

        html.Div(
            [
                html.Label(
                    "Filter by Region:",
                    style={"fontSize": "20px", "fontWeight": "bold"}
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",  # default
                    labelStyle={"display": "inline-block", "marginRight": "20px"},
                    style={"marginTop": "10px", "marginBottom": "20px"}
                ),
            ],
            style={"textAlign": "center", "marginBottom": "20px"},
        ),

        dcc.Graph(id="sales-graph")
    ]
)

# ---------------------------
# CALLBACK FOR INTERACTIVITY
# ---------------------------
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Daily Pink Morsel Sales",
        color="region",
        labels={"date": "Date", "sales": "Total Sales ($)"}
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f5f7fa",
        title_font_size=24,
        font=dict(size=14),
        xaxis=dict(showgrid=True, gridcolor="#ddd"),
        yaxis=dict(showgrid=True, gridcolor="#ddd")
    )

    return fig


# ---------------------------
# Run App
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)




