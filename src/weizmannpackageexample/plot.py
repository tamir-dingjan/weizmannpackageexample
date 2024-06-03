import os

import numpy as np
from matplotlib import pyplot as plt
from ipywidgets import widgets


# plot the scores
class PlotScores:
    def __init__(self, all_scores, opts):
        self.all_scores = all_scores
        self.opts = opts
        self.mouse = widgets.Dropdown(
            options=["all", *opts["mice"]], description="Mouse:"
        )
        self.mouse.observe(self.plot, names="value")
        self.plot()

    def plot(self, *args):
        plt.cla()
        clusters_range = np.arange(2, 2 + len(list(self.all_scores.values())[0]))
        if self.mouse.value == "all":
            scores = [self.all_scores[mouse] for mouse in self.opts["mice"]]
            plt.errorbar(
                clusters_range,
                np.mean(scores, axis=0),
                yerr=np.std(scores, axis=0) / np.sqrt(len(self.opts["mice"])),
                label="all",
                color="tab:blue",
            )
            [
                plt.plot(
                    clusters_range,
                    self.all_scores[mouse],
                    alpha=0.25,
                    label=mouse,
                    color="tab:blue",
                )
                for mouse in self.opts["mice"]
            ]
        else:
            plt.plot(
                clusters_range,
                self.all_scores[self.mouse.value],
                label=self.mouse.value,
            )
        plt.xlabel("Num. clusters")
        plt.ylabel("Silhouette score")
        # add bottom
        plt.subplots_adjust(bottom=0.15)
        # save figure
        plt.savefig(os.path.join(self.opts["results_dir"], "scores_plot.svg"))
