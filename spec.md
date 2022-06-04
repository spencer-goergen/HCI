# Example of a light planning spec for my sketch

 ## General Description

This will show a user plane crashes around the world since 1918. There is a variety of data points, including what phase the flight was in when it crashed, the crash site, and the country operating the plane. For example, the user may compare data from all the flights that crashed in their takeoff phase between Canada, United States, and Mexico.
App shows a simple line graph between the years 1918 to 2022, with a y-axis of number of crashes.
The user should be able to filter/refine settings between the variety of columns.

External:
Data is found at https://www.kaggle.com/datasets/abeperez/historical-plane-crash-data and saved locally in the application.
GUI: Webpage style app. I am unsure what module/API would help me accomplish this at this time.
APIs: Pandas, NumPy, Matplotlib, Seaborn. (One or multiple of these, probably!)


Possible enhancements:
Data could also be visualized using GeoPandas on a world map.
Could change the dates to select a specific time frame.
There could be interactions by the user by selecting specific "points" on the graph to get a summary of the specific crash(es).
Could include zooming.

## Task Vignettes

Task 1: Filter by date and magnitude ranges

location will be given automatically
User configurable fields:
date range: default 1900 to current, only uses years!
magnitude range: defaults to 7 to 9.5
radius: 10 miles
Task 1 user activity:

user starts app, fetches and shows quakes as per defaults
user enters start (1950) and end (2022) years (Validate GUI: start < end!)
user enters magnitude high (9.5) and low (7.2) (Validate: high > low)
user enters radius: 50 miles
user leaves num_quakes toggle off, num_quakes is greyed out
user hits Refresh Map, which connects to the USGS (show spinner while processing) and changes the map markers and radius accordingly and updates the map legend to show which size corresponds
Task 2: Filter by date range and X largest magnitude quakes

location will be given automatically
User configurable fields:
date range: default 1900 to current, only uses years!
radius: 10 miles
show number of X largest quakes number field (10), initally toggled off

Task 2 user activity:

   * user starts app, fetches and shows quakes as per defaults
   * user enters start (1950) and end (2022) years (Validate GUI: start < end!)
   * skips magnitude selection
   * user enters radius: 50 miles
   * user switched num_quakes toggle oon, num_quakes is now active (default: 10 largest quakes) and magnitude is inactive
   * user enters num_quakes: 25
   * user hits Refresh Map, which connects to the USGS (show spinner while processing) and changes the map markers and radius accordingly and updates the   map legend to show which size corresponds

Diagram:


