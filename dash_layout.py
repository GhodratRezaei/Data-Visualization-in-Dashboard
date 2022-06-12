import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output

# Add Dataframe
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]
})


fig = px.bar( df, x = 'Fruit', y = 'Amount', color = 'City', barmode='group')




app = dash.Dash(__name__)
app.layout = html.Div(  children= [
    html.H1( children= 'DashBoard' , style={'textAlign' : 'center'} ),
    dcc.Dropdown(options= [ {'label': 'New York City' , 'value':'NYC'},
                            {'label':'Montreal', 'value':'MTL'},
                            {'label':'San Francisco', 'value':'SF'}
    ] , value = 'NYC'    ),
    dcc.Graph( id  = 'example-graph-2', figure = fig )

])




















if __name__ == '__main__':
    app.run_server()