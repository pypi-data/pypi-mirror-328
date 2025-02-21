"""
Library of color schemes for Plotter.
"""

# grey background of the subplots
color_background = "rgb(245,245,245)"

color_grid = "white"

color_dashline = "#555555"

# for continuous data, neutral color in mid-range
color_divergent_centered = [
    (0.0, "rgb(255,120,90)"),  # red
    (0.25, "rgb(255,200,100)"),
    (0.5, "rgb(240,240,230)"),  # neutral
    (0.65, "rgb(90,190,210)"),
    (0.8, "rgb(70,110,160)"),
    (1.0, "rgb(100,50,100)"),  # navy
]
color_divergent_reds_only = [((0.5 - position) * 2, color) for position, color in color_divergent_centered[:3]]
color_divergent_reds_only.sort(key=lambda x: x[0])
color_divergent_blues_only = [((position - 0.5) * 2, color) for position, color in color_divergent_centered[2:]]


# for continuous data
color_divergent_asymmetric = [(0.0, "rgb(255,200,100)"), (0.25, "rgb(240,240,230)"), (0.5, "rgb(90,190,210)"), (0.75, "rgb(70,110,160)"), (1.0, "rgb(100,50,100)")]

# for contour plots
color_mono_blues = [(0.0, color_background), (0.3, "rgb(90,190,210)"), (0.6, "rgb(70,110,160)"), (1.0, "rgb(100,50,100)")]


color_mono_grey = [(0.0, "rgb(245,245,245)"), (1.0, "rgb(100,100,100)")]

# for categorical data
color_qualitative10 = ["#643264", "#5abed2", "#466ea0", "#ffc864", "#ff785a", "#8ce6e6", "#5aa0a0", "#aa50a0", "#eb5a64", "#aad8c3"]

# used by evaluation plots for training and design errors
color_evalerrors = {
    "x_err": {"main": "rgb(90,190,210)", "sec": "rgb(90,190,210)"},
    "y_err": {"main": "rgb(100,50,100)", "sec": "rgb(100,50,100)"},
    "de": {"main": "rgb(90,190,210)", "sec": "rgb(90,190,210)"},
    "de_s": {"main": "rgb(70,110,160)", "sec": "rgb(70,110,160)"},
}

# used by training evaluation plots that distinguish between train, val, and test data
color_datasplit = {"train": "#999999", "val": "#bbbbbb", "test": "#dddddd"}


def apply_default_style(fig):
    fig.update_layout(plot_bgcolor=color_background, paper_bgcolor="white")
    axis_kwargs = dict(mirror=True, ticks="outside", showline=False, gridcolor=color_grid, linecolor="black")
    fig.update_xaxes(**axis_kwargs)
    fig.update_yaxes(**axis_kwargs)
