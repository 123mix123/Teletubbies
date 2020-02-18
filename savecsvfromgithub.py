import pandas as pd
import csv
url="https://raw.githubusercontent.com/123mix123/Mixchanawee/master/videouploadedin2m.csv"
df = pd.read_csv(url,error_bad_lines=False)
df.to_csv('urlcsv'+'.csv',line_terminator="\n",index=False)
