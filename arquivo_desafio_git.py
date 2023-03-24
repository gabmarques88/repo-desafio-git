print('hello world')
import pandas as pd

df = pd.DataFrame({
    'nome':['João', 'José', 'Maria'],
    'idade': [33, 45, 60]
})

print(df)
df.describe()
df.shape