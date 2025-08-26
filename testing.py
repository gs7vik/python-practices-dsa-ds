import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.choice([2,np.nan], (20, 5), p=[0.2, 0.8]), columns=list('abcde'))

print(df.loc['a'])