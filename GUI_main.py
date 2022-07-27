from tkinter.tix import ExFileSelectBox
import PySimpleGUI as sg            # For GUI
import pandas as pd                 # For Graphs
import matplotlib.pyplot as plt     #   ...
import seaborn as sns               #   ...
import os                           # For directory movement
import csv

# Default df
df = pd.read_csv("Dataset.csv") 

# Menus for GUI

button_menu_def_graph = ['Line Graph', 'Bar Graph']
button_menu_def_country = ['All Countries','Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Ecuador', 'Egypt', 'El Salvador', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Krygyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Madagascar', 'Malaysia', 'Maldives', 'Mali', 'Mexico', 'Moldova', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Singapore', 'Slovakia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
button_menu_def_cause = ['All Causes', 'Technical failure', 'Terrorism', 'Weather', 'Human factor', 'Other']
button_menu_def_phase = ['All Phases', 'Flight', 'Landing', 'Parking', 'Takeoff','Taxiing']

# Default Graphs
os.chdir('images')
default_line = 'top_default.png'
default_bar = 'bottom_default.png'
os.chdir('../')

# Top Variables

t_graph = 'Line Graph'
t_country = 'All Countries'
t_cause = 'All Causes'
t_phase = 'All Phases'

# Bottom Variables

b_graph = 'Bar Graph'
b_country = 'All Countries'
b_cause = 'All Causes'
b_phase = 'All Phases'

# GUI Layout

column1 = [
        [sg.Text("Plane Crashes", font = ('Calibri 24 bold'))],
        [sg.Text("from 1918-2022", font = ('Calibri 24 bold'))],
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Combo((button_menu_def_graph),font = ('Calibri 11'), size = (24,2), expand_y = True, default_value='Line Graph', key='t_graph_menu')],
        [sg.Combo((button_menu_def_country),font = ('Calibri 11'), size = (24,6), expand_y = True, default_value='All Countries', key='t_country_menu')],
        [sg.Combo((button_menu_def_cause),font = ('Calibri 11'), size = (24,10), expand_y = True, default_value='All Causes', key='t_cause_menu')],
        [sg.Combo((button_menu_def_phase),font = ('Calibri 11'), size = (24,10), expand_y = True, default_value='All Phases', key='t_phase_menu')],
        [sg.Button(('Refresh Top Image'), font = ('Calibri 12'))],
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Combo((button_menu_def_graph),font = ('Calibri 11'), size = (24,2), expand_y = True, default_value='Bar Graph', key='b_graph_menu')],
        [sg.Combo((button_menu_def_country),font = ('Calibri 11'), size = (24,6), expand_y = True, default_value='All Countries', key='b_country_menu')],
        [sg.Combo((button_menu_def_cause),font = ('Calibri 11'), size = (24,10), expand_y = True, default_value='All Causes', key='b_cause_menu')],
        [sg.Combo((button_menu_def_phase),font = ('Calibri 11'), size = (24,10), expand_y = True, default_value='All Phases', key='b_phase_menu')],
        [sg.Button(('Refresh Bottom Image'), font = ('Calibri 12'))],
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')] #Space between outputs
    ]

column2 = [
        [sg.pin(sg.Image(filename=default_line, key='top_graph'))], 
        [sg.pin(sg.Image(filename=default_bar, key='bottom_graph'))]
    ]

column3 = [
        [sg.Button("Exit", font = ('Calibri 16'))],
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')] #Space between outputs
    ]

layout = [
    [sg.Column(column1),
    sg.VSeperator(),
    sg.Column(column2),
    sg.Column(column3)]
    ]


# GUI Function

def GUI_run():
    # Move to Images (Ouput graphs)
    os.chdir('images')

    # Name Window
    window =sg.Window('Plane Crashes from 1918-2022',layout)
    
    while True:
        # Graph styles
        plt.style.use('fivethirtyeight')

        # Bring in Global Variables
        global t_graph
        global t_country
        global t_cause
        global t_phase

        global b_country
        global b_country
        global b_cause
        global b_phase

        event, values = window.read()

        # Close on Exit
        if event in (sg.WIN_CLOSED, 'Exit'):
                break

        # Top Graph Update Variables Line

        if values['t_graph_menu'] == "Line Graph":
            t_graph = values['t_graph_menu']
        else:
            t_graph = values['t_graph_menu']
        
        # Countries

        if values['t_country_menu'] == "All Countries":
            t_country = values['t_country_menu']
            type(t_country)
            print(t_country)
        else:
            t_country = values['t_country_menu']
            type(t_country)
            print(t_country)

        # Causes

        if values['t_cause_menu'] != 'All Causes':
            t_cause = values['t_cause_menu']
        else:
            t_cause = values['t_cause_menu']

        # Phases

        if values['t_phase_menu'] != 'All Phases':
            t_phase = values['t_phase_menu']
        else:
            t_phase = values['t_phase_menu']

        # Bottom Graph Update Variables

        if values['b_graph_menu'] == "Line Graph":
            b_graph = values['b_graph_menu']
        else:
            b_graph = values['b_graph_menu']

        # Countries

        if values['b_country_menu'] != "All Countries":
            b_country = values['b_country_menu']
        else:
            b_country = values['b_country_menu']

        # Causes

        if values['b_cause_menu'] != 'All Causes':
            b_cause = values['b_cause_menu']
        else:
            b_cause = values['b_cause_menu']

        # Phases

        if values['b_phase_menu'] != 'All Phases':
            b_phase = values['b_phase_menu']
        else:
            b_phase = values['b_phase_menu']



        # Refresh Top Graph

        if event=='Refresh Top Image':
            t_country=t_country.replace("[", "")
            t_country=t_country.replace("]", "")
            t_country=t_country.replace("'", "")
            print(t_country)
            if t_graph == "Line Graph" or t_graph == None:
                if t_country == 'All Countries' or t_country == None:
                        line_plot_all()  
                        window['top_graph'].Update(filename='output.png')
                else:                                
                        top_line()
                        window['top_graph'].Update(filename='output.png')
            
            else:
                if t_country == 'All Countries' or t_country == None:
                        bar_plot_all()  
                        window['top_graph'].Update(filename='output.png')
                else:                                
                        top_bar()
                        window['top_graph'].Update(filename='output.png')


        # Refresh Bottom Graph
        if event=='Refresh Bottom Image':
            if b_graph == "Bar Graph" or b_graph == None:
                if b_country == 'All Countries' or b_country == None:
                        bar_plot_all_bottom()  
                        window['bottom_graph'].Update(filename='output.png')
                else:                                
                        bottom_bar()
                        window['bottom_graph'].Update(filename='output.png')
            
            else: # Line Graph
                if t_country == 'All Countries' or t_country == None:
                        line_plot_all_bottom()  
                        window['bottom_graph'].Update(filename='output.png')
                else:                                
                        bottom_line()
                        window['bottom_graph'].Update(filename='output.png')

    window.close()


# All Graphs with Defaults

def line_plot_all():
    from GUI_main import GUI_run
    if (t_cause == 'All Causes' or t_cause == None):
        if(t_phase == 'All Phases' or t_phase == None):
            category = 'Year'
            numeric = 'Fatalities'

            df_all = df.groupby(category)[numeric].sum()

            df_all = {category: df_all.index,numeric: df_all.values}
            df_all = pd.DataFrame(df_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y, # which columns for x and y
                                data=df_all, # in which dataframe
                                ci=0, # no error bars (much faster!)
                                ) 


            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            ax.set(ylim=(0, 5000))

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide Fatalities by Year", fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png") 
        else:
            df_phase_all = df.loc[df['Phase'] == t_phase]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_phase_all = df_phase_all.groupby(category)[numeric].sum()

            df_phase_all = {category: df_phase_all.index,numeric: df_phase_all.values}
            df_phase_all = pd.DataFrame(df_phase_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_phase_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year during " + t_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
    else:
        if(t_phase == 'All Phases' or t_phase == None):
            df_cause_all = df.loc[df['Cause'] == t_cause]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_cause_all = df_cause_all.groupby(category)[numeric].sum()

            df_cause_all = {category: df_cause_all.index,numeric: df_cause_all.values}
            df_cause_all = pd.DataFrame(df_cause_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_cause_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year caused by " + t_cause, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
        else:
            df_cause_all = df.loc[df['Cause'] == t_cause]
            df_cause_phase_all = df_cause_all.loc[df_cause_all['Phase'] == t_phase]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_cause_phase_all = df_cause_phase_all.groupby(category)[numeric].sum()

            df_cause_phase_all = {category: df_cause_phase_all.index,numeric: df_cause_phase_all.values}
            df_cause_phase_all = pd.DataFrame(df_cause_phase_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_cause_phase_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year caused by " + t_cause + ' during ' + t_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")

def bar_plot_all():
    from GUI_main import GUI_run
    if (t_cause == 'All Causes' or t_cause == None):
        if(t_phase == 'All Phases' or t_phase == None):
            category = 'Year'
            numeric = 'Fatalities'

            df_all = df.groupby(category)[numeric].sum()

            df_all = {category: df_all.index,numeric: df_all.values}
            df_all = pd.DataFrame(df_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y, # which columns for x and y
                                data=df_all, # in which dataframe
                                ci=0, # no error bars (much faster!)
                                ) 


            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            ax.set(ylim=(0, 5000))

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide Fatalities by Year", fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png") 
        else:
            df_phase_all = df.loc[df['Phase'] == t_phase]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_phase_all = df_phase_all.groupby(category)[numeric].sum()

            df_phase_all = {category: df_phase_all.index,numeric: df_phase_all.values}
            df_phase_all = pd.DataFrame(df_phase_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_phase_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year during " + t_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
    else:
        if(t_phase == 'All Phases' or t_phase == None):
            df_cause_all = df.loc[df['Cause'] == t_cause]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_cause_all = df_cause_all.groupby(category)[numeric].sum()

            df_cause_all = {category: df_cause_all.index,numeric: df_cause_all.values}
            df_cause_all = pd.DataFrame(df_cause_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_cause_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year caused by " + t_cause, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
        else:
            df_cause_all = df.loc[df['Cause'] == t_cause]
            df_cause_phase_all = df_cause_all.loc[df_cause_all['Phase'] == t_phase]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_cause_phase_all = df_cause_phase_all.groupby(category)[numeric].sum()

            df_cause_phase_all = {category: df_cause_phase_all.index,numeric: df_cause_phase_all.values}
            df_cause_phase_all = pd.DataFrame(df_cause_phase_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_cause_phase_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year caused by " + t_cause + ' during ' + t_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")


# Top Graphs


def top_line():
    from GUI_main import GUI_run
    df_country = df.loc[df['Country'] == t_country]
    category = 'Year'
    numeric = 'Fatalities'
    if (t_cause == 'All Causes' or t_cause == None):
        if(t_phase == 'All Phases' or t_phase == None):
            t_line_country = df_country.groupby('Year')['Fatalities'].sum()
            category = 'Year'
            numeric = 'Fatalities'
            t_line_country = {category: t_line_country.index, numeric: t_line_country.values}
            t_line_country = pd.DataFrame(t_line_country)
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=t_line_country,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + t_country, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()

            fig.savefig("output.png")
        else:
            df_phase = df_country.loc[df_country['Phase'] == t_phase]
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_phase,
                            ci=0,
                            ) 
                    
            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + t_country + " during "  + t_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
    else:
        if(t_phase == 'All Phases' or t_phase == None):
            df_cause = df_country.loc[df_country['Cause'] == t_cause]
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_cause,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + t_country + " caused by "  + t_cause, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
        else:
            df_cause = df_country.loc[df_country['Cause'] == t_cause]
            df_phase_cause = df_cause.loc[df_cause['Phase'] == t_phase]

            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_phase_cause,
                            ci=0,
                            ) 


            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + t_country + " caused by "  + t_cause + " during "+ t_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")  

def top_bar():
    from GUI_main import GUI_run
    df_country = df.loc[df['Country'] == t_country]
    category = 'Year'
    numeric = 'Fatalities'
    if (t_cause == 'All Causes' or t_cause == None):
        if(t_phase == 'All Phases' or t_phase == None):
            t_line_country = df_country.groupby('Year')['Fatalities'].sum()
            category = 'Year'
            numeric = 'Fatalities'
            t_line_country = {category: t_line_country.index, numeric: t_line_country.values}
            t_line_country = pd.DataFrame(t_line_country)
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=t_line_country,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + t_country, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()

            fig.savefig("output.png")
        else:
            df_phase = df_country.loc[df_country['Phase'] == t_phase]
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_phase,
                            ci=0,
                            ) 
                    
            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + t_country + " during "  + t_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
    else:
        if(t_phase == 'All Phases' or t_phase == None):
            df_cause = df_country.loc[df_country['Cause'] == t_cause]
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_cause,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + t_country + " caused by "  + t_cause, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
        else:
            df_cause = df_country.loc[df_country['Cause'] == t_cause]
            df_phase_cause = df_cause.loc[df_cause['Phase'] == t_phase]

            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_phase_cause,
                            ci=0,
                            ) 


            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + t_country + " caused by "  + t_cause + " during "+ t_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")  



# Bottom Graphs


def line_plot_all_bottom():
    from GUI_main import GUI_run
    if (b_cause == 'All Causes' or b_cause == None):
        if(b_phase == 'All Phases' or b_phase == None):
            category = 'Year'
            numeric = 'Fatalities'

            df_all = df.groupby(category)[numeric].sum()

            df_all = {category: df_all.index,numeric: df_all.values}
            df_all = pd.DataFrame(df_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y, # which columns for x and y
                                data=df_all, # in which dataframe
                                ci=0, # no error bars (much faster!)
                                ) 


            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            ax.set(ylim=(0, 5000))

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide Fatalities by Year", fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png") 
        else:
            df_phase_all = df.loc[df['Phase'] == b_phase]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_phase_all = df_phase_all.groupby(category)[numeric].sum()

            df_phase_all = {category: df_phase_all.index,numeric: df_phase_all.values}
            df_phase_all = pd.DataFrame(df_phase_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_phase_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year during " + b_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
    else:
        if(b_phase == 'All Phases' or b_phase == None):
            df_cause_all = df.loc[df['Cause'] == b_cause]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_cause_all = df_cause_all.groupby(category)[numeric].sum()

            df_cause_all = {category: df_cause_all.index,numeric: df_cause_all.values}
            df_cause_all = pd.DataFrame(df_cause_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_cause_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year caused by " + b_cause, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
        else:
            df_cause_all = df.loc[df['Cause'] == b_cause]
            df_cause_phase_all = df_cause_all.loc[df_cause_all['Phase'] == b_phase]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_cause_phase_all = df_cause_phase_all.groupby(category)[numeric].sum()

            df_cause_phase_all = {category: df_cause_phase_all.index,numeric: df_cause_phase_all.values}
            df_cause_phase_all = pd.DataFrame(df_cause_phase_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_cause_phase_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year caused by " + b_cause + ' during ' + b_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")

def bar_plot_all_bottom():
    from GUI_main import GUI_run
    if (b_cause == 'All Causes' or b_cause == None):
        if(b_phase == 'All Phases' or b_phase == None):
            category = 'Year'
            numeric = 'Fatalities'

            df_all = df.groupby(category)[numeric].sum()

            df_all = {category: df_all.index,numeric: df_all.values}
            df_all = pd.DataFrame(df_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y, # which columns for x and y
                                data=df_all, # in which dataframe
                                ci=0, # no error bars (much faster!)
                                ) 


            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            ax.set(ylim=(0, 5000))

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide Fatalities by Year", fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png") 
        else:
            df_phase_all = df.loc[df['Phase'] == b_phase]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_phase_all = df_phase_all.groupby(category)[numeric].sum()

            df_phase_all = {category: df_phase_all.index,numeric: df_phase_all.values}
            df_phase_all = pd.DataFrame(df_phase_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_phase_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year during " + b_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
    else:
        if(b_phase == 'All Phases' or b_phase == None):
            df_cause_all = df.loc[df['Cause'] == b_cause]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_cause_all = df_cause_all.groupby(category)[numeric].sum()

            df_cause_all = {category: df_cause_all.index,numeric: df_cause_all.values}
            df_cause_all = pd.DataFrame(df_cause_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_cause_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year caused by " + b_cause, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
        else:
            df_cause_all = df.loc[df['Cause'] == b_cause]
            df_cause_phase_all = df_cause_all.loc[df_cause_all['Phase'] == b_phase]

            #Total Fatalities
            category = 'Year'
            numeric = 'Fatalities'

            df_cause_phase_all = df_cause_phase_all.groupby(category)[numeric].sum()

            df_cause_phase_all = {category: df_cause_phase_all.index,numeric: df_cause_phase_all.values}
            df_cause_phase_all = pd.DataFrame(df_cause_phase_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_cause_phase_all,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide fatalities by Year caused by " + b_cause + ' during ' + b_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")



def bottom_line():
    from GUI_main import GUI_run
    df_country = df.loc[df['Country'] == b_country]
    category = 'Year'
    numeric = 'Fatalities'
    if (b_cause == 'All Causes' or b_cause == None):
        if(b_phase == 'All Phases' or b_phase == None):
            b_line_country = df_country.groupby('Year')['Fatalities'].sum()
            category = 'Year'
            numeric = 'Fatalities'
            b_line_country = {category: b_line_country.index, numeric: b_line_country.values}
            b_line_country = pd.DataFrame(b_line_country)
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=b_line_country,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + b_country, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()

            fig.savefig("output.png")
        else:
            df_phase = df_country.loc[df_country['Phase'] == b_phase]
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_phase,
                            ci=0,
                            ) 
                    
            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + b_country + " during "  + b_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
    else:
        if(b_phase == 'All Phases' or b_phase == None):
            df_cause = df_country.loc[df_country['Cause'] == b_cause]
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_cause,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + b_country + " caused by "  + b_cause, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
        else:
            df_cause = df_country.loc[df_country['Cause'] == b_cause]
            df_phase_cause = df_cause.loc[df_cause['Phase'] == b_phase]

            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                            data=df_phase_cause,
                            ci=0,
                            ) 


            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=10)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + b_country + " caused by "  + b_cause + " during "+ b_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")  

def bottom_bar():
    from GUI_main import GUI_run
    df_country = df.loc[df['Country'] == b_country]
    category = 'Year'
    numeric = 'Fatalities'
    if (b_cause == 'All Causes' or b_cause == None):
        if(b_phase == 'All Phases' or b_phase == None):
            b_line_country = df_country.groupby('Year')['Fatalities'].sum()
            category = 'Year'
            numeric = 'Fatalities'
            b_line_country = {category: b_line_country.index, numeric: b_line_country.values}
            b_line_country = pd.DataFrame(b_line_country)
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=b_line_country,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + b_country, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()

            fig.savefig("output.png")
        else:
            df_phase = df_country.loc[df_country['Phase'] == b_phase]
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_phase,
                            ci=0,
                            ) 
                    
            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + b_country + " during "  + b_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
    else:
        if(b_phase == 'All Phases' or b_phase == None):
            df_cause = df_country.loc[df_country['Cause'] == b_cause]
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_cause,
                            ci=0,
                            ) 

            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + b_country + " caused by "  + b_cause, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")
        else:
            df_cause = df_country.loc[df_country['Cause'] == b_cause]
            df_phase_cause = df_cause.loc[df_cause['Phase'] == b_phase]

            fig, ax = plt.subplots(figsize=(13.5,3.5))  # new plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                            data=df_phase_cause,
                            ci=0,
                            ) 


            plt.xticks(rotation=90)
            ax.tick_params(axis='x', which='both', labelsize=8)

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=7)

            ax.set_title("Fatalities by Year for " + b_country + " caused by "  + b_cause + " during "+ b_phase, fontsize='18')
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)
            fig = ax.get_figure()
            fig.savefig("output.png")  



