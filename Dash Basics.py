import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc




# Read the airline data info into pandas DataFrame
airline_data = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
    encoding = 'ISO-8859-1',
    dtype={'Div1Airport': str, 'Div1TailNum': str,
           'Div2Airport': str, 'Div2TailNum': str}
)

# Sampling data
data = airline_data.sample(n = 500, random_state= 42)

#Express Plotly
fig = px.pie(data, values = 'Flights', names='DistanceGroup',
             title = 'Distance group proportion by flights')

#Creating Dash Application
# Dash title by html.H1, Dash Description by html.P1 and Graph Component by dcc.Graph()
app = dash.Dash(__name__)
#  Create an outer division using html.Div
app.layout = html.Div(
    children=[html.H1('Airline DashBoard',  style={'textAlign':'center'  , 'color':'#503D36', 'font_size':40}),

              html.P(' Proportion of distance group (250 mile distance interval group) by flights.  ', style = {'textAlign':'center', 'color':'#F57241'}),
              dcc.Graph(figure = fig)  # fig was defined by Express plotly
              ])



if __name__ =='__main__':
    app.run_server()
