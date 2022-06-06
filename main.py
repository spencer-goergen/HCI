#import Plane Crash file
import pandas as pd
df = pd.read_csv("Plane Crash dataset.csv")

display(df.head(10))  #top 10 rows only

df = df.astype({'Country':'str'})
display(df.dtypes)  #show data types of columns

# line plot
df.plot.line(x='Year', y='Total fatalities');

