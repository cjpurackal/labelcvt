#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import os.path
from pathlib import Path


def imageplot(xmin, ymin, xmax, ymax, file_path):
    im = np.array(Image.open(file_path), dtype=np.uint8)
    fig, ax = plt.subplots(1)
    size = im.shape

    draw = []

    labelsyolo = open(
        "/home/jeffin/agrima/datasets/capgemini/dataset"
        "/labelsbbox/apple/apple_1.txt",
        "r").read().replace(
        "\n",
        "").split(" ")[
            1:]

    labelsyolo = [float(x) for x in labelsyolo]
    print(labelsyolo)
    ax.imshow(im)
    rect = patches.Rectangle(
        (xmin,
         ymin),
        xmax,
        ymax,
        linewidth=1,
        edgecolor='b',
        facecolor="none")
    ax.add_patch(rect)

    plt.show()
