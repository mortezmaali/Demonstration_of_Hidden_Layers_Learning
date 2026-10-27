# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 4 - VISUALIZATION 4
# INPUT SPACE -> HIDDEN SPACE
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

MUTED = "#A8B2C7"
GRID = "#33405A"

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


# Example point
x1 = -1.0
x2 = 1.0


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


# ============================================================
# FIGURE
# ============================================================

plt.close("all")


fig, (
    ax_left,
    ax_right
) = plt.subplots(
    1,
    2,
    figsize=(14, 7)
)


fig.patch.set_facecolor(
    BACKGROUND
)


for ax in [
    ax_left,
    ax_right
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
# LEFT
# ============================================================

ax_left.set_xlim(
    -1.6,
    1.6
)


ax_left.set_ylim(
    -1.6,
    1.6
)


ax_left.set_xlabel(
    r"$x_1$",
    color=WHITE,
    fontsize=15
)


ax_left.set_ylabel(
    r"$x_2$",
    color=WHITE,
    fontsize=15
)


ax_left.set_title(
    "INPUT SPACE",
    color=WHITE,
    fontsize=20
)


ax_left.scatter(
    [x1],
    [x2],
    s=500,
    color=BLUE,
    edgecolor=YELLOW,
    linewidth=4
)


ax_left.text(
    x1 + 0.15,
    x2 + 0.15,
    f"({x1:.1f}, {x2:.1f})",
    fontsize=15,
    color=YELLOW,
    fontweight="bold"
)


# ============================================================
# RIGHT
# ============================================================

ax_right.set_xlim(
    -0.05,
    1.05
)


ax_right.set_ylim(
    -0.05,
    1.05
)


ax_right.set_xlabel(
    r"$h_1$",
    color=WHITE,
    fontsize=15
)


ax_right.set_ylabel(
    r"$h_2$",
    color=WHITE,
    fontsize=15
)


ax_right.set_title(
    "HIDDEN FEATURE SPACE",
    color=WHITE,
    fontsize=20
)


hidden_point = ax_right.scatter(
    [],
    [],
    s=500,
    color=BLUE,
    edgecolor=YELLOW,
    linewidth=4
)


hidden_text = ax_right.text(
    0.50,
    0.15,
    "",
    transform=ax_right.transAxes,
    ha="center",
    fontsize=16,
    color=YELLOW,
    fontweight="bold"
)


fig.text(
    0.5,
    0.52,
    "→",
    ha="center",
    va="center",
    fontsize=45,
    color=WHITE
)


fig.text(
    0.5,
    0.43,
    "HIDDEN LAYER",
    ha="center",
    fontsize=14,
    color=MUTED,
    fontweight="bold"
)


fig.suptitle(
    "THE HIDDEN RESPONSES BECOME NEW COORDINATES",
    fontsize=25,
    color=WHITE,
    fontweight="bold",
    y=0.96
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
# ANIMATE
# ============================================================

for frame in range(
    70
):

    t = (
        frame
        /
        69
    )


    current_h1 = (
        t * h1
    )


    current_h2 = (
        t * h2
    )


    hidden_point.set_offsets(
        [
            [
                current_h1,
                current_h2
            ]
        ]
    )


    hidden_text.set_text(
        f"h₁ = {current_h1:.3f}\n"
        f"h₂ = {current_h2:.3f}"
    )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        PAUSE_TIME
    )


hidden_text.set_text(
    f"({x1:.1f}, {x2:.1f})"
    f"  →  "
    f"({h1:.3f}, {h2:.3f})"
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