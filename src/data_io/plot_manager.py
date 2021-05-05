import numpy as np
from matplotlib import pyplot as plt

from src.unit_converter import DaysConverter


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
        location = fit.get_location()
        source = fit.get_source()
        title = source.get_dataset_title(dataset_type) + ' in ' + location

        fig, axes = plt.subplots()
        axes.plot(x, real_data, linewidth=1, color='#263859', linestyle='--', label='Real data')
        axes.plot(x, explained, linewidth=1, color='#ca3e47', linestyle='-', label='Model prediction')
        self.config_plot_background(axes)
        self.config_fit_plot_axis(axes, fit)
        axes.set_title(title)
        axes.legend()

        plt.show()

    def plot_parameters_over_time(self, parameter_tuples, start_from):
        x_right_lim = start_from + len(parameter_tuples)
        x = np.arange(start_from, x_right_lim)
        rhos = [tup[0] for tup in parameter_tuples]
        gamma_by_rhos = [tup[1] for tup in parameter_tuples]

        fig, axes = plt.subplots(1, 2)
        rho_axes = axes[0]
        gamma_by_rho_axes = axes[1]
        rho_axes.plot(x, rhos, linewidth=1, color='#db6400', linestyle='-', label='\u03C1')
        gamma_by_rho_axes.plot(x, gamma_by_rhos, linewidth=1, color='#61b15a', linestyle='-', label='\u03B3 / \u03C1')
        self.config_plot_background(rho_axes)
        self.config_plot_background(gamma_by_rho_axes)
        self.config_parameters_plot_axis(rho_axes, gamma_by_rho_axes)
        rho_axes.legend()
        gamma_by_rho_axes.legend()

        plt.show()

    def plot_mtbis(self, mtbis, start_from, plot_unit):

        converter = DaysConverter.get_instance()
        converted_mtbis = converter.convert_days_to(plot_unit, mtbis)

        x_right_lim = start_from + len(mtbis)
        x = np.arange(start_from, x_right_lim)

        fig, axes = plt.subplots()
        axes.plot(x, converted_mtbis, linewidth=1, color='#db6400', linestyle='-', label='MTBI')
        self.config_plot_background(axes)
        self.config_mtbi_plot_axis(axes, plot_unit)
        axes.legend()
        plt.show()

    def config_plot_background(self, axes):
        axes.patch.set_facecolor("#ffffff")
        axes.patch.set_edgecolor('black')
        axes.patch.set_linewidth('1')
        axes.set_facecolor("#ffffff")
        axes.grid(color='black', linestyle='--', linewidth=0.5)

    def config_fit_plot_axis(self, axes, fit):
        dataset = fit.get_dataset_type()
        source = fit.get_source()
        axes.set_xlabel('t (days)')
        axes.set_ylabel(source.get_fit_plot_ylabel(dataset))
        axes.ticklabel_format(axis='x', style='plain')
        axes.ticklabel_format(axis='y', style='plain')

    def config_parameters_plot_axis(self, rho_axes, gamma_by_rho_axes):
        rho_axes.set_xlabel('t (days)')
        rho_axes.set_ylabel('\u03C1')
        self.config_axis_plain_style(rho_axes)

        gamma_by_rho_axes.set_xlabel('t (days)')
        gamma_by_rho_axes.set_ylabel('\u03B3 / \u03C1')
        self.config_axis_plain_style(gamma_by_rho_axes)

    def config_mtbi_plot_axis(self, axes, plot_unit):
        axes.set_xlabel('t (days)')
        axes.set_ylabel('MTBI (' + str(plot_unit) + ')')
        self.config_axis_plain_style(axes)

    def config_axis_plain_style(self, axes):
        axes.ticklabel_format(axis='x', style='plain')
        axes.ticklabel_format(axis='y', style='plain')
