import numpy as np
from sklearn.cluster import KMeans
import imageio
import skimage.transform
import math
import os as os

def load_paintings(artist):

    path = 'samples/' + artist
    files = os.listdir(path)

    image_list = []
    flatten_list = []

    for i in range(len(files)):

        file = path + '/' + files[i]
        image = np.array(imageio.imread(file))

        width = math.floor(image.shape[0] * 0.25)
        height = math.floor(image.shape[1] * 0.25)
        new_size = (width, height)

        resized_image = skimage.transform.resize(image, new_size, order=3)

        image_list.append(resized_image)

        flatten = resized_image.reshape((width * height), -1)
        flatten_list.append(flatten)

    return image_list, flatten_list


def cluster_paintings(artist, bits=32):
    image_list, flatten_list = load_paintings(artist)

    kmeans = KMeans(n_clusters=bits, random_state=21)

    centroids_list = []

    try:
        np.load('cache/{}_{}_centroids.npy'.format(artist, bits))
    except:

        print('Clutering started. {} pictures in total.'.format(len(flatten_list)))
        for i in range(len(flatten_list)):
            kmeans.fit(flatten_list[i])
            centroids = kmeans.cluster_centers_

            centroids_list.append(centroids)

            print('Clustering... {}/{}'.format(i, len(flatten_list)))

        filename = 'cache/{}_{}_centroids.npy'.format(artist, bits)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        np.save(filename, centroids_list)
        print('Clustering done!')

    return image_list
