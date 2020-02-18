import pandas as pd
import csv
url="https://github.com/123mix123/Mixchanawee/blob/master/videouploadedin2m.csv"
df = pd.read_csv(url,error_bad_lines=False)
df.to_csv('urlcsv'+'.csv',line_terminator="\n",index=False)
