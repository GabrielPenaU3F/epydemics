import numpy as np
from matplotlib import pyplot as plt, rc

from src.data_manipulation.data_manager import DataManager
from src.domain.unit_converter import DaysConverter

rc('font', **{'family': 'serif', 'serif': ['CMU Sans Serif']})
plt.rcParams['pdf.fonttype'] = 42


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
        axes.set_title(title)
        self.config_plot_background(axes)
        self.config_fit_plot_axis(axes, fit)
        axes.legend()

        plt.show()

    def plot_parameters_over_time(self, parameter_tuples, location, start_from):
        x_right_lim = start_from + len(parameter_tuples)
        x = np.arange(start_from, x_right_lim)
        rhos = [tup[0] for tup in parameter_tuples]
        gamma_per_rhos = [tup[1] for tup in parameter_tuples]

        fig, axes = plt.subplots(1, 2)
        rho_axes = axes[0]
        gamma_per_rho_axes = axes[1]
        rho_axes.plot(x, rhos, linewidth=1, color='#db6400', linestyle='-', label='\u03C1')
        rho_axes.set_title('\u03C1 over time (' + location + ')')
        gamma_per_rho_axes.plot(x, gamma_per_rhos, linewidth=1, color='#61b15a', linestyle='-', label='\u03B3 / \u03C1')
        gamma_per_rho_axes.set_title('\u03B3 / \u03C1 over time (' + location + ')')
        self.config_plot_background(rho_axes)
        self.config_plot_background(gamma_per_rho_axes)
        self.config_parameters_plot_axis(rho_axes, gamma_per_rho_axes)
        rho_axes.legend()
        gamma_per_rho_axes.legend()

        plt.show()

    def plot_mtbis(self, mtbis, location, start_from, plot_unit):

        converter = DaysConverter.get_instance()
        converted_mtbis = converter.convert_days_to(plot_unit, mtbis)

        x_right_lim = start_from + len(mtbis)
        x = np.arange(start_from, x_right_lim)

        fig, axes = plt.subplots()
        axes.plot(x, converted_mtbis, linewidth=1, color='#6F17A6', linestyle='-', label='MTBI')
        axes.set_title('Mean Time Between Infections (' + location + ')')
        self.config_plot_background(axes)
        self.config_mtbi_plot_axis(axes, plot_unit)
        axes.legend()
        plt.show()

    def plot_mtbi_inverses(self, mtbis, location, dataset, start_from, unit, real_data):

        converter = DaysConverter.get_instance()
        converted_mtbis = converter.convert_days_to(unit, mtbis)
        inverses = np.power(converted_mtbis, -1)

        x_right_lim = start_from + len(inverses)
        x = np.arange(start_from, x_right_lim)

        fig, axes = plt.subplots()
        axes.plot(x, inverses, linewidth=1, color='#6F17A6', linestyle='-', label='MTBI inverses')
        if real_data is True:
            data = DataManager.get_raw_incidence_data(location, dataset=dataset, start=start_from, end=x_right_lim-1)
            axes.plot(x, data, linewidth=1, color='#80BF60', linestyle='-', label='Incidence data')

        axes.set_title('MTBI inverses (' + location + ')')
        self.config_plot_background(axes)
        self.config_mtbi_plot_axis(axes, unit)
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

    def config_parameters_plot_axis(self, rho_axes, gamma_per_rho_axes):

        rho_axes.set_xlabel('t (days)')
        rho_axes.set_ylabel('\u03C1')
        self.config_axis_plain_style(rho_axes)

        gamma_per_rho_axes.set_xlabel('t (days)')
        gamma_per_rho_axes.set_ylabel('\u03B3 / \u03C1')
        self.config_axis_plain_style(gamma_per_rho_axes)

    def config_mtbi_plot_axis(self, axes, plot_unit):
        axes.set_xlabel('t (days)')
        axes.set_ylabel('MTBI (' + str(plot_unit) + ')')
        self.config_axis_plain_style(axes)

    def config_axis_plain_style(self, axes):
        axes.ticklabel_format(axis='x', style='plain')
        axes.ticklabel_format(axis='y', style='plain')
