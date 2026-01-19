import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_sales.csv")

# Convert Date to datetime and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales ($)"
    }
)

# Initialize Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods – Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}
        ),
        dcc.Graph(figure=fig)
    ]
)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
