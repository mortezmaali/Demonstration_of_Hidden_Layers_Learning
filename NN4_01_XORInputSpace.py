# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 4 - VISUALIZATION 1
# XOR IN THE ORIGINAL INPUT SPACE
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")


import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# SETTINGS
# ============================================================

RANDOM_SEED = 5
N_PER_CLUSTER = 18

PAUSE_TIME = 0.035

BACKGROUND = "#090D18"

RED = "#FF5369"
BLUE = "#4D9FFF"

WHITE = "#F5F7FF"
YELLOW = "#FFD166"

MUTED = "#A8B2C7"
GRID = "#33405A"


# ============================================================
# MAXIMIZE WINDOW
# ============================================================

def maximize_window():

    try:

        manager = plt.get_current_fig_manager()

        if hasattr(
            manager,
            "window"
        ):

            manager.window.showMaximized()

    except Exception:

        pass


# ============================================================
# XOR DATA
# ============================================================

rng = np.random.default_rng(
    RANDOM_SEED
)


bottom_left = rng.normal(
    (-1, -1),
    0.22,
    size=(N_PER_CLUSTER, 2)
)


top_left = rng.normal(
    (-1, 1),
    0.22,
    size=(N_PER_CLUSTER, 2)
)


bottom_right = rng.normal(
    (1, -1),
    0.22,
    size=(N_PER_CLUSTER, 2)
)


top_right = rng.normal(
    (1, 1),
    0.22,
    size=(N_PER_CLUSTER, 2)
)


red_points = np.vstack(
    [
        bottom_left,
        top_right
    ]
)


blue_points = np.vstack(
    [
        top_left,
        bottom_right
    ]
)


# ============================================================
# FIGURE
# ============================================================

plt.close("all")


fig, ax = plt.subplots(
    figsize=(12, 8)
)


fig.patch.set_facecolor(
    BACKGROUND
)


ax.set_facecolor(
    BACKGROUND
)


ax.set_xlim(
    -2,
    2
)


ax.set_ylim(
    -2,
    2
)


ax.set_xlabel(
    r"$x_1$  /  Input 1",
    fontsize=16,
    color=WHITE
)


ax.set_ylabel(
    r"$x_2$  /  Input 2",
    fontsize=16,
    color=WHITE
)


ax.tick_params(
    colors=MUTED
)


ax.grid(
    alpha=0.20,
    color=GRID,
    linestyle=":"
)


for spine in ax.spines.values():

    spine.set_color(
        GRID
    )


# ============================================================
# DATA
# ============================================================

ax.scatter(
    red_points[:, 0],
    red_points[:, 1],
    s=125,
    color=RED,
    edgecolor=WHITE,
    linewidth=0.8,
    zorder=5
)


ax.scatter(
    blue_points[:, 0],
    blue_points[:, 1],
    s=125,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=0.8,
    zorder=5
)


# ============================================================
# DECISION LINE
# ============================================================

line, = ax.plot(
    [],
    [],
    color=WHITE,
    linewidth=4,
    zorder=4
)


ax.set_title(
    "ORIGINAL INPUT SPACE",
    fontsize=25,
    color=WHITE,
    fontweight="bold",
    pad=20
)


ax.text(
    0.5,
    1.015,
    r"Each point is described by $(x_1,x_2)$",
    transform=ax.transAxes,
    ha="center",
    fontsize=15,
    color=MUTED
)


message = ax.text(
    0.5,
    0.05,
    "",
    transform=ax.transAxes,
    ha="center",
    fontsize=17,
    color=YELLOW,
    fontweight="bold"
)


# ============================================================
# SHOW + MAXIMIZE
# ============================================================

plt.show(
    block=False
)

plt.pause(
    0.2
)

maximize_window()

plt.pause(
    0.6
)


# ============================================================
# ROTATE LINE
# ============================================================

frames = 180


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


    angle = (
        progress
        *
        np.pi
    )


    dx = np.cos(
        angle
    )


    dy = np.sin(
        angle
    )


    line.set_data(
        [
            -3 * dx,
            3 * dx
        ],
        [
            -3 * dy,
            3 * dy
        ]
    )


    message.set_text(
        "One straight boundary cannot separate XOR."
    )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


message.set_text(
    "THE ORIGINAL REPRESENTATION MAKES THE PROBLEM DIFFICULT"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()


# ============================================================
# KEEP OPEN
# ============================================================

while plt.fignum_exists(
    fig.number
):

    fig.canvas.flush_events()

    plt.pause(
        0.05
    )