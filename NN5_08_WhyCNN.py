# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:31:09 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 5 - VISUALIZATION 8
# WHY IMAGES NEED SOMETHING SPECIAL
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle


BACKGROUND = "#090D18"
PANEL = "#101827"

WHITE = "#F5F7FF"
BLUE = "#4D9FFF"
YELLOW = "#FFD166"
RED = "#FF5369"
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
# FIGURE
# ============================================================

plt.close("all")

fig, ax = plt.subplots(
    figsize=(15, 8)
)

fig.patch.set_facecolor(
    BACKGROUND
)

ax.set_facecolor(
    BACKGROUND
)

ax.set_xlim(
    0,
    15
)

ax.set_ylim(
    0,
    8
)

ax.axis("off")


fig.suptitle(
    "WHY IMAGES NEED SOMETHING SPECIAL",
    fontsize=28,
    color=WHITE,
    fontweight="bold",
    y=0.96
)


message = ax.text(
    7.5,
    0.55,
    "",
    ha="center",
    fontsize=18,
    color=YELLOW,
    fontweight="bold"
)


# ============================================================
# IMAGE GRID
# ============================================================

grid_x0 = 1.0
grid_y0 = 2.0

grid_size = 4.0

image_box = Rectangle(
    (
        grid_x0,
        grid_y0
    ),
    grid_size,
    grid_size,
    edgecolor=WHITE,
    facecolor="#172033",
    linewidth=2.5
)

ax.add_patch(
    image_box
)


ax.text(
    3.0,
    6.45,
    "IMAGE",
    ha="center",
    fontsize=17,
    color=WHITE,
    fontweight="bold"
)


# ============================================================
# MANY OUTPUT NEURONS
# ============================================================

neurons = []

for i in range(
    7
):

    y = (
        1.7
        +
        i * 0.72
    )

    circle = Circle(
        (
            11.5,
            y
        ),
        0.28,
        facecolor="#203052",
        edgecolor=BLUE,
        linewidth=2
    )

    ax.add_patch(
        circle
    )

    neurons.append(
        circle
    )


# ============================================================
# CONNECTIONS
# ============================================================

connections = []

sample_points = []

for r in range(
    5
):

    for c in range(
        5
    ):

        px = (
            grid_x0
            +
            0.4
            +
            c * 0.8
        )

        py = (
            grid_y0
            +
            0.4
            +
            r * 0.8
        )

        sample_points.append(
            (px, py)
        )


for px, py in sample_points:

    for neuron in neurons:

        nx, ny = neuron.center

        line, = ax.plot(
            [
                px,
                nx - 0.3
            ],
            [
                py,
                ny
            ],
            color=MUTED,
            linewidth=0.5,
            alpha=0
        )

        connections.append(
            line
        )


parameter_text = ax.text(
    8.0,
    6.4,
    "",
    ha="center",
    fontsize=17,
    color=RED,
    fontweight="bold"
)


# ============================================================
# SHOW
# ============================================================

plt.show(block=False)

plt.pause(0.2)

maximize_window()

plt.pause(0.8)


# ============================================================
# FULLY CONNECTED EXPLOSION
# ============================================================

for frame in range(
    55
):

    t = frame / 54


    for line in connections:

        line.set_alpha(
            0.20 * t
        )


    parameter_text.set_text(
        "EVERY PIXEL → EVERY NEURON"
    )


    message.set_text(
        "With images, a fully connected network can require huge numbers of weights."
    )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


plt.pause(
    1.0
)


# ============================================================
# FADE CONNECTIONS AWAY
# ============================================================

for frame in range(
    40
):

    t = (
        1
        -
        frame / 39
    )


    for line in connections:

        line.set_alpha(
            0.20 * t
        )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


# ============================================================
# SMALL LOCAL FILTER
# ============================================================

filter_box = Rectangle(
    (
        grid_x0,
        grid_y0
    ),
    1.2,
    1.2,
    edgecolor=GREEN,
    facecolor="none",
    linewidth=4
)

ax.add_patch(
    filter_box
)


parameter_text.set_text(
    "WHAT IF WE LOOK LOCALLY?"
)


# ============================================================
# SLIDE FILTER ACROSS IMAGE
# ============================================================

positions = []

for row in range(
    4
):

    cols = range(4)

    if row % 2 == 1:
        cols = reversed(range(4))

    for col in cols:

        positions.append(
            (
                grid_x0
                +
                col * 0.9,

                grid_y0
                +
                row * 0.9
            )
        )


for target_x, target_y in positions:

    current_x, current_y = filter_box.get_xy()


    for frame in range(
        18
    ):

        t = (
            frame / 17
        )


        t = (
            t
            *
            t
            *
            (
                3
                -
                2*t
            )
        )


        x = (
            current_x
            *
            (1-t)
            +
            target_x
            *
            t
        )


        y = (
            current_y
            *
            (1-t)
            +
            target_y
            *
            t
        )


        filter_box.set_xy(
            (
                x,
                y
            )
        )


        message.set_text(
            "A small shared filter can scan local regions of the image."
        )


        fig.canvas.draw_idle()
        fig.canvas.flush_events()

        plt.pause(
            0.025
        )


# ============================================================
# FINAL
# ============================================================

parameter_text.set_text(
    "CONVOLUTION"
)


message.set_text(
    "NEXT EPISODE: CONVOLUTIONAL NEURAL NETWORKS"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()


while plt.fignum_exists(fig.number):

    fig.canvas.flush_events()

    plt.pause(0.05)