## Modules

- Python v3.6 or newer
  - pip3 install pysimplegui
  - pip3 install pandas
  - pip3 install Matplotlib
  - pip3 install seaborn

## run.py

- Imports GUI_main
- Runs GUI_run()

This ensures that there is only one instance of GUI_run()

## GUI_main

Rest of program

### Main

- Import Modules
- create default dataframe 'df' from Dataset.csv
  - via Pandas pd.read_csv()
- create menus via lists for GUI
- Select default graphs from /images
  - os.chdir to images, assign variables, move up
- Assign default variables


### GUI Layout

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












