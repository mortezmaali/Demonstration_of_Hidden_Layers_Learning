# -*- coding: utf-8 -*-

# ============================================================
# EPISODE 4 - VISUALIZATION 8
# GOING DEEPER
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

        if hasattr(
            manager,
            "window"
        ):

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


ax.axis(
    "off"
)


fig.suptitle(
    "FROM ONE HIDDEN LAYER TO DEEP NETWORKS",
    fontsize=27,
    color=WHITE,
    fontweight="bold",
    y=0.96
)


# ============================================================
# LAYERS
# ============================================================

layer_x = [
    1.5,
    4.5,
    7.5,
    10.5,
    13.5
]


layer_counts = [
    2,
    3,
    3,
    3,
    1
]


layer_names = [
    "RAW INPUT",
    "LAYER 1",
    "LAYER 2",
    "LAYER 3",
    "OUTPUT"
]


layer_descriptions = [
    "Original measurements",
    "Simple features",
    "Feature combinations",
    "More abstract representation",
    "Final decision"
]


layers = []


for x_pos, count in zip(
    layer_x,
    layer_counts
):

    if count == 1:

        ys = [
            4
        ]

    elif count == 2:

        ys = [
            5.2,
            2.8
        ]

    else:

        ys = [
            5.6,
            4.0,
            2.4
        ]


    current_layer = []


    for y_pos in ys:

        circle = Circle(
            (
                x_pos,
                y_pos
            ),
            0.42,
            facecolor="#203052",
            edgecolor=MUTED,
            linewidth=2.5,
            alpha=0
        )


        ax.add_patch(
            circle
        )


        current_layer.append(
            circle
        )


    layers.append(
        current_layer
    )


# ============================================================
# CONNECTIONS
# ============================================================

all_connections = []


for layer_index in range(
    len(layers) - 1
):

    current_lines = []


    for node_a in layers[
        layer_index
    ]:

        for node_b in layers[
            layer_index + 1
        ]:

            start = node_a.center

            end = node_b.center


            line, = ax.plot(
                [
                    start[0] + 0.42,
                    end[0] - 0.42
                ],
                [
                    start[1],
                    end[1]
                ],
                color=WHITE,
                linewidth=1.5,
                alpha=0
            )


            current_lines.append(
                line
            )


    all_connections.append(
        current_lines
    )


# ============================================================
# LABELS
# ============================================================

name_texts = []

description_texts = []


for x_pos, name, description in zip(
    layer_x,
    layer_names,
    layer_descriptions
):

    name_text = ax.text(
        x_pos,
        6.8,
        name,
        ha="center",
        fontsize=14,
        color=WHITE,
        fontweight="bold",
        alpha=0
    )


    desc_text = ax.text(
        x_pos,
        1.15,
        description,
        ha="center",
        fontsize=11,
        color=MUTED,
        alpha=0
    )


    name_texts.append(
        name_text
    )


    description_texts.append(
        desc_text
    )


message = ax.text(
    7.5,
    0.45,
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
# BUILD NETWORK
# ============================================================

for layer_index in range(
    len(layers)
):

    for frame in range(
        35
    ):

        t = (
            frame
            /
            34
        )


        for node in layers[
            layer_index
        ]:

            node.set_alpha(
                t
            )


            node.set_edgecolor(
                BLUE
                if layer_index == 0
                else YELLOW
                if layer_index < len(layers) - 1
                else GREEN
            )


        name_texts[
            layer_index
        ].set_alpha(
            t
        )


        description_texts[
            layer_index
        ].set_alpha(
            t
        )


        fig.canvas.draw_idle()
        fig.canvas.flush_events()

        plt.pause(
            PAUSE_TIME
        )


    if layer_index < len(
        all_connections
    ):

        for frame in range(
            30
        ):

            t = (
                frame
                /
                29
            )


            for line in all_connections[
                layer_index
            ]:

                line.set_alpha(
                    0.65
                    *
                    t
                )


            fig.canvas.draw_idle()
            fig.canvas.flush_events()

            plt.pause(
                PAUSE_TIME
            )


    if layer_index == 0:

        message.set_text(
            "Start with the raw input."
        )

    elif layer_index == 1:

        message.set_text(
            "The first hidden layer learns useful features."
        )

    elif layer_index == 2:

        message.set_text(
            "The next layer combines those features."
        )

    elif layer_index == 3:

        message.set_text(
            "Deeper layers build increasingly abstract representations."
        )

    else:

        message.set_text(
            "The final representation makes the decision easier."
        )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        0.8
    )


# ============================================================
# SIGNAL MOVES THROUGH NETWORK
# ============================================================

for layer_index in range(
    len(all_connections)
):

    for line in all_connections[
        layer_index
    ]:

        line.set_color(
            BLUE
        )

        line.set_linewidth(
            3
        )


    message.set_text(
        "REPRESENTATION → REPRESENTATION → REPRESENTATION"
    )


    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(
        0.8
    )


    for line in all_connections[
        layer_index
    ]:

        line.set_color(
            WHITE
        )

        line.set_linewidth(
            1.5
        )


message.set_text(
    "NEXT: WHAT DO DEEPER LAYERS ACTUALLY LEARN?"
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