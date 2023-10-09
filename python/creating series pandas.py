 #Creating a series based on data and index positions

import pandas as pd

days = [31, 28, 31, 30]
months = ['Jan', 'Feb', 'Mar', 'Apr']
s1 = pd.Series(data=days, index=months)
s2 = pd.Series(data=months, index=days)
print(s1)
print(s2)