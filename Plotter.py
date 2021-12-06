# Imports
import pandas as pd
import plotly.express as px
import plotly.io as pio
import random
import datetime
import plotly.graph_objects as go

class Plotter:
    def __init__(self):
        self.dataframe = pd.read_csv('data/data.csv')
        self.temp = self.dataframe.copy()
        self.temp = self.temp.drop([0, 1])
        self.dataPrep()
        
        # Settings
        pio.renderers.default = 'vscode'
        pio.templates.default = 'plotly'
        print("Module is set up!")
        
    def counter(self, column):
        copy = self.temp.copy()
        return copy.groupby([column]).size().reset_index(name='count')
    
    def dataPrep(self):
        print("Preparing the data... \n")
        # Time
        self.temp['StartDate'] = pd.to_datetime(self.temp['StartDate'], format='%Y-%m-%d %H:%M:%S')
        self.temp['EndDate'] = pd.to_datetime(self.temp['EndDate'], format='%Y-%m-%d %H:%M:%S')
        # Edge cases
        ages = ['under 18', 'above 25']
        self.temp = self.temp[self.temp.Q2.isin(ages) == False]
        self.temp = self.temp[self.temp.Q3 != 'Never']
        self.temp = self.temp.reset_index(drop=True)
        
    def raffle(self):
        email_column = self.temp.loc[:,'Q1']
        emails = email_column.values
        print("Selected winner is", random.choice(emails))
        
    def vis(self, plot_num, question):
        if plot_num == 'single bar count':
            group_data = self.counter(self.temp, question)
            figure = px.bar(data_frame=group_data, x=copy, y='count')
            figure.show()
        
    
    