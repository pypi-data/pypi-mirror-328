import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import colors as mcolors

plt_markers: list[str] = list(Line2D.markers.keys())
# remove ',' from the list of markers
plt_markers.remove(',')
# remove 'o' from the list of markers
plt_markers.remove('o')


def lionplot(
    x: np.ndarray,
    y: np.ndarray,
    yerr: np.ndarray,
    ax: plt.Axes,
    hue_values: np.ndarray | None = None,
    elinewidth: int = 30,
    markersize: int = 10,
) -> None:

    x = np.asarray(x)
    y = np.asarray(y)
    yerr = np.asarray(yerr)
    hue_values = np.asarray(hue_values) if hue_values is not None else np.array([])

    # TODO: handle arbitrary length of hue_values
    colors: list[tuple[float, float, float]] = [mcolors.to_rgb(color) for color in plt.rcParams['axes.prop_cycle'].by_key()['color']]

    unique_category_vals = np.unique(hue_values)
    for i, category_val in enumerate(unique_category_vals):
        subset_x = x[hue_values == category_val]
        subset_y = y[hue_values == category_val]
        subset_yerr = yerr[hue_values == category_val]

        ax.errorbar(
            x=subset_x,
            y=subset_y,
            yerr=subset_yerr,
            label=category_val if len(unique_category_vals) > 0 else None,
            elinewidth=elinewidth,
            linestyle="none",
            markersize=markersize,
            marker=plt_markers[i],
            color=colors[i],
            ecolor=(*colors[i], 0.3),
        )
    return ax
    # else:
    #     ax.errorbar(
    #         x=[
    #             "_".join(el)
    #             for el in cliff_deltas.loc[IndexSlice[component, :], :].index
    #         ],
    #         y=values,
    #         yerr=(lower_bounds, upper_bounds),
    #         label=custom_label,
    #         elinewidth=elinewidth,
    #         linestyle="none",
    #         markersize=markersize,
    #         marker=".",
    #         color=color,
    #         ecolor=(*color, 0.3),
    #     )
