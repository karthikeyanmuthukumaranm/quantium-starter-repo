import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("data/processed_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Initialize app
app = Dash(__name__)

# Layout
app.layout = html.Div(
    className="app-container",
    children=[
        html.H1("Soul Foods – Pink Morsel Sales Visualiser"),

        html.Div(
            className="card",
            children=[
                html.Div(
                    className="radio-group",
                    children=[
                        html.Label("Select Region:"),
                        dcc.RadioItems(
                            id="region-selector",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            inline=True
                        ),
                    ],
                ),

                dcc.Graph(id="sales-line-chart"),
            ],
        ),
    ],
)

# Callback
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value"),
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
        color = "Region"
    else:
        filtered_df = df[df["Region"] == selected_region]
        color = None

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color=color,
        labels={
            "Date": "Date",
            "Sales": "Total Sales ($)",
        },
        title="Pink Morsel Sales Over Time",
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_x=0.5,
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)
