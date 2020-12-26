# Vince J. Straub, 2020

from matplotlib import colors as mcolors
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random 
import glob 

def run():
    """Plots a simple random walk drawing in 2 dimensions 
    and then randomly calls an image interpolation method
    to fill out the image. The image is saved in the your
    local directory.
    """
    methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
              'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
              'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

    x = random.randint(10,20)
    y = random.randint(10,50)
    z = np.random.rand(x,y)
    cmap = plt.cm.colors.ListedColormap(np.random.rand(200,4))

    plt.figure(figsize=(12,7))
    ax = plt.axes()

    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.imshow(z, cmap=cmap, interpolation=random.choice(methods))

    plt.savefig('a_la_recherche_de_Vera_Molner_example_output.png', bbox_inches='tight', pad_inches=0.25)

if __name__ == "__main__":
    run()


