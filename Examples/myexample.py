import pandas as pd
import numpy as np 

mat = np.arange(0,20).reshape(10,2)

df = pd.DataFrame(data=mat, columns=['A','B'])
print(df)


