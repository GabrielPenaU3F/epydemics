from matplotlib import pyplot as plt

from src.strings_manager import StringManager


class PlotManager:

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = PlotManager()
        return cls.instance

    def __init__(self):
        pass

    def plot_fit_results(self, fit):
        x = fit.get_x_data()
        real_data = fit.get_y_data()
        explained = fit.get_explained_data()
        dataset_type = fit.get_dataset_type()
        country = fit.get_country()
        title = StringManager.get_dataset_title(dataset_type) + country

        fig, axes = plt.subplots()
        axes.plot(x, real_data, linewidth=1, color='#263859', linestyle='--', label='Real data')
        axes.plot(x, explained, linewidth=1, color='#ca3e47', linestyle='-', label='Model prediction')
        self.config_plot_background(axes)
        self.config_plot_axis(axes, fit)
        axes.set_title(title)
        axes.legend()

        plt.show()

    def config_plot_background(self, axes):
        axes.patch.set_facecolor("#ffffff")
        axes.patch.set_edgecolor('black')
        axes.patch.set_linewidth('1')
        axes.set_facecolor("#ffffff")
        axes.grid(color='black', linestyle='--', linewidth=0.5)

    def config_plot_axis(self, axes, fit):
        dataset = fit.get_dataset_type()
        axes.set_xlabel('t (days)')
        axes.set_ylabel(StringManager.get_fit_plot_ylabel(dataset))
        axes.ticklabel_format(axis='x', style='plain')
        axes.ticklabel_format(axis='y', style='plain')
