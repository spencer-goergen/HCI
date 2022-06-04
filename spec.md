# Plane Crashes Light Project Spec 

 ## General Description

- This will show a user plane crashes around the world since 1918. There is a variety of data points, including what phase the flight was in when it crashed, the crash site, and the country operating the plane. For example, the user may compare data from all the flights that crashed in their takeoff phase between Canada, United States, and Mexico.
- App shows a simple line graph between the years 1918 to 2022, with a y-axis of number of crashes.
- The user should be able to filter/refine settings between the variety of columns.

External:
- Data is found at https://www.kaggle.com/datasets/abeperez/historical-plane-crash-data and saved locally in the application.
- GUI: Webpage style app. I am unsure what module/API would help me accomplish this at this time.
- APIs: Pandas, NumPy, Matplotlib, Seaborn. (One or multiple of these, probably!)


Possible enhancements:
- Data could also be visualized using GeoPandas on a world map.
- Could change the dates to select a specific time frame.
- There could be interactions by the user by selecting specific "points" on the graph to get a summary of the specific crash(es).
- Could include zooming.

## Task Vignettes

Sketch (example, created in Photoshop):

![Sketch2](https://user-images.githubusercontent.com/106708967/172018147-d56804a9-4c11-4d2f-9eaa-1bd1a65603ea.jpg)

Task 1: Filter by countries

   * defaults/previous filters automatically loaded
   * User configurable fields:
     * countries selected: (Countries)

Task 1 User activity:

   * user starts webapp, fetches and shows the countries and data points selected as per defaults
   * user selects the drop-down to filter by country
   * user selects/deselects whichever countries they would like
   * user hits Refresh, and the webapp reflects the new filters.

Task 2: Filter by crash cause

   * defaults/previous filters automatically loaded
   * User configurable fields:
     * crash cause: Technical Failure, Weather, Human Error, Terrorism, Unknown

Task 2 user activity:

   * user starts webapp, fetches and shows the countries and data points selected as per defaults
   * user selects the drop-down to filter by crash cause
   * user selects/deselects whichever crash causes they would like
   * user hits Refresh, and the webapp reflects the new filters.

Tasks 3-X:

   * Identicaly to Task 1, Task 2
   * Filters possible:
     * Flight phase, Operator, Crash site, Crash locationm, Fatalities, Survivors


## Technical Flow


Data structures: 
    - pandas dataframe, each containing data about each quake (date, lat/long location, magnitude) that's been scarped from the USGS
    - a dict or object that stores all the current values for all application form fields: data range, magnitude range, radius, num_quakes, toggle, etc. 
    - default values for these could be hard coded or read from a config.txt file
    - dict/object with any other values the application needs, that are NOT user configurable, e.g. the current location, which is provided at startup from the geolocation function, a scale factor for the markers, geometry/color or the markers, etc.


Core functions:
- def get_location():
    - uses geolocation to approximate current browser geolocation 
    - not sure yet if/how user concent is needed?
    - returns geolocation (lat/long) or error string (hardcode Chicago as backup location on fail)

- def get_quake_data(date_range, magnitude_range, number_of_largest_quakes, radius):
    - scrapes data from the USGS according to arguments
    - if number_of_largest_quakes is None, magnitude range is used
    - should still be limited to ~100 quakes to ensure a responsive map (in which case they should be sorted by magnitude!)
    - returns a pandas dataframe or error string

- def draw_map(folium_map, dataframe, config_dict):
    - draws markers from the dataframe into a folium map
    - config_dict has stuff like scale factor, marker geometry and color, etc.
    - needs to also update the map legend


Program flow:
- Flask app main page creates the GUI, gets geolocation and renders the folium map for this location with current GUI defaults using the dataframe
- (GUI could be vanilla Javascript or maybe Bootstrap ...)
- changes in GUI fields are collected in a HTML form and sent back to the server
- scrapes a new dataframe according to user values, clears folium map and re-draws it from new dataframe











