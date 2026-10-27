# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:29:23 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 5 - VISUALIZATION 6
# WHY DEPTH HELPS — FEATURE REUSE
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


BACKGROUND = "#090D18"

WHITE = "#F5F7FF"
BLUE = "#4D9FFF"
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


plt.close("all")

fig, ax = plt.subplots(
    figsize=(14, 8)
)

fig.patch.set_facecolor(
    BACKGROUND
)

ax.set_facecolor(
    BACKGROUND
)

ax.set_xlim(
    0,
    14
)

ax.set_ylim(
    0,
    8
)

ax.axis("off")


fig.suptitle(
    "WHY DEPTH HELPS: REUSE SIMPLE FEATURES",
    fontsize=27,
    color=WHITE,
    fontweight="bold",
    y=0.96
)


# ============================================================
# POSITIONS
# ============================================================

edge_pos = (
    2.5,
    4
)


corner1_pos = (
    6,
    5.3
)


corner2_pos = (
    6,
    2.7
)


shape1_pos = (
    10,
    5.3
)


shape2_pos = (
    10,
    2.7
)


def node(
    pos,
    label,
    color
):

    circle = Circle(
        pos,
        0.75,
        facecolor="#203052",
        edgecolor=color,
        linewidth=3
    )

    ax.add_patch(
        circle
    )

    ax.text(
        pos[0],
        pos[1],
        label,
        ha="center",
        va="center",
        fontsize=14,
        color=WHITE,
        fontweight="bold"
    )

    return circle


node(
    edge_pos,
    "EDGE",
    BLUE
)

node(
    corner1_pos,
    "CORNER A",
    YELLOW
)

node(
    corner2_pos,
    "CORNER B",
    YELLOW
)

node(
    shape1_pos,
    "SHAPE A",
    GREEN
)

node(
    shape2_pos,
    "SHAPE B",
    GREEN
)


pairs = [
    (edge_pos, corner1_pos),
    (edge_pos, corner2_pos),

    (corner1_pos, shape1_pos),
    (corner1_pos, shape2_pos),

    (corner2_pos, shape1_pos),
    (corner2_pos, shape2_pos)
]


lines = []


for start, end in pairs:

    line, = ax.plot(
        [
            start[0] + 0.75,
            end[0] - 0.75
        ],
        [
            start[1],
            end[1]
        ],
        color=MUTED,
        linewidth=2,
        alpha=0.3
    )

    lines.append(
        line
    )


message = ax.text(
    7,
    0.7,
    "",
    ha="center",
    fontsize=19,
    color=YELLOW,
    fontweight="bold"
)


plt.show(block=False)

plt.pause(0.2)

maximize_window()

plt.pause(0.8)


for i, line in enumerate(lines):

    for frame in range(
        30
    ):

        t = frame / 29

        line.set_alpha(
            0.3
            +
            0.7 * t
        )

        line.set_linewidth(
            2
            +
            3 * t
        )

        message.set_text(
            "One learned feature can contribute to many deeper features."
        )

        fig.canvas.draw_idle()
        fig.canvas.flush_events()

        plt.pause(
            PAUSE_TIME
        )

    line.set_linewidth(
        2.5
    )


message.set_text(
    "REUSE SIMPLE FEATURES  →  BUILD MANY COMPLEX FEATURES"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()


while plt.fignum_exists(fig.number):

    fig.canvas.flush_events()

    plt.pause(0.05)