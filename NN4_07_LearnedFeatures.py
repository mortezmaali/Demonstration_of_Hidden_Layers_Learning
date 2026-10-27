# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 4 - VISUALIZATION 7
# WHAT DID THE HIDDEN LAYER LEARN?
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


BACKGROUND = "#090D18"

WHITE = "#F5F7FF"
BLUE = "#4D9FFF"
RED = "#FF5369"

YELLOW = "#FFD166"
GREEN = "#54E3A4"

MUTED = "#A8B2C7"

PAUSE_TIME = 0.04


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

    return (
        1
        /
        (
            1
            +
            np.exp(-z)
        )
    )


examples = [
    (-1.0, -1.0, 0),
    (-1.0, 1.0, 1),
    (1.0, -1.0, 1),
    (1.0, 1.0, 0)
]


# ============================================================
# FIGURE
# ============================================================

plt.close("all")


fig, ax = plt.subplots(
    figsize=(13, 7)
)


fig.patch.set_facecolor(
    BACKGROUND
)


ax.set_facecolor(
    BACKGROUND
)


ax.set_xlim(
    0,
    13
)


ax.set_ylim(
    0,
    7
)


ax.axis(
    "off"
)


fig.suptitle(
    "WHAT DID THE HIDDEN LAYER ACTUALLY LEARN?",
    fontsize=26,
    color=WHITE,
    fontweight="bold",
    y=0.95
)


# ============================================================
# INPUT
# ============================================================

point_display = ax.scatter(
    [2.0],
    [3.7],
    s=1100,
    color=BLUE,
    edgecolor=WHITE,
    linewidth=3
)


input_text = ax.text(
    2,
    2.25,
    "",
    ha="center",
    fontsize=18,
    color=WHITE
)


# ============================================================
# FEATURE BARS
# ============================================================

ax.text(
    6,
    5.8,
    "LEARNED FEATURES",
    ha="center",
    fontsize=18,
    color=YELLOW,
    fontweight="bold"
)


bar1_bg = Rectangle(
    (4.2, 4.3),
    3.6,
    0.55,
    facecolor="#203052",
    edgecolor=WHITE,
    linewidth=1.5
)


bar2_bg = Rectangle(
    (4.2, 2.8),
    3.6,
    0.55,
    facecolor="#203052",
    edgecolor=WHITE,
    linewidth=1.5
)


ax.add_patch(
    bar1_bg
)


ax.add_patch(
    bar2_bg
)


bar1 = Rectangle(
    (4.2, 4.3),
    0,
    0.55,
    facecolor=YELLOW
)


bar2 = Rectangle(
    (4.2, 2.8),
    0,
    0.55,
    facecolor=GREEN
)


ax.add_patch(
    bar1
)


ax.add_patch(
    bar2
)


h1_text = ax.text(
    8.1,
    4.55,
    "",
    va="center",
    fontsize=16,
    color=YELLOW
)


h2_text = ax.text(
    8.1,
    3.05,
    "",
    va="center",
    fontsize=16,
    color=GREEN
)


ax.text(
    3.8,
    4.55,
    "h₁",
    ha="right",
    va="center",
    fontsize=19,
    color=YELLOW
)


ax.text(
    3.8,
    3.05,
    "h₂",
    ha="right",
    va="center",
    fontsize=19,
    color=GREEN
)


message = ax.text(
    6.5,
    0.75,
    "Hidden neurons turn the original inputs into useful learned features.",
    ha="center",
    fontsize=18,
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
    0.7
)


# ============================================================
# CYCLE THROUGH POINTS
# ============================================================

for x1, x2, class_value in examples:

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


    target_color = (
        BLUE
        if class_value == 1
        else RED
    )


    point_display.set_facecolor(
        target_color
    )


    input_text.set_text(
        f"Input\n"
        f"x₁ = {x1:+.1f}\n"
        f"x₂ = {x2:+.1f}\n\n"
        f"{'BLUE' if class_value == 1 else 'RED'}"
    )


    for frame in range(
        55
    ):

        t = (
            frame
            /
            54
        )


        t = (
            t
            *
            t
            *
            (
                3
                -
                2 * t
            )
        )


        bar1.set_width(
            3.6
            *
            h1
            *
            t
        )


        bar2.set_width(
            3.6
            *
            h2
            *
            t
        )


        h1_text.set_text(
            f"{h1*t:.3f}"
        )


        h2_text.set_text(
            f"{h2*t:.3f}"
        )


        fig.canvas.draw_idle()
        fig.canvas.flush_events()

        plt.pause(
            PAUSE_TIME
        )


    plt.pause(
        0.8
    )


    bar1.set_width(
        0
    )


    bar2.set_width(
        0
    )


message.set_text(
    "THE HIDDEN LAYER LEARNS A NEW REPRESENTATION OF THE DATA"
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