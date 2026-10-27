# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 5 - VISUALIZATION 1
# RAW INPUT = PIXELS
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# STYLE
# ============================================================

BACKGROUND = "#090D18"
PANEL = "#101827"

WHITE = "#F5F7FF"
YELLOW = "#FFD166"
MUTED = "#A8B2C7"
GRID = "#33405A"

PAUSE_TIME = 0.04


# ============================================================
# MAXIMIZE WINDOW
# ============================================================

def maximize_window():

    try:

        manager = plt.get_current_fig_manager()

        if hasattr(manager, "window"):
            manager.window.showMaximized()

    except Exception:
        pass


# ============================================================
# CREATE SIMPLE SYNTHETIC IMAGE
# ============================================================

N = 20

img = np.zeros(
    (N, N),
    dtype=float
)

# House body
img[8:17, 5:15] = 0.75

# Roof
for row in range(3, 9):

    width = row - 2

    center = 10

    left = center - width
    right = center + width + 1

    img[row, left:right] = 1.0

# Door
img[12:17, 9:11] = 0.15

# Windows
img[10:12, 6:8] = 0.15
img[10:12, 12:14] = 0.15


# ============================================================
# FIGURE
# ============================================================

plt.close("all")

fig, (ax_img, ax_pixels) = plt.subplots(
    1,
    2,
    figsize=(15, 8)
)

fig.patch.set_facecolor(
    BACKGROUND
)

for ax in [ax_img, ax_pixels]:

    ax.set_facecolor(
        PANEL
    )

    ax.tick_params(
        colors=MUTED
    )

    for spine in ax.spines.values():
        spine.set_color(GRID)


# ============================================================
# LEFT — IMAGE
# ============================================================

ax_img.imshow(
    img,
    cmap="gray",
    vmin=0,
    vmax=1
)

ax_img.set_title(
    "THE IMAGE WE SEE",
    color=WHITE,
    fontsize=21,
    fontweight="bold"
)

ax_img.axis("off")


# ============================================================
# RIGHT — PIXEL GRID
# ============================================================

pixel_view = ax_pixels.imshow(
    np.zeros_like(img),
    cmap="gray",
    vmin=0,
    vmax=1
)

ax_pixels.set_title(
    "WHAT THE NETWORK RECEIVES",
    color=WHITE,
    fontsize=21,
    fontweight="bold"
)

ax_pixels.set_xticks(
    np.arange(-0.5, N, 1),
    minor=True
)

ax_pixels.set_yticks(
    np.arange(-0.5, N, 1),
    minor=True
)

ax_pixels.grid(
    which="minor",
    color=GRID,
    linewidth=0.5,
    alpha=0.5
)

ax_pixels.tick_params(
    left=False,
    bottom=False,
    labelleft=False,
    labelbottom=False
)


# ============================================================
# TEXT
# ============================================================

fig.suptitle(
    "DEEP NETWORKS START WITH RAW NUMBERS",
    fontsize=27,
    color=WHITE,
    fontweight="bold",
    y=0.96
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


# ============================================================
# SHOW + MAXIMIZE
# ============================================================

plt.show(block=False)

plt.pause(0.2)

maximize_window()

plt.pause(0.7)


# ============================================================
# REVEAL PIXELS
# ============================================================

current = np.zeros_like(img)

indices = [
    (r, c)
    for r in range(N)
    for c in range(N)
]

for step, (r, c) in enumerate(indices):

    current[r, c] = img[r, c]

    if step % 4 == 0:

        pixel_view.set_data(
            current
        )

        message.set_text(
            "To the network, this image begins as a grid of pixel values."
        )

        fig.canvas.draw_idle()
        fig.canvas.flush_events()

        plt.pause(
            0.015
        )


pixel_view.set_data(
    img
)

message.set_text(
    "RAW INPUT = PIXEL VALUES"
)

fig.canvas.draw_idle()
fig.canvas.flush_events()


while plt.fignum_exists(fig.number):

    fig.canvas.flush_events()

    plt.pause(0.05)