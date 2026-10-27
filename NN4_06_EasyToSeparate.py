# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 4 - VISUALIZATION 6
# NONLINEAR BEFORE -> LINEAR AFTER
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")


import numpy as np
import matplotlib.pyplot as plt


BACKGROUND = "#090D18"
PANEL = "#101827"

RED = "#FF5369"
BLUE = "#4D9FFF"

WHITE = "#F5F7FF"
YELLOW = "#FFD166"
GREEN = "#54E3A4"

MUTED = "#A8B2C7"
GRID = "#33405A"

PAUSE_TIME = 0.035


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


def sigmoid(z):

    z = np.clip(
        z,
        -30,
        30
    )

    return (
        1
        /
        (
            1
            +
            np.exp(-z)
        )
    )


def transform(
    points
):

    x1 = points[:, 0]

    x2 = points[:, 1]


    s = (
        x1
        +
        x2
    )


    h1 = sigmoid(
        8
        *
        (
            s
            +
            0.5
        )
    )


    h2 = sigmoid(
        8
        *
        (
            s
            -
            0.5
        )
    )


    return np.column_stack(
        [
            h1,
            h2
        ]
    )


# ============================================================
# DATA
# ============================================================

rng = np.random.default_rng(
    5
)


N = 18


bl = rng.normal(
    (-1, -1),
    0.22,
    size=(N, 2)
)


tl = rng.normal(
    (-1, 1),
    0.22,
    size=(N, 2)
)


br = rng.normal(
    (1, -1),
    0.22,
    size=(N, 2)
)


tr = rng.normal(
    (1, 1),
    0.22,
    size=(N, 2)
)


red = np.vstack(
    [
        bl,
        tr
    ]
)


blue = np.vstack(
    [
        tl,
        br
    ]
)


red_h = transform(
    red
)


blue_h = transform(
    blue
)


# ============================================================
# FIGURE
# ============================================================

plt.close("all")


fig, (
    ax1,
    ax2
) = plt.subplots(
    1,
    2,
    figsize=(15, 8)
)


fig.patch.set_facecolor(
    BACKGROUND
)


for ax in [
    ax1,
    ax2
]:

    ax.set_facecolor(
        PANEL
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
# INPUT
# ============================================================

ax1.set_xlim(
    -2,
    2
)


ax1.set_ylim(
    -2,
    2
)


ax1.set_xlabel(
    r"$x_1$",
    color=WHITE,
    fontsize=15
)


ax1.set_ylabel(
    r"$x_2$",
    color=WHITE,
    fontsize=15
)


ax1.set_title(
    "INPUT SPACE",
    color=WHITE,
    fontsize=20,
    fontweight="bold"
)


ax1.scatter(
    red[:, 0],
    red[:, 1],
    s=115,
    color=RED,
    edgecolor=WHITE,
    linewidth=0.8
)


ax1.scatter(
    blue[:, 0],
    blue[:, 1],
    s=115,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=0.8
)


bad_line, = ax1.plot(
    [],
    [],
    color=WHITE,
    linewidth=4
)


# ============================================================
# HIDDEN SPACE
# ============================================================

ax2.set_xlim(
    -0.08,
    1.08
)


ax2.set_ylim(
    -0.08,
    1.08
)


ax2.set_xlabel(
    r"$h_1$",
    color=WHITE,
    fontsize=15
)


ax2.set_ylabel(
    r"$h_2$",
    color=WHITE,
    fontsize=15
)


ax2.set_title(
    "HIDDEN FEATURE SPACE",
    color=WHITE,
    fontsize=20,
    fontweight="bold"
)


ax2.scatter(
    red_h[:, 0],
    red_h[:, 1],
    s=115,
    color=RED,
    edgecolor=WHITE,
    linewidth=0.8
)


ax2.scatter(
    blue_h[:, 0],
    blue_h[:, 1],
    s=115,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=0.8
)


good_line, = ax2.plot(
    [],
    [],
    color=GREEN,
    linewidth=4
)


# ============================================================
# TITLES
# ============================================================

fig.suptitle(
    "THE SAME CLASSIFICATION PROBLEM — A BETTER REPRESENTATION",
    fontsize=24,
    color=WHITE,
    fontweight="bold",
    y=0.965
)


message = fig.text(
    0.5,
    0.045,
    "",
    ha="center",
    fontsize=18,
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
    0.7
)


# ============================================================
# ORIGINAL SPACE
# ============================================================

frames = 130


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


    bad_line.set_data(
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
        "INPUT SPACE: NO SINGLE STRAIGHT LINE CAN SEPARATE XOR"
    )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


plt.pause(
    0.6
)


# ============================================================
# CORRECT HIDDEN-SPACE SEPARATOR
#
# h2 ≈ 0.81 h1 - 0.006
# ============================================================

h1_values = np.linspace(
    -0.10,
    1.10,
    300
)


final_h2 = (
    0.81
    *
    h1_values
    -
    0.006
)


start_h2 = np.full_like(
    h1_values,
    -0.15
)


frames = 90


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


    current_h2 = (
        start_h2
        *
        (
            1 - t
        )
        +
        final_h2
        *
        t
    )


    good_line.set_data(
        h1_values,
        current_h2
    )


    message.set_text(
        "HIDDEN SPACE: NOW ONE STRAIGHT LINE CAN SEPARATE THE CLASSES"
    )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


message.set_text(
    "NONLINEAR IN INPUT SPACE  →  LINEAR IN HIDDEN SPACE"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()


while plt.fignum_exists(
    fig.number
):

    fig.canvas.flush_events()

    plt.pause(
        0.05
    )