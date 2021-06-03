import pickle
import pandas as pd

medians_center = pickle.load(open('median_center.pkl','rb'))
medians_whole = pickle.load(open('median_whole.pkl','rb'))

df = pd.DataFrame((medians_center, medians_whole))
df = df.transpose()
print(df.head())
