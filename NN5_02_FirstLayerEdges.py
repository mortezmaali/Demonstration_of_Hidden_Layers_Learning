# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:26:12 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 5 - VISUALIZATION 2
# FIRST LAYER — SIMPLE EDGES
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")

import numpy as np
import matplotlib.pyplot as plt


BACKGROUND = "#090D18"
PANEL = "#101827"

WHITE = "#F5F7FF"
YELLOW = "#FFD166"
MUTED = "#A8B2C7"
GRID = "#33405A"

PAUSE_TIME = 0.04


def maximize_window():

    try:
        manager = plt.get_current_fig_manager()

        if hasattr(manager, "window"):
            manager.window.showMaximized()

    except Exception:
        pass


# ============================================================
# IMAGE
# ============================================================

N = 20

img = np.zeros((N, N))

img[8:17, 5:15] = 0.75

for row in range(3, 9):

    width = row - 2
    center = 10

    img[
        row,
        center-width:center+width+1
    ] = 1.0

img[12:17, 9:11] = 0.15
img[10:12, 6:8] = 0.15
img[10:12, 12:14] = 0.15


# ============================================================
# SIMPLE CONVOLUTION
# ============================================================

def conv2d_same(image, kernel):

    kh, kw = kernel.shape

    ph = kh // 2
    pw = kw // 2

    padded = np.pad(
        image,
        ((ph, ph), (pw, pw)),
        mode="edge"
    )

    output = np.zeros_like(image)

    for r in range(image.shape[0]):

        for c in range(image.shape[1]):

            region = padded[
                r:r+kh,
                c:c+kw
            ]

            output[r, c] = np.sum(
                region * kernel
            )

    return output


vertical_kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])


horizontal_kernel = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])


diag_kernel = np.array([
    [-2, -1, 0],
    [-1,  0, 1],
    [ 0,  1, 2]
])


responses = [
    np.abs(
        conv2d_same(
            img,
            vertical_kernel
        )
    ),

    np.abs(
        conv2d_same(
            img,
            horizontal_kernel
        )
    ),

    np.abs(
        conv2d_same(
            img,
            diag_kernel
        )
    )
]


titles = [
    "VERTICAL EDGES",
    "HORIZONTAL EDGES",
    "DIAGONAL EDGES"
]


# Normalize
responses = [
    r / (np.max(r) + 1e-9)
    for r in responses
]


# ============================================================
# FIGURE
# ============================================================

plt.close("all")

fig, axes = plt.subplots(
    1,
    4,
    figsize=(16, 7)
)

fig.patch.set_facecolor(
    BACKGROUND
)


for ax in axes:

    ax.set_facecolor(
        PANEL
    )

    ax.axis("off")


axes[0].imshow(
    img,
    cmap="gray",
    vmin=0,
    vmax=1
)

axes[0].set_title(
    "RAW PIXELS",
    color=WHITE,
    fontsize=18,
    fontweight="bold"
)


feature_images = []

for i in range(3):

    artist = axes[i+1].imshow(
        np.zeros_like(img),
        cmap="magma",
        vmin=0,
        vmax=1
    )

    axes[i+1].set_title(
        titles[i],
        color=WHITE,
        fontsize=18,
        fontweight="bold"
    )

    feature_images.append(
        artist
    )


fig.suptitle(
    "FIRST LAYER: SIMPLE FEATURES",
    fontsize=27,
    color=WHITE,
    fontweight="bold",
    y=0.95
)


message = fig.text(
    0.5,
    0.05,
    "",
    ha="center",
    fontsize=18,
    color=YELLOW,
    fontweight="bold"
)


# ============================================================
# SHOW + MAXIMIZE
# ============================================================

plt.show(block=False)

plt.pause(0.2)

maximize_window()

plt.pause(0.7)


# ============================================================
# REVEAL FEATURE MAPS
# ============================================================

for i in range(3):

    for alpha in np.linspace(
        0,
        1,
        45
    ):

        feature_images[i].set_data(
            responses[i] * alpha
        )

        message.set_text(
            "Early features can respond to simple edge patterns."
        )

        fig.canvas.draw_idle()
        fig.canvas.flush_events()

        plt.pause(
            PAUSE_TIME
        )

    plt.pause(
        0.5
    )


message.set_text(
    "PIXELS  →  SIMPLE EDGES"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()


while plt.fignum_exists(fig.number):

    fig.canvas.flush_events()

    plt.pause(0.05)