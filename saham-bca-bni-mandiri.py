# -*- coding: utf-8 -*-
"""TugasBesar_Visdat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o_bAmILBJCZ3M5pt4St5065OFoYyD8uy

#Tugas Besar - Visualisasi Data Interaktif Fluktuasi Harga Saham BBNI, BBCA, dan BMRI

kelas: IF-43-GAB02
##Muhammad Rifqi Arrahim (1301190425)
"""
import flask
import os
# Data handling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Bokeh libraries
from bokeh.io import output_file, output_notebook, curdoc
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource

app = flask.Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
        """##Import Data"""

        BBCA = pd.read_csv("./data/BBCA.JK.csv")
        BBNI = pd.read_csv("./data/BBNI.JK.csv")
        BMRI = pd.read_csv("./data/BMRI.JK.csv")

        """##Mengubah tipe kolom 'Date' menjadi DateTime"""

        BBCA['Date'] = pd.to_datetime(BBCA.Date)

        BBNI['Date'] = pd.to_datetime(BBNI.Date)

        BMRI['Date'] = pd.to_datetime(BMRI.Date)

        """## Set output file extension"""

        #output_file('Saham.html', title='Saham')

        # Output the visualization directly in the notebook
        output_notebook()

        """##Set CollumnDataSource"""

        cds_BBCA = ColumnDataSource(BBCA)
        cds_BBNI = ColumnDataSource(BBNI)
        cds_BMRI = ColumnDataSource(BMRI)

        """##Konfigurasi figure"""

        fig_adj = figure(plot_height=500,
                plot_width=800,
                x_axis_label='Date',
                y_axis_label='Adj Close',
                title='Adjusted Close')

        fig_vol = figure(x_axis_type='datetime',
                        plot_width=800,
                        plot_height=500,
                        x_axis_label='Date',
                        y_axis_label='Volume',
                        title='Volume')

        fig_open = figure(x_axis_type='datetime',
                        plot_width=800,
                        plot_height=500,
                        x_axis_label='Date',
                        y_axis_label='Open',
                        title='Open')

        fig_close = figure(x_axis_type='datetime',
                        plot_width=800,
                        plot_height=500,
                        x_axis_label='Date',
                        y_axis_label='Volume',
                        title='Close')

        fig_high = figure(x_axis_type='datetime',
                        plot_width=800,
                        plot_height=500,
                        x_axis_label='Date',
                        y_axis_label='Volume',
                        title='High')

        fig_low = figure(x_axis_type='datetime',
                        plot_width=800,
                        plot_height=500,
                        x_axis_label='Date',
                        y_axis_label='Volume',
                        title='Low')

        """## Draw each Line in Graph"""

        fig_adj.line(x='Date', y='Adj Close', 
                color='Orange', legend_label='BBNI',
                source=cds_BBNI)

        fig_adj.line(x='Date', y='Adj Close', 
                color='Yellow', legend_label='BMRI',
                source=cds_BMRI)

        fig_adj.line(x='Date', y='Adj Close', 
                color='Blue', legend_label='BBCA',
                source=cds_BBCA)

        fig_adj.legend.location = 'top_right'

        fig_vol.line(x='Date', y='Volume', 
                color='Orange', legend_label='BBNI',
                source=cds_BBNI)

        fig_vol.line(x='Date', y='Volume', 
                color='Yellow', legend_label='BMRI',
                source=cds_BMRI)

        fig_vol.line(x='Date', y='Volume', 
                color='Blue', legend_label='BBCA',
                source=cds_BBCA)

        fig_vol.legend.location = 'top_right'

        fig_open.line(x='Date', y='Open', 
                color='Orange', legend_label='BBNI',
                source=cds_BBNI)

        fig_open.line(x='Date', y='Open', 
                color='Yellow', legend_label='BMRI',
                source=cds_BMRI)

        fig_open.line(x='Date', y='Open', 
                color='Blue', legend_label='BBCA',
                source=cds_BBCA)

        fig_open.legend.location = 'top_right'

        fig_close.line(x='Date', y='Close', 
                color='Orange', legend_label='BBNI',
                source=cds_BBNI)

        fig_close.line(x='Date', y='Close', 
                color='Yellow', legend_label='BMRI',
                source=cds_BMRI)

        fig_close.line(x='Date', y='Close', 
                color='Blue', legend_label='BBCA',
                source=cds_BBCA)

        fig_close.legend.location = 'top_right'

        fig_high.line(x='Date', y='High', 
                color='Orange', legend_label='BBNI',
                source=cds_BBNI)

        fig_high.line(x='Date', y='High', 
                color='Yellow', legend_label='BMRI',
                source=cds_BMRI)

        fig_high.line(x='Date', y='High', 
                color='Blue', legend_label='BBCA',
                source=cds_BBCA)

        fig_high.legend.location = 'top_right'

        fig_low.line(x='Date', y='Low', 
                color='Orange', legend_label='BBNI',
                source=cds_BBNI)

        fig_low.line(x='Date', y='Low', 
                color='Yellow', legend_label='BMRI',
                source=cds_BMRI)

        fig_low.line(x='Date', y='Low', 
                color='Blue', legend_label='BBCA',
                source=cds_BBCA)

        fig_low.legend.location = 'top_right'

        """## HoverTool"""

        tooltips = [
                ('Date', '@Date{%F}'),
                ('Open', '@Open'),
                ('High', '@High'),
                ('Low', '@Low'),
                ('Close', '@Close'),
                ('Adj Close', '@Adj Close'),
                ('Volume', '@Volume'),
                ]
        fig_adj.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))
        fig_vol.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))
        fig_open.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))
        fig_close.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))
        fig_high.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))
        fig_low.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))

        """##Set 'Hide graph at clicked Legend' function"""

        fig_adj.legend.click_policy = 'hide'
        fig_vol.legend.click_policy = 'hide'
        fig_open.legend.click_policy = 'hide'
        fig_close.legend.click_policy = 'hide'
        fig_high.legend.click_policy = 'hide'
        fig_low.legend.click_policy = 'hide'

        """##Set Panel"""

        panel_adj= Panel(child=fig_adj, title='Adjusted Close')
        panel_vol = Panel(child=fig_vol, title='Volume')
        panel_open = Panel(child=fig_open, title='Open')
        panel_close = Panel(child=fig_close, title='Close')
        panel_high = Panel(child=fig_high, title='High')
        panel_low = Panel(child=fig_low, title='Low')

        tabs = Tabs(tabs=[panel_adj, panel_vol, panel_open, panel_close, panel_high, panel_low])

        """## Show Plot"""
        show(tabs)
        #curdoc().add_root(tabs)
        #curdoc().title = "Pergerakan Saham BCA, BNI, Mandiri"
if __name__ == "__main__":
        app.secret.key = 'rahasia'
        app.debug = True
        app.run()