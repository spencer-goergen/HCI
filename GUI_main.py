import PySimpleGUI as sg            # For GUI
import pandas as pd                 # For DataFrames
import matplotlib.pyplot as plt     # For Graphs
import seaborn as sns               # For Graphs
import os                           # For directory movement

# Default Dataframe
df = pd.read_csv("Dataset.csv") 

# Menus for GUI
button_menu_def_graph = ['Line Graph', 'Bar Graph']
button_menu_def_country = ['All Countries', 'United States of America', 'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Ecuador', 'Egypt', 'El Salvador', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Krygyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Madagascar', 'Malaysia', 'Maldives', 'Mali', 'Mexico', 'Moldova', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Singapore', 'Slovakia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
button_menu_def_cause = ['All Causes', 'Technical failure', 'Terrorism', 'Weather', 'Human factor', 'Other']
button_menu_def_phase = ['All Phases', 'Flight', 'Landing', 'Parking', 'Takeoff','Taxiing']

# Default Graphs in images
os.chdir('images')
default_line = 'top_default.png'
default_bar = 'bottom_default.png'
os.chdir('../')

# Default Top Variables
t_graph = 'Line Graph'
t_country = 'All Countries'
t_cause = 'All Causes'
t_phase = 'All Phases'

# Default sBottom Variables
b_graph = 'Bar Graph'
b_country = 'All Countries'
b_cause = 'All Causes'
b_phase = 'All Phases'

## GUI Layout

# Column1 has Title, Dropdowns, and Refresh buttons
column1 = [
        [sg.Text("Plane Crashes", font = ('Calibri 24 bold'))],
        [sg.Text("from 1918-2022", font = ('Calibri 24 bold'))],
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Combo((button_menu_def_graph),font = ('Calibri 11'),readonly = True, size = (24,2),  expand_y = True, default_value='Line Graph', key='t_graph_menu')],
        [sg.Combo((button_menu_def_country),font = ('Calibri 11'), readonly = True, size = (24,6), expand_y = True, default_value='All Countries', key='t_country_menu')],
        [sg.Combo((button_menu_def_cause),font = ('Calibri 11'), readonly = True, size = (24,10), expand_y = True, default_value='All Causes', key='t_cause_menu')],
        [sg.Combo((button_menu_def_phase),font = ('Calibri 11'), readonly = True, size = (24,10), expand_y = True, default_value='All Phases', key='t_phase_menu')],
        [sg.Button(('Refresh Top Image'), font = ('Calibri 12'))],
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Combo((button_menu_def_graph),font = ('Calibri 11'), readonly = True, size = (24,2), expand_y = True, default_value='Bar Graph', key='b_graph_menu')],
        [sg.Combo((button_menu_def_country),font = ('Calibri 11'), readonly = True, size = (24,6), expand_y = True, default_value='All Countries', key='b_country_menu')],
        [sg.Combo((button_menu_def_cause),font = ('Calibri 11'), readonly = True, size = (24,10), expand_y = True, default_value='All Causes', key='b_cause_menu')],
        [sg.Combo((button_menu_def_phase),font = ('Calibri 11'), readonly = True, size = (24,10), expand_y = True, default_value='All Phases', key='b_phase_menu')],
        [sg.Button(('Refresh Bottom Image'), font = ('Calibri 12'))],
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')], #Space between outputs
        [sg.Text(' ')] #Space between outputs
    ]

# Column2 has Graphs
column2 = [
        [sg.pin(sg.Image(filename=default_line, key='top_graph'))], 
        [sg.pin(sg.Image(filename=default_bar, key='bottom_graph'))]
    ]

# Column3 has Exit button
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

# Layout puts Columns1-3 together
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

    # Title of Window
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

        # Reads values of selections
        event, values = window.read()

        # Close on Exit
        if event in (sg.WIN_CLOSED, 'Exit'):
                break

        # Top Graph -- Update Type on Click
        
        if values['t_graph_menu'] == "Line Graph":
            t_graph = values['t_graph_menu']
        else:
            t_graph = values['t_graph_menu']
        
        # Top Graph -- Update Country on Click 

        if values['t_country_menu'] == "All Countries":
            t_country = values['t_country_menu']
        else:
            t_country = values['t_country_menu']

        # Top Graph -- Update Cause on Click 

        if values['t_cause_menu'] != 'All Causes':
            t_cause = values['t_cause_menu']
        else:
            t_cause = values['t_cause_menu']

        # Top Graph -- Update Phase on Click 

        if values['t_phase_menu'] != 'All Phases':
            t_phase = values['t_phase_menu']
        else:
            t_phase = values['t_phase_menu']

        # Bottom Graph -- Update Type on Click 

        if values['b_graph_menu'] == "Line Graph":
            b_graph = values['b_graph_menu']
        else:
            b_graph = values['b_graph_menu']

        # Bottom Graph -- Update Country on Click

        if values['b_country_menu'] != "All Countries":
            b_country = values['b_country_menu']
        else:
            b_country = values['b_country_menu']

        # Bottom Graph -- Update Cause on Click

        if values['b_cause_menu'] != 'All Causes':
            b_cause = values['b_cause_menu']
        else:
            b_cause = values['b_cause_menu']

        # Bottom Graph -- Update Phase on Click

        if values['b_phase_menu'] != 'All Phases':
            b_phase = values['b_phase_menu']
        else:
            b_phase = values['b_phase_menu']

        # On "Refresh Top Graph" Click

        if event=='Refresh Top Image':          # 'None' is when no item has been clicked yet (i.e. Default)
            if t_graph == "Line Graph" or t_graph == None:             
                if t_country == 'All Countries' or t_country == None:
                        line_plot_all_top()                                 # All countries for line graph
                        window['top_graph'].Update(filename='output.png')
                else:                                
                        top_line()                                          # Specific country for line graph
                        window['top_graph'].Update(filename='output.png')
            
            else: # Bar Graph
                if t_country == 'All Countries' or t_country == None:
                        bar_plot_all_top()                                  # All countries for bar graph
                        window['top_graph'].Update(filename='output.png')
                else:                                
                        top_bar()                                           # Specific country for bar graph
                        window['top_graph'].Update(filename='output.png')


        # Refresh Bottom Graph (Same notes from "Refresh Top Graphs")

        if event=='Refresh Bottom Image':
            if b_graph == "Bar Graph" or b_graph == None:
                if b_country == 'All Countries' or b_country == None:
                        bar_plot_all_bottom()  
                        window['bottom_graph'].Update(filename='output.png')
                else:                                
                        bottom_bar()
                        window['bottom_graph'].Update(filename='output.png')
            
            else: # Line Graph
                if b_country == 'All Countries' or b_country == None:
                        line_plot_all_bottom()  
                        window['bottom_graph'].Update(filename='output.png')
                else:                                
                        bottom_line()
                        window['bottom_graph'].Update(filename='output.png')

    window.close()

## Top Graph Functions
# line_plot_all_top() has notes

def line_plot_all_top():
    from GUI_main import GUI_run
    if (t_cause == 'All Causes' or t_cause == None):
        if(t_phase == 'All Phases' or t_phase == None):
            # All countries, all causes, all phases
            category = 'Year'
            numeric = 'Fatalities'

            df_all = df.groupby(category)[numeric].sum()

            df_all = {category: df_all.index,numeric: df_all.values}
            df_all = pd.DataFrame(df_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))              # Create plot
            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y, 
                                data=df_all,
                                ci=0,
                                ) 

            plt.xticks(rotation=90)                                 # Axis tick marks
            ax.tick_params(axis='x', which='both', labelsize=8)     

            ax.set(ylim=(0, 5000))                                  # 0-5000 Fatalities Y axis

            plt.xticks(fontsize=10)                                 # Size of Ticks
            plt.yticks(fontsize=7)

            ax.set_title("Worldwide Fatalities by Year", fontsize='18')     # Title, Y label, X Label
            ax.set_ylabel(ax.get_ylabel(), fontsize='14')                   
            ax.set_xlabel(" ", fontsize='1')

            plt.subplots_adjust(bottom=0.15)                        # Clearance on bottom

            fig = ax.get_figure()                                   # Save figure
            fig.savefig("output.png")
            fig.clear()
        else:
            # All countries, all causes, specific 
            df_phase_all = df.loc[df['Phase'] == t_phase]                          # Limit by phase

            category = 'Year'
            numeric = 'Fatalities'

            df_phase_all = df_phase_all.groupby(category)[numeric].sum()

            df_phase_all = {category: df_phase_all.index,numeric: df_phase_all.values}
            df_phase_all = pd.DataFrame(df_phase_all)
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()
    else:
        if(t_phase == 'All Phases' or t_phase == None):
            # All countries, specific causes, all phases
            df_cause_all = df.loc[df['Cause'] == t_cause]   # Limit by Cause

            category = 'Year'
            numeric = 'Fatalities'

            df_cause_all = df_cause_all.groupby(category)[numeric].sum()

            df_cause_all = {category: df_cause_all.index,numeric: df_cause_all.values}
            df_cause_all = pd.DataFrame(df_cause_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()
        else:
            # All countries, specific causes, specific phases
            df_cause_all = df.loc[df['Cause'] == t_cause]                               # Limit by Cause
            df_cause_phase_all = df_cause_all.loc[df_cause_all['Phase'] == t_phase]     # Limit by Phase

            category = 'Year'
            numeric = 'Fatalities'

            df_cause_phase_all = df_cause_phase_all.groupby(category)[numeric].sum()

            df_cause_phase_all = {category: df_cause_phase_all.index,numeric: df_cause_phase_all.values}
            df_cause_phase_all = pd.DataFrame(df_cause_phase_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()

def bar_plot_all_top():
    from GUI_main import GUI_run
    if (t_cause == 'All Causes' or t_cause == None):
        if(t_phase == 'All Phases' or t_phase == None):
            category = 'Year'
            numeric = 'Fatalities'

            df_all = df.groupby(category)[numeric].sum()

            df_all = {category: df_all.index,numeric: df_all.values}
            df_all = pd.DataFrame(df_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))
            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                                data=df_all,
                                ci=0,
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
            fig.clear()
        else:
            df_phase_all = df.loc[df['Phase'] == t_phase]

            category = 'Year'
            numeric = 'Fatalities'

            df_phase_all = df_phase_all.groupby(category)[numeric].sum()

            df_phase_all = {category: df_phase_all.index,numeric: df_phase_all.values}
            df_phase_all = pd.DataFrame(df_phase_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()
    else:
        if(t_phase == 'All Phases' or t_phase == None):
            df_cause_all = df.loc[df['Cause'] == t_cause]

            category = 'Year'
            numeric = 'Fatalities'

            df_cause_all = df_cause_all.groupby(category)[numeric].sum()

            df_cause_all = {category: df_cause_all.index,numeric: df_cause_all.values}
            df_cause_all = pd.DataFrame(df_cause_all)

 
            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()
        else:
            df_cause_all = df.loc[df['Cause'] == t_cause]
            df_cause_phase_all = df_cause_all.loc[df_cause_all['Phase'] == t_phase]

            category = 'Year'
            numeric = 'Fatalities'

            df_cause_phase_all = df_cause_phase_all.groupby(category)[numeric].sum()

            df_cause_phase_all = {category: df_cause_phase_all.index,numeric: df_cause_phase_all.values}
            df_cause_phase_all = pd.DataFrame(df_cause_phase_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()

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

            fig, ax = plt.subplots(figsize=(13.5,3.5))

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
            fig.clear()
        else:
            df_phase = df_country.loc[df_country['Phase'] == t_phase]
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()
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
            fig.clear()
        else:
            df_cause = df_country.loc[df_country['Cause'] == t_cause]
            df_phase_cause = df_cause.loc[df_cause['Phase'] == t_phase]

            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear() 

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

            fig, ax = plt.subplots(figsize=(13.5,3.5))

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
            fig.clear()
        else:
            df_phase = df_country.loc[df_country['Phase'] == t_phase]
            if df_phase.empty == True:
                sg.Popup('No phase detected for this country. Try again.', font = ('Calibri 11'), keep_on_top=True)
            else:
                fig, ax = plt.subplots(figsize=(13.5,3.5))
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
                fig.clear()
    else:
        if(t_phase == 'All Phases' or t_phase == None):
            df_cause = df_country.loc[df_country['Cause'] == t_cause]        
            if df_cause.empty == True:
                sg.Popup('No cause detected for this country. Try again.',font = ('Calibri 11'), keep_on_top=True)
            else:
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
                fig.clear()
        else:
            df_cause = df_country.loc[df_country['Cause'] == t_cause]
            df_phase_cause = df_cause.loc[df_cause['Phase'] == t_phase]
            if df_phase_cause.empty == True:
                sg.Popup('No phase and cause detected for this country. Try again.', font = ('Calibri 11'), keep_on_top=True)
            else:
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
                fig.clear()

## Bottom Graphs Functions

def line_plot_all_bottom():
    from GUI_main import GUI_run
    if (b_cause == 'All Causes' or b_cause == None):
        if(b_phase == 'All Phases' or b_phase == None):
            category = 'Year'
            numeric = 'Fatalities'

            df_all_bottom = df.groupby(category)[numeric].sum()

            df_all_bottom = {category: df_all_bottom.index,numeric: df_all_bottom.values}
            df_all_bottom = pd.DataFrame(df_all_bottom)

            fig, ax = plt.subplots(figsize=(13.5,3.5))

            x = 'Year'
            y = 'Fatalities'

            ax = sns.lineplot(x=x, y=y,
                                data=df_all_bottom,
                                ci=0,
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
            fig.clear()
        else:
            df_phase_all = df.loc[df['Phase'] == b_phase]

            category = 'Year'
            numeric = 'Fatalities'

            df_phase_all = df_phase_all.groupby(category)[numeric].sum()

            df_phase_all = {category: df_phase_all.index,numeric: df_phase_all.values}
            df_phase_all = pd.DataFrame(df_phase_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))

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
            fig.clear()
    else:
        if(b_phase == 'All Phases' or b_phase == None):
            df_cause_all = df.loc[df['Cause'] == b_cause]

            category = 'Year'
            numeric = 'Fatalities'

            df_cause_all = df_cause_all.groupby(category)[numeric].sum()

            df_cause_all = {category: df_cause_all.index,numeric: df_cause_all.values}
            df_cause_all = pd.DataFrame(df_cause_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))

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
            fig.clear()
        else:
            df_cause_all = df.loc[df['Cause'] == b_cause]
            df_cause_phase_all = df_cause_all.loc[df_cause_all['Phase'] == b_phase]

            category = 'Year'
            numeric = 'Fatalities'

            df_cause_phase_all = df_cause_phase_all.groupby(category)[numeric].sum()

            df_cause_phase_all = {category: df_cause_phase_all.index,numeric: df_cause_phase_all.values}
            df_cause_phase_all = pd.DataFrame(df_cause_phase_all)
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()

def bar_plot_all_bottom():
    from GUI_main import GUI_run
    if (b_cause == 'All Causes' or b_cause == None):
        if(b_phase == 'All Phases' or b_phase == None):
            category = 'Year'
            numeric = 'Fatalities'

            df_all = df.groupby(category)[numeric].sum()

            df_all = {category: df_all.index,numeric: df_all.values}
            df_all = pd.DataFrame(df_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))

            x = 'Year'
            y = 'Fatalities'

            ax = sns.barplot(x=x, y=y,
                                data=df_all,
                                ci=0,
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
            fig.clear()
        else:
            df_phase_all = df.loc[df['Phase'] == b_phase]

            category = 'Year'
            numeric = 'Fatalities'

            df_phase_all = df_phase_all.groupby(category)[numeric].sum()

            df_phase_all = {category: df_phase_all.index,numeric: df_phase_all.values}
            df_phase_all = pd.DataFrame(df_phase_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()
    else:
        if(b_phase == 'All Phases' or b_phase == None):
            df_cause_all = df.loc[df['Cause'] == b_cause]

            category = 'Year'
            numeric = 'Fatalities'

            df_cause_all = df_cause_all.groupby(category)[numeric].sum()

            df_cause_all = {category: df_cause_all.index,numeric: df_cause_all.values}
            df_cause_all = pd.DataFrame(df_cause_all)

            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()
        else:
            df_cause_all = df.loc[df['Cause'] == b_cause]
            df_cause_phase_all = df_cause_all.loc[df_cause_all['Phase'] == b_phase]

            category = 'Year'
            numeric = 'Fatalities'

            df_cause_phase_all = df_cause_phase_all.groupby(category)[numeric].sum()

            df_cause_phase_all = {category: df_cause_phase_all.index,numeric: df_cause_phase_all.values}
            df_cause_phase_all = pd.DataFrame(df_cause_phase_all)
 
            fig, ax = plt.subplots(figsize=(13.5,3.5))
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
            fig.clear()

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

            fig, ax = plt.subplots(figsize=(13.5,3.5))
        
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
            fig.clear()
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
            fig.clear()
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
            fig.clear()
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
            fig.clear()  

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

            fig, ax = plt.subplots(figsize=(13.5,3.5))

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
            fig.clear()
        else:
            df_phase = df_country.loc[df_country['Phase'] == b_phase]
            if df_phase.empty == True:
                sg.Popup('No phase detected for this country. Try again',font = ('Calibri 11'),  keep_on_top=True)
            else:
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
                fig.clear()
    else:
        if(b_phase == 'All Phases' or b_phase == None):
            df_cause = df_country.loc[df_country['Cause'] == b_cause]
            if df_cause.empty == True:
                sg.Popup('No cause detected for this country. Try again',font = ('Calibri 11'),  keep_on_top=True)
            else:
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
                fig.clear()
        else:
            df_cause = df_country.loc[df_country['Cause'] == b_cause]
            df_phase_cause = df_cause.loc[df_cause['Phase'] == b_phase]
            if df_phase_cause.empty == True:
                sg.Popup('No cause or phase detected for this country. Try again',font = ('Calibri 11'),  keep_on_top=True)
            else:
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
                fig.clear()
