from src.data_io.plot_manager import PlotManager


def config_regular_plot_structure(axes, legend_loc=None):
    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.tick_params(axis='both', which='major', labelsize=24)

    if legend_loc is not None:
        axes.legend(loc=legend_loc, prop={'size': 32})
