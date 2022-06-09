## Start of Program

#Import APIs
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Style of Plots
plt.style.use('fivethirtyeight')

#Read files
df = pd.read_csv("Plane Crash dataset.csv")

#Convert specific columns from objects to strings
df = df.astype({'Country':'string'})
df = df.astype({'Aircraft':'string'})
df = df.astype({'Crash cause':'string'})

## Display first 3 rows + data points (DEBUG)

#display(df.head(3))  # head(10) top 10 rows only, display: fancy jupyer print()
#display(df.dtypes)

print('Success.')



##          Deaths by Crash Cause       ##

#Split fig from ax (don't fully understand)
fig, ax = plt.subplots()

# Bar Chart Creation

# (Grab crash cause and total fatalities from file)
bars = ax.bar(df['Crash cause'], df['Total fatalities'], xerr=0, align='center')

# Set x,y ticks; rotate xticks, make title
# ax.set_xlabel('Crash Cause') ## (Not needed)
plt.xticks(rotation=90)
ax.set_title('Deaths by Cause')

# Show plot
plt.show()




##          Deaths by Crash Cause       ##

#Split fig from ax (don't fully understand)

# Bar Chart Creation

# (Grab crash cause and total fatalities from file)
bars = ax.bar(df['Country'], df['Total fatalities'], xerr=0, align='center')

# Set x,y ticks; rotate xticks, make title
# ax.set_xlabel('Crash Cause') ## (Not needed)
plt.xticks(rotation=90)
ax.set_title('Deaths by Cause')

# Show plot
plt.show()
