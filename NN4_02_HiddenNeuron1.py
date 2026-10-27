# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 4 - VISUALIZATION 2
# HIDDEN NEURON 1
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

RED = "#FF5369"
BLUE = "#4D9FFF"

WHITE = "#F5F7FF"
YELLOW = "#FFD166"

MUTED = "#A8B2C7"
GRID = "#33405A"

PAUSE_TIME = 0.04


# ============================================================
# MAXIMIZE
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
# SIGMOID
# ============================================================

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


# ============================================================
# XOR DATA
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


# ============================================================
# RESPONSE FIELD
# ============================================================

grid_x = np.linspace(
    -2,
    2,
    400
)


grid_y = np.linspace(
    -2,
    2,
    400
)


XX, YY = np.meshgrid(
    grid_x,
    grid_y
)


H1 = sigmoid(
    8
    *
    (
        XX
        +
        YY
        +
        0.5
    )
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
    r"$x_1$",
    fontsize=16,
    color=WHITE
)


ax.set_ylabel(
    r"$x_2$",
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


response_image = ax.imshow(
    H1,
    extent=[
        -2,
        2,
        -2,
        2
    ],
    origin="lower",
    cmap="Blues",
    vmin=0,
    vmax=1,
    alpha=0,
    interpolation="bilinear",
    zorder=1
)


ax.scatter(
    red_points[:, 0],
    red_points[:, 1],
    s=120,
    color=RED,
    edgecolor=WHITE,
    linewidth=0.8,
    zorder=5
)


ax.scatter(
    blue_points[:, 0],
    blue_points[:, 1],
    s=120,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=0.8,
    zorder=5
)


x_line = np.linspace(
    -2.5,
    2.5,
    300
)


y_line = (
    -x_line
    -
    0.5
)


boundary, = ax.plot(
    x_line,
    y_line,
    color=YELLOW,
    linewidth=4,
    alpha=0
)


ax.set_title(
    "HIDDEN NEURON 1",
    fontsize=25,
    color=WHITE,
    fontweight="bold",
    pad=20
)


ax.text(
    0.5,
    1.015,
    r"$h_1=\sigma(8(x_1+x_2+0.5))$",
    transform=ax.transAxes,
    ha="center",
    fontsize=17,
    color=YELLOW
)


message = ax.text(
    0.5,
    0.05,
    "",
    transform=ax.transAxes,
    ha="center",
    fontsize=16,
    color=MUTED
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
# BOUNDARY
# ============================================================

for alpha_value in np.linspace(
    0,
    1,
    45
):

    boundary.set_alpha(
        alpha_value
    )


    message.set_text(
        "The neuron creates one linear boundary."
    )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# RESPONSE FIELD
# ============================================================

for alpha_value in np.linspace(
    0,
    0.45,
    60
):

    response_image.set_alpha(
        alpha_value
    )


    message.set_text(
        "Its output is a continuous response, not just a line."
    )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


message.set_text(
    r"Every $(x_1,x_2)$ point becomes a new value:  $h_1$"
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