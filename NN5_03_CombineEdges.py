# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:27:15 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 5 - VISUALIZATION 3
# SECOND LAYER — COMBINE SIMPLE FEATURES
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
# SYNTHETIC FEATURE MAPS
# ============================================================

N = 40

vertical = np.zeros((N, N))
horizontal = np.zeros((N, N))

vertical[
    8:32,
    19:22
] = 1

horizontal[
    19:22,
    8:32
] = 1


corner = (
    vertical
    +
    horizontal
)

corner = np.clip(
    corner,
    0,
    1
)


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
    vertical,
    cmap="magma",
    vmin=0,
    vmax=1
)

axes[0].set_title(
    "VERTICAL EDGE",
    color=WHITE,
    fontsize=18,
    fontweight="bold"
)


axes[1].imshow(
    horizontal,
    cmap="magma",
    vmin=0,
    vmax=1
)

axes[1].set_title(
    "HORIZONTAL EDGE",
    color=WHITE,
    fontsize=18,
    fontweight="bold"
)


axes[2].text(
    0.5,
    0.5,
    "+",
    transform=axes[2].transAxes,
    ha="center",
    va="center",
    fontsize=75,
    color=WHITE
)


axes[3].set_title(
    "COMBINED PATTERN",
    color=WHITE,
    fontsize=18,
    fontweight="bold"
)


combined_artist = axes[3].imshow(
    np.zeros_like(corner),
    cmap="viridis",
    vmin=0,
    vmax=1
)


fig.suptitle(
    "SECOND LAYER: COMBINE SIMPLE FEATURES",
    fontsize=27,
    color=WHITE,
    fontweight="bold",
    y=0.95
)


message = fig.text(
    0.5,
    0.055,
    "",
    ha="center",
    fontsize=18,
    color=YELLOW,
    fontweight="bold"
)


plt.show(block=False)

plt.pause(0.2)

maximize_window()

plt.pause(0.8)


for alpha in np.linspace(
    0,
    1,
    80
):

    combined_artist.set_data(
        corner * alpha
    )

    message.set_text(
        "A deeper neuron can combine several simpler features."
    )

    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


message.set_text(
    "EDGES  →  CORNERS / LOCAL PATTERNS"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()


while plt.fignum_exists(fig.number):

    fig.canvas.flush_events()

    plt.pause(0.05)