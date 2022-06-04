# Plane Crashes Light Project Spec 

 ## General Description

This will show a user plane crashes around the world since 1918. There is a variety of data points, including what phase the flight was in when it crashed, the crash site, and the country operating the plane. For example, the user may compare data from all the flights that crashed in their takeoff phase between Canada, United States, and Mexico.
App shows a simple line graph between the years 1918 to 2022, with a y-axis of number of crashes.
The user should be able to filter/refine settings between the variety of columns.

External: /n
Data is found at https://www.kaggle.com/datasets/abeperez/historical-plane-crash-data and saved locally in the application.
GUI: Webpage style app. I am unsure what module/API would help me accomplish this at this time.
APIs: Pandas, NumPy, Matplotlib, Seaborn. (One or multiple of these, probably!)


Possible enhancements:
Data could also be visualized using GeoPandas on a world map.
Could change the dates to select a specific time frame.
There could be interactions by the user by selecting specific "points" on the graph to get a summary of the specific crash(es).
Could include zooming.

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











