# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:27:43 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 5 - VISUALIZATION 4
# DEEPER LAYER — LARGER STRUCTURES
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

PAUSE_TIME = 0.04


def maximize_window():

    try:
        manager = plt.get_current_fig_manager()

        if hasattr(manager, "window"):
            manager.window.showMaximized()

    except Exception:
        pass


# ============================================================
# FEATURE STAGES
# ============================================================

N = 50


edge_map = np.zeros((N, N))

edge_map[8:42, 10] = 1
edge_map[8:42, 39] = 1
edge_map[8, 10:40] = 1
edge_map[41, 10:40] = 1


corner_map = np.zeros((N, N))

for r, c in [
    (8, 10),
    (8, 39),
    (41, 10),
    (41, 39)
]:

    corner_map[
        r-2:r+3,
        c-2:c+3
    ] = 1


shape_map = np.zeros((N, N))

shape_map[
    8:42,
    10:40
] = 0.55

shape_map[
    12:38,
    14:36
] = 0


# ============================================================
# FIGURE
# ============================================================

plt.close("all")

fig, axes = plt.subplots(
    1,
    3,
    figsize=(15, 7)
)

fig.patch.set_facecolor(
    BACKGROUND
)


for ax in axes:

    ax.set_facecolor(
        PANEL
    )

    ax.axis("off")


artists = [
    axes[0].imshow(
        np.zeros_like(edge_map),
        cmap="magma",
        vmin=0,
        vmax=1
    ),

    axes[1].imshow(
        np.zeros_like(corner_map),
        cmap="viridis",
        vmin=0,
        vmax=1
    ),

    axes[2].imshow(
        np.zeros_like(shape_map),
        cmap="plasma",
        vmin=0,
        vmax=1
    )
]


titles = [
    "EDGES",
    "LOCAL PATTERNS",
    "LARGER STRUCTURE"
]


for ax, title in zip(
    axes,
    titles
):

    ax.set_title(
        title,
        color=WHITE,
        fontsize=19,
        fontweight="bold"
    )


fig.suptitle(
    "DEEPER LAYERS BUILD ON EARLIER FEATURES",
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


plt.show(block=False)

plt.pause(0.2)

maximize_window()

plt.pause(0.7)


maps = [
    edge_map,
    corner_map,
    shape_map
]


messages = [
    "Layer 1 responds to simple local structure.",
    "Layer 2 combines those responses.",
    "A deeper layer can represent a larger pattern."
]


for artist, fmap, text in zip(
    artists,
    maps,
    messages
):

    for alpha in np.linspace(
        0,
        1,
        55
    ):

        artist.set_data(
            fmap * alpha
        )

        message.set_text(
            text
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
    "SIMPLE FEATURES  →  LARGER STRUCTURES"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()


while plt.fignum_exists(fig.number):

    fig.canvas.flush_events()

    plt.pause(0.05)