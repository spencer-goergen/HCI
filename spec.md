# Example of a light planning spec for my sketch

 <font size="5"> General Description </font>

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


