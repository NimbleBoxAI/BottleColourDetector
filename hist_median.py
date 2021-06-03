import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.image as mpimg
import pickle
import os

def is_too_bright(pixel):
    # Filters out too bright pixels which can skew mean RGB values
    if pixel[0] < 250 and pixel[1] < 250 and pixel[2] < 250:
        return False
    else:
        return True

def is_too_dark(pixel):
    # Filters out too dark pixels which can skew mean RGB values
    if pixel[0] > 5 and pixel[1] > 5 and pixel[2] > 5:
        return False
    else:
        return True

def median(in_path, out_path, batch=False, region='center', region_offset=50):

	if batch is False:
		image = mpimg.imread(in_path)

		if region == 'whole':
			selection = image
		elif region == 'center':
			center = [image.shape[0]//2, image.shape[1]//2]
			selection = image[center[0] - region_offset : center[0] + region_offset, 
							  center[1] - region_offset : center[1] + region_offset]


		r_median = np.median(selection[:,:,0])
		g_median = np.median(selection[:,:,1])
		b_median = np.median(selection[:,:,2])
		
		return (r_median,g_median,b_median)

	else:
		median_values = []
		with os.scandir(in_path) as entries:
			for entry in entries:
				if entry.is_file():
					image = mpimg.imread(f'{in_path}{entry.name}')

					
					if region == 'whole':
						selection = image
					elif region == 'center':
						center = [image.shape[0]//2, image.shape[1]//2]
						selection = image[center[0] - region_offset : center[0] + region_offset, 
										  center[1] - region_offset : center[1] + region_offset]


					r_median = np.median(selection[:,:,0])
					g_median = np.median(selection[:,:,1])
					b_median = np.median(selection[:,:,2])

					median_values.append((r_median,g_median,b_median))

		f = open(out_path,'wb')
		pickle.dump(median_values, f)
		f.close()

		return True

if __name__=='__main__':

	# These parameters can be accepted as arguments
	in_path = './pics/auto_seg/'
	out_path = 'medians_center.pkl'
	batch = True
	region = 'center'
	region_offset = 50

	median(in_path=in_path,
			out_path=out_path, 
			batch=batch, 
			region=region, 
			region_offset=region_offset)

	print('Medians calculated successfully')