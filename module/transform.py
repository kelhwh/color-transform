import numpy as np
import imageio
import skimage.transform
import math
import os
import matplotlib.pyplot as plt


def transform_my_pic(artist, target_pic, bits, image_list, output_width=300, method='closest'):
    try:
        centroids_list = np.load('cache/{}_{}_centroids.npy'.format(artist, bits))
    except:
        print("No clusters found for '{}'. Please do clustering_paintings first!".format(artist))

    # start to read in the pic to be transformed
    target = np.array(imageio.imread(target_pic))

    ratio = target.shape[1] / target.shape[0]
    output_height = math.floor(output_width * ratio)

    resized_target = skimage.transform.resize(target, (output_width, output_height), order=3)
    target_flatten = resized_target.reshape((output_width * output_height), -1)

    # distance_to_samples stores the sum of distance between each pixel in target pic and the closeset centroids in each sample paintings, shape = [1, number of sample paintings]
    distance_to_samples = []

    # target_mapped stores the index of centroid that each pixel will be assigned to for all sample paintings, shape = [# paintings, target_width, target_height]
    target_mapped = np.zeros((len(centroids_list), output_width * output_height))

    for s in range(len(centroids_list)):
        distance_to_samples.append(0)

        print("Comparing your picture with {}'s paintings... {}/{}".format(artist, s, len(centroids_list)))

        for i in range(len(target_flatten)):
            distance = np.sqrt(np.sum(np.power(target_flatten[i] - centroids_list[s], 2), axis=1))

            target_mapped[s, i] = np.argmin(distance)

            min_distance = np.min(distance)
            distance_to_samples[s] += min_distance

    closest_sample = np.argmin(distance_to_samples)
    farthest_sample = np.argmax(distance_to_samples)

    assert method in ['closest', 'farthest'], "Please choose one of the methods: 'closest' or 'farthest'"

    if method == 'closest':
        target_transformed = centroids_list[closest_sample][target_mapped[closest_sample].astype(
            'int')]  # only int can be used as index to transform back in to centroids
        plt.imshow(image_list[closest_sample])
        plt.show()
    elif method == 'farthest':
        target_transformed = centroids_list[farthest_sample][target_mapped[farthest_sample].astype('int')]
        plt.imshow(image_list[farthest_sample])
        plt.show()

    target_transformed = target_transformed.reshape(output_width, output_height, -1)

    plt.imshow(resized_target)
    plt.show()
    plt.imshow(target_transformed)
    plt.show()