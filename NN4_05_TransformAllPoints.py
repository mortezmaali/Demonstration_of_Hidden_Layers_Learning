# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 4 - VISUALIZATION 5
# TRANSFORM THE ENTIRE DATASET
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


def hidden_transform(
    points
):

    x1 = points[:, 0]
    x2 = points[:, 1]


    h1 = sigmoid(
        8
        *
        (
            x1
            +
            x2
            +
            0.5
        )
    )


    h2 = sigmoid(
        8
        *
        (
            x1
            +
            x2
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


bottom_left = rng.normal(
    (-1, -1),
    0.22,
    size=(N, 2)
)


top_left = rng.normal(
    (-1, 1),
    0.22,
    size=(N, 2)
)


bottom_right = rng.normal(
    (1, -1),
    0.22,
    size=(N, 2)
)


top_right = rng.normal(
    (1, 1),
    0.22,
    size=(N, 2)
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


red_hidden = hidden_transform(
    red_points
)


blue_hidden = hidden_transform(
    blue_points
)


# ============================================================
# FIGURE
# ============================================================

plt.close("all")


fig, (
    ax_input,
    ax_hidden
) = plt.subplots(
    1,
    2,
    figsize=(15, 8)
)


fig.patch.set_facecolor(
    BACKGROUND
)


for ax in [
    ax_input,
    ax_hidden
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
# INPUT SPACE
# ============================================================

ax_input.set_xlim(
    -2,
    2
)


ax_input.set_ylim(
    -2,
    2
)


ax_input.set_xlabel(
    r"$x_1$",
    color=WHITE,
    fontsize=15
)


ax_input.set_ylabel(
    r"$x_2$",
    color=WHITE,
    fontsize=15
)


ax_input.set_title(
    "INPUT SPACE  $(x_1,x_2)$",
    color=WHITE,
    fontsize=19
)


input_red = ax_input.scatter(
    red_points[:, 0],
    red_points[:, 1],
    s=115,
    color=RED,
    edgecolor=WHITE,
    linewidth=0.7
)


input_blue = ax_input.scatter(
    blue_points[:, 0],
    blue_points[:, 1],
    s=115,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=0.7
)


# ============================================================
# HIDDEN SPACE
# ============================================================

ax_hidden.set_xlim(
    -0.08,
    1.08
)


ax_hidden.set_ylim(
    -0.08,
    1.08
)


ax_hidden.set_xlabel(
    r"$h_1$",
    color=WHITE,
    fontsize=15
)


ax_hidden.set_ylabel(
    r"$h_2$",
    color=WHITE,
    fontsize=15
)


ax_hidden.set_title(
    "HIDDEN SPACE  $(h_1,h_2)$",
    color=WHITE,
    fontsize=19
)


hidden_red = ax_hidden.scatter(
    red_hidden[:, 0],
    red_hidden[:, 1],
    s=115,
    color=RED,
    edgecolor=WHITE,
    linewidth=0.7,
    alpha=0
)


hidden_blue = ax_hidden.scatter(
    blue_hidden[:, 0],
    blue_hidden[:, 1],
    s=115,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=0.7,
    alpha=0
)


# ============================================================
# OVERLAY
# ============================================================

overlay = fig.add_axes(
    [
        0,
        0,
        1,
        1
    ],
    frameon=False
)


overlay.set_xlim(
    0,
    1
)


overlay.set_ylim(
    0,
    1
)


overlay.axis(
    "off"
)


moving_red = overlay.scatter(
    [],
    [],
    s=115,
    color=RED,
    edgecolor=WHITE,
    linewidth=0.7,
    zorder=20
)


moving_blue = overlay.scatter(
    [],
    [],
    s=115,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=0.7,
    zorder=20
)


fig.suptitle(
    "THE HIDDEN LAYER TRANSFORMS THE DATA",
    fontsize=26,
    color=WHITE,
    fontweight="bold",
    y=0.96
)


message = fig.text(
    0.5,
    0.05,
    "",
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
    0.8
)


# IMPORTANT:
# Render after maximizing so coordinate transforms correspond
# to the maximized window.

fig.canvas.draw()

plt.pause(
    0.2
)


# ============================================================
# COORDINATE TRANSFORMS
# ============================================================

inverse_fig = fig.transFigure.inverted()


red_start_pixels = ax_input.transData.transform(
    red_points
)


blue_start_pixels = ax_input.transData.transform(
    blue_points
)


red_end_pixels = ax_hidden.transData.transform(
    red_hidden
)


blue_end_pixels = ax_hidden.transData.transform(
    blue_hidden
)


red_start = inverse_fig.transform(
    red_start_pixels
)


blue_start = inverse_fig.transform(
    blue_start_pixels
)


red_end = inverse_fig.transform(
    red_end_pixels
)


blue_end = inverse_fig.transform(
    blue_end_pixels
)


input_red.set_alpha(
    0.15
)


input_blue.set_alpha(
    0.15
)


# ============================================================
# TRANSFORM
# ============================================================

frames = 120


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


    current_red = (
        red_start
        *
        (
            1 - t
        )
        +
        red_end
        *
        t
    )


    current_blue = (
        blue_start
        *
        (
            1 - t
        )
        +
        blue_end
        *
        t
    )


    moving_red.set_offsets(
        current_red
    )


    moving_blue.set_offsets(
        current_blue
    )


    message.set_text(
        r"$(x_1,x_2)$  →  HIDDEN LAYER  →  $(h_1,h_2)$"
    )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# FINAL
# ============================================================

moving_red.set_offsets(
    np.empty(
        (
            0,
            2
        )
    )
)


moving_blue.set_offsets(
    np.empty(
        (
            0,
            2
        )
    )
)


hidden_red.set_alpha(
    1
)


hidden_blue.set_alpha(
    1
)


message.set_text(
    "THE HIDDEN LAYER HAS REORGANIZED THE DATA"
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