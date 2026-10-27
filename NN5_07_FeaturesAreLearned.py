# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:30:22 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 5 - VISUALIZATION 7
# FEATURES EMERGE THROUGH TRAINING
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
BLUE = "#4D9FFF"
YELLOW = "#FFD166"
GREEN = "#54E3A4"
MUTED = "#A8B2C7"

PAUSE_TIME = 0.04


def maximize_window():

    try:
        manager = plt.get_current_fig_manager()

        if hasattr(manager, "window"):
            manager.window.showMaximized()

    except Exception:
        pass


# ============================================================
# TARGET EDGE FILTERS
# ============================================================

target_filters = [
    np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=float),

    np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ], dtype=float),

    np.array([
        [-2, -1, 0],
        [-1,  0, 1],
        [ 0,  1, 2]
    ], dtype=float)
]


rng = np.random.default_rng(
    12
)


random_filters = [
    rng.normal(
        0,
        1,
        size=(3, 3)
    )
    for _ in range(3)
]


# ============================================================
# FIGURE
# ============================================================

plt.close("all")

fig, axes = plt.subplots(
    1,
    3,
    figsize=(14, 7)
)

fig.patch.set_facecolor(
    BACKGROUND
)


artists = []


for i, ax in enumerate(axes):

    ax.set_facecolor(
        PANEL
    )

    artist = ax.imshow(
        random_filters[i],
        cmap="coolwarm",
        vmin=-2,
        vmax=2
    )

    ax.set_title(
        f"FILTER {i+1}",
        color=WHITE,
        fontsize=18,
        fontweight="bold"
    )

    ax.set_xticks([])
    ax.set_yticks([])

    artists.append(
        artist
    )


fig.suptitle(
    "USEFUL FEATURES EMERGE THROUGH TRAINING",
    fontsize=27,
    color=WHITE,
    fontweight="bold",
    y=0.95
)


epoch_text = fig.text(
    0.5,
    0.12,
    "",
    ha="center",
    fontsize=21,
    color=YELLOW,
    fontweight="bold"
)


message = fig.text(
    0.5,
    0.055,
    "",
    ha="center",
    fontsize=17,
    color=MUTED
)


plt.show(block=False)

plt.pause(0.2)

maximize_window()

plt.pause(0.8)


# ============================================================
# MORPH RANDOM FILTERS INTO STRUCTURED FILTERS
# ============================================================

frames = 140


for frame in range(
    frames
):

    progress = (
        frame
        /
        (
            frames - 1
        )
    )


    t = (
        progress
        *
        progress
        *
        (
            3
            -
            2
            *
            progress
        )
    )


    for i in range(3):

        current = (
            random_filters[i]
            *
            (1-t)
            +
            target_filters[i]
            *
            t
        )

        artists[i].set_data(
            current
        )


    epoch_text.set_text(
        f"TRAINING PROGRESS: {100*progress:3.0f}%"
    )


    message.set_text(
        "Backpropagation changes the weights because useful patterns reduce the loss."
    )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


epoch_text.set_text(
    "STRUCTURED FEATURE RESPONSES"
)


message.set_text(
    "We do not manually assign each neuron a feature — useful representations are learned."
)


fig.canvas.draw_idle()
fig.canvas.flush_events()


while plt.fignum_exists(fig.number):

    fig.canvas.flush_events()

    plt.pause(0.05)