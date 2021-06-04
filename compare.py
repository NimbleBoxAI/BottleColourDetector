import pickle
import pandas as pd

medians = pickle.load(open('median_center.pkl','rb'))

df = pd.DataFrame.from_dict(medians, orient='index').transpose()

df.to_excel('median_color_signatures.xlsx')

print('Comparison exported.')