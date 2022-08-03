# Modules

- Python v3.6 or newer
  - pip3 install pysimplegui
  - pip3 install pandas
  - pip3 install Matplotlib
  - pip3 install seaborn

# run.py

- Imports GUI_main
- Runs GUI_run()

This ensures that there is only one instance of GUI_run()

# GUI_main.py

Rest of program

## Main

- Import Modules
- create default dataframe 'df' from Dataset.csv
  - via Pandas pd.read_csv()
- create menus via lists for GUI
- Select default graphs from /images
  - os.chdir to images, assign variables, move up
- Assign default variables


## GUI Layout

3 Columns are in the layout

Column1:
- sg.Text is used for Title
- sg.Combo is used for drop-down menu
- sg.Button is used for Refresh buttons
- sg.Text(' ') is used for spacing

Column2:
- sg.pin(sg.Image())
  - sg.Image is the graphs that are displayed
  - sg.pin is added to allow for changing the graph image via the key='Variable'

Column3:
- sg.Button("Exit") exits the application
- sg.Text(' ') is used for spacing

Layout:
- sg.Column houses the columns
- sg.VSeperator() adds a line vector to seperate Column1 and Column2


## GUI_run()

### Main
- os.chdir('images') move back to images
- sg.Window creates window with title and layout assigned above

### while True:

How program takes inputs and re-directs to graph creating function

- plt.style.use() assigns style of graphs
- gloabl variables are brought in
- events, values = window.read() reads values from window
- Exit on clicking "exit"

if values['t_graph_menu'] == "Line Graph":
   t_graph = values['t_graph_menu']
else:
   t_graph = values['t_graph_menu']

- This if/else checks for what option is selected from the menu drop down and displays that option in the window


if event=='Refresh Top Image':  

- This event checks when the Refresh button is selected, and then re-directs to the appropriate function
- t_graph == 'Line Graph' or t_graph == None
  - t_graph default is Line Graph, but before selected reads out 'None', so this accounts for both
  - window['top_graph'].Update(filename='output.png') is replacing the graph image from the function that just ran

### Graph Functions

Top Graph Functions
- def line_plot_all_top():
- def bar_plot_all_top():
- def top_line():
- def top_bar():

Bottom Graph Functions
- def line_plot_all_bottom():
- def bar_plot_all_bottom():
- def bottom_line():
- def bottom_bar():

Difference between line_plot_all_top() and top_line()
- '_all_' function is not limiting by country, '_line()' function does

Difference between top_bar() and top_line()
- ax = sns.lineplot
- ax = sns.barplot

Outside of these differences, the functions are nearly identical.
Only def top_line() will be commented on here. (in code, line_plot_all_top() has comments).

### def top_line()

#### Main

- GUI_run is imported
- df_country = df.loc[df['Country'] == t_country]
  - df.loc is limiting the dataframe by a specific [Column == element]
- if/else statemnts for Cause and Phase
  - This creates a graph based on the user's inputs from the GUI
- df_country.groupby('Year')['Fatalities'].sum()
  - This is summing up all fatalites by year from the dataframe
- {category: t_line_country.index, numeric: t_line_country.values}
  - Creating index and values from dataframe
  - pd.Dataframe() creates new dataframe

#### Creating Graph

- fig, ax = plt.subplots() creates figure and its size
- category, x = 'Year'; numeric, y = 'Fatalities
- ax = sns.lineplot() using dataframe and ci=0 for no error bars

- plt.xticks, yticks these are the years (1942,1943,1943) and fatatalites (0-5000)
- ax.tick_params sets the size and axis
- ax.set_title is the Title of graph
- ax.set_x/ylabel is the labels on axises
- plt.subplots_adjust(bottom=0.15) creates room for clearance at the bottom of the graph

- fig = ax.get_figure() retrieves graph
- fig.savefig("output.png") saves graph
- fig.clear() clears cache
