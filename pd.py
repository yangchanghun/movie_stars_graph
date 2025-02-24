import pandas as pd

data = pd.read_csv('은평구스터디카페.csv')

data.groupby(data['lcation'])
print(data.groupby(data['lcation']).count())
