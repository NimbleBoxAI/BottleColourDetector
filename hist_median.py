import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.image as mpimg
import pickle
import os
from PIL import Image

def median(data_path, out_path, batch=False, region='center', region_offset=50):

	if batch is False:
		image = mpimg.imread(data_path)
		image = np.array(Image.fromarray(image).resize((100,120)))[20:]
		plt.imshow(image)
		plt.show()

		if region == 'whole':
			selection = image
		elif region == 'center':
			center = [image.shape[0]//2, image.shape[1]//2]
			selection = image[center[0] - region_offset : center[0] + region_offset, 
							  center[1] - region_offset : center[1] + region_offset]

		plt.imshow(selection)
		plt.show()

		r_median = np.median(selection[:,:,0])
		g_median = np.median(selection[:,:,1])
		b_median = np.median(selection[:,:,2])
		
		return (r_median,g_median,b_median)

	else:
		median_values = {}

		with os.scandir(data_path) as labels:
			for label in labels:

				if os.path.isdir(label):
					item_path = data_path + label.name + '/'
					median_label = []

					with os.scandir(item_path) as items:

						for item in items:

							image = mpimg.imread(f'{item_path}{item.name}')
							image = np.array(Image.fromarray(image).resize((100,120)))[20:]

					
							if region == 'whole':
								selection = image
							elif region == 'center':
								center = [image.shape[0]//2, image.shape[1]//2]
								selection = image[center[0] - region_offset : center[0] + region_offset, 
												  center[1] - region_offset : center[1] + region_offset]


							r_median = np.median(selection[:,:,0])
							g_median = np.median(selection[:,:,1])
							b_median = np.median(selection[:,:,2])

							median_label.append((r_median,g_median,b_median))
					
					median_values[label.name] = median_label

		f = open(out_path,'wb')
		pickle.dump(median_values, f)
		f.close()

		return True

if __name__=='__main__':

	# These parameters can be accepted as arguments
	data_path_single = './pics/data/blue/blue7.jpg'
	data_path = './pics/data/'
	out_path = 'median_center.pkl'
	batch = True
	region = 'center'
	region_offset = 20

	if batch is False:
		medians = median(data_path=data_path_single,
							out_path=out_path, 
							batch=batch, 
							region=region, 
							region_offset=region_offset)
		print(medians)


	median(data_path=data_path,
			out_path=out_path, 
			batch=batch, 
			region=region, 
			region_offset=region_offset)

	print('Medians calculated successfully')