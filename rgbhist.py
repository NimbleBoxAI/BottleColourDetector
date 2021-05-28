#usage: python rgbhist.py ./pics/auto_seg/ ./hists/ True

import sys
from skimage import io
import matplotlib.pyplot as plt
import os
import argparse


def hist(in_path, out_path, batch=False):

	if batch is False:
		image = io.imread(path)
		fig = plt.figure(figsize = [10, 5])

		plt.subplot(1, 2, 1)
		plt.imshow(image)
		plt.title(path.rpartition('/')[-1][:-4])

		plt.subplot(1, 2, 2)
		plt.hist(image.ravel(), bins = 256, color = 'orange', )
		plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
		plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
		plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
		plt.xlabel('Intensity Value')
		plt.ylabel('Count')
		plt.legend(['Total', 'Red_Channel', 'Green_Channel', 'Blue_Channel'])
		
		return fig

	else:
		with os.scandir(in_path) as entries:
			for entry in entries:
				if entry.is_file():
					image = io.imread(f'{in_path}{entry.name}')
					plt.figure(figsize = [10, 5])

					plt.subplot(1, 2, 1)
					plt.imshow(image)
					plt.title(entry.name)

					plt.subplot(1, 2, 2)
					plt.hist(image.ravel(), bins = 256, color = 'orange', )
					plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
					plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
					plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
					plt.xlabel('Intensity Value')
					plt.ylabel('Count')
					plt.legend(['Total', 'Red_Channel', 'Green_Channel', 'Blue_Channel'])
					plt.savefig(f'{out_path}{entry.name}')
					plt.close()

		return True


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Process Images')

    parser.add_argument('in_path', default='./pics/auto_seg/', help='Path to input directory')
    parser.add_argument('out_path', default='./hists/', help='Path to output directory')
    parser.add_argument('batch', type = bool, default=True, help='Whether process in batch or not')
    args = parser.parse_args()

    hist(args.in_path, args.out_path, args.batch)