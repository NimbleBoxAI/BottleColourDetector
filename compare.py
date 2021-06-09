import pickle
import pandas as pd

pickle_data = pickle.load(open('clustered.pkl','rb'))

df = pd.DataFrame.from_dict(pickle_data, orient='index').transpose()

df.to_excel('clusters.xlsx')

print('Comparison exported.')