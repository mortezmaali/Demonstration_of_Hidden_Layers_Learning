# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:28:34 2026

@author: Morteza
"""

# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 5 - VISUALIZATION 5
# THE FEATURE HIERARCHY
# ============================================================

from IPython import get_ipython

ipython = get_ipython()

if ipython is not None:
    ipython.run_line_magic("matplotlib", "qt")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


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
    "A HIERARCHY OF LEARNED REPRESENTATIONS",
    fontsize=28,
    color=WHITE,
    fontweight="bold",
    y=0.96
)


labels = [
    "PIXELS",
    "EDGES",
    "CORNERS /\nTEXTURES",
    "SHAPES /\nPARTS",
    "HIGHER-LEVEL\nREPRESENTATION"
]


x_positions = [
    1.7,
    4.5,
    7.4,
    10.3,
    13.2
]


colors = [
    BLUE,
    BLUE,
    YELLOW,
    YELLOW,
    GREEN
]


boxes = []
texts = []
arrows = []


for x, label, color in zip(
    x_positions,
    labels,
    colors
):

    box = FancyBboxPatch(
        (x-1.0, 3.1),
        2.0,
        1.5,
        boxstyle="round,pad=0.05,rounding_size=0.15",
        edgecolor=color,
        facecolor="#101827",
        linewidth=3,
        alpha=0
    )

    ax.add_patch(
        box
    )

    text = ax.text(
        x,
        3.85,
        label,
        ha="center",
        va="center",
        fontsize=15,
        color=WHITE,
        fontweight="bold",
        alpha=0
    )

    boxes.append(
        box
    )

    texts.append(
        text
    )


for i in range(
    len(x_positions)-1
):

    arrow = ax.annotate(
        "",
        xy=(
            x_positions[i+1]-1.05,
            3.85
        ),
        xytext=(
            x_positions[i]+1.05,
            3.85
        ),
        arrowprops=dict(
            arrowstyle="->",
            color=WHITE,
            linewidth=3,
            alpha=0
        )
    )

    arrows.append(
        arrow
    )


message = ax.text(
    7.5,
    1.1,
    "",
    ha="center",
    fontsize=19,
    color=YELLOW,
    fontweight="bold"
)


plt.show(block=False)

plt.pause(0.2)

maximize_window()

plt.pause(0.7)


for i in range(
    len(boxes)
):

    for frame in range(
        35
    ):

        t = frame / 34

        boxes[i].set_alpha(
            t
        )

        texts[i].set_alpha(
            t
        )

        fig.canvas.draw_idle()
        fig.canvas.flush_events()

        plt.pause(
            PAUSE_TIME
        )

    if i < len(arrows):

        arrows[i].arrow_patch.set_alpha(
            1
        )

    if i == 0:

        message.set_text(
            "Start with raw pixel values."
        )

    elif i == 1:

        message.set_text(
            "Early layers can capture simple local structure."
        )

    elif i == 2:

        message.set_text(
            "Later layers combine earlier features."
        )

    elif i == 3:

        message.set_text(
            "The representation becomes richer."
        )

    else:

        message.set_text(
            "Deeper layers can support increasingly complex decisions."
        )

    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        0.7
    )


message.set_text(
    "DEEPER LAYERS DON'T START OVER — THEY BUILD ON EARLIER FEATURES"
)


fig.canvas.draw_idle()
fig.canvas.flush_events()


while plt.fignum_exists(fig.number):

    fig.canvas.flush_events()

    plt.pause(0.05)