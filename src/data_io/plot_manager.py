import numpy as np
from matplotlib import pyplot as plt, rc

from src.data_manipulation.data_manager import DataManager
from src.domain.unit_converter import DaysConverter

rc('font', **{'family': 'serif', 'serif': ['Arial']})
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

    def plot_fit_results(self, fit, location, dataset):
        source = DataManager.get_data_source()
        dataset = DataManager.choose_dataset(dataset)

        x = fit.get_x_data()
        real_data = fit.get_y_data()
        explained = fit.get_explained_data()
        title = source.get_dataset_title(dataset) + ' in ' + location

        fig, axes = plt.subplots()
        axes.plot(x, real_data, linewidth=1, color='#263859', linestyle='--', label='Real data')
        axes.plot(x, explained, linewidth=1, color='#ca3e47', linestyle='-', label='Model prediction')
        axes.set_title(title)
        self.config_plot_background(axes)
        self.config_fit_plot_axis(axes, fit, dataset)
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

    def plot_mtbi_inverses(self, mtbis, location, dataset, start, real_data):

        inverses = np.power(mtbis, -1)

        x_left_lim = start - 1
        x_right_lim = x_left_lim + len(inverses)
        x = np.arange(x_left_lim, x_right_lim)

        fig, axes = plt.subplots()
        axes.plot(x, inverses, linewidth=1, color='#6F17A6', linestyle='-', label='MTBI inverses')
        if real_data is True:
            data = DataManager.get_raw_daily_data(location, dataset=dataset,
                                                  start=x_left_lim, end=x_right_lim - 1)
            axes.plot(x, data, linewidth=1, color='#80BF60', linestyle='-', label='Daily data')

        axes.set_title('MTBI inverses (' + location + ')')
        self.config_plot_background(axes)
        self.config_mtbi_plot_axis(axes, 'day')
        axes.legend()
        plt.show()

    def plot_fit_residuals(self, residuals, location, dataset):
        source = DataManager.get_data_source()
        dataset = DataManager.choose_dataset(dataset)
        dataset_title = source.get_dataset_title(dataset)
        title = dataset_title + ' in ' + location + ', fit_model residuals'
        x = np.arange(1, len(residuals) + 1)

        fig, axes = plt.subplots()
        axes.plot(x, residuals, linewidth=1, color='#9A0619', linestyle='-', label='Residuals')
        axes.set_title(title)
        self.config_plot_background(axes)
        self.config_fit_residuals_axis(axes)
        axes.legend()

        plt.show()

    def plot_last_residual_over_time(self, residuals, location, start_from):
        x_right_lim = start_from + len(residuals)
        x = np.arange(start_from, x_right_lim)

        fig, axes = plt.subplots()
        axes.plot(x, residuals, linewidth=1, color='#9A0619', linestyle='-', label='Last residual over time')
        axes.set_title('Fit residuals over time (' + location + ')')
        self.config_plot_background(axes)
        self.config_axis_plain_style(axes)
        axes.legend()

        plt.show()

    def plot_cumulative_data(self, raw_data, location, dataset):
        source = DataManager.get_data_source()
        dataset = DataManager.choose_dataset(dataset)
        title = source.get_dataset_datacurve_title(dataset, 'cumulative') + ' curve (' + location + ')'
        label = source.get_dataset_datacurve_ylabel(dataset, 'cumulative')
        self.plot_data(raw_data, title, label)

    def plot_daily_data(self, raw_data, location, dataset):
        source = DataManager.get_data_source()
        dataset = DataManager.choose_dataset(dataset)
        title = source.get_dataset_datacurve_title(dataset, 'daily') + ' curve (' + location + ')'
        label = source.get_dataset_datacurve_ylabel(dataset, 'daily')
        self.plot_data(raw_data, title, label)

    def plot_data(self, raw_data, title, label):
        x = np.arange(1, len(raw_data) + 1)
        fig, axes = plt.subplots()
        axes.plot(x, raw_data, linewidth=1, color='#6F17A6', linestyle='-', label=label)
        axes.set_title(title)
        self.config_plot_background(axes)
        self.config_axis_plain_style(axes)
        axes.legend()
        plt.show()

    def plot_daily_data_spectrum(self, spectrum_mod, location, xscale):

        fig, axes = plt.subplots()

        spectrum_mod = spectrum_mod[:int(len(spectrum_mod)/2)]
        if xscale == 'rad':
            w = np.linspace(0, np.pi, len(spectrum_mod), endpoint=None)
        elif xscale == 'freq':
            w = np.linspace(0, 1/2, len(spectrum_mod), endpoint=None)

        axes.plot(w, spectrum_mod,  linewidth=1, color='#6F17A6', linestyle='-', label='Spectrum absolute value')
        axes.set_title('Spectrum absolute value (' + location + ')')

        self.config_spectrum_plot_axis(axes, xscale)
        self.config_plot_background(axes)
        axes.legend()
        plt.show()

    def config_plot_background(self, axes):
        axes.patch.set_facecolor("#ffffff")
        axes.patch.set_edgecolor('black')
        axes.patch.set_linewidth('1')
        axes.set_facecolor("#ffffff")
        axes.grid(color='black', linestyle='--', linewidth=0.5)

    def config_fit_plot_axis(self, axes, fit, dataset):
        source = DataManager.get_data_source()
        axes.set_xlabel('t (days)')
        axes.set_ylabel(source.get_fit_plot_ylabel(dataset))
        self.config_axis_plain_style(axes)

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

    def config_spectrum_plot_axis(self, axes, xscale):
        self.config_axis_plain_style(axes)
        xticks = None
        xticklabels = None
        if xscale == 'rad':
            xticks = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi]
            xticklabels = ['0', r'$\pi$/4', r'$\pi$/2', r'3$\pi$/4', r'$\pi$']
            axes.set_xlabel('\u03C9 (rad/day)')
        elif xscale == 'freq':
            xticks = [0, 1/8, 1/4, 3/8, 1/2]
            xticklabels = ['0', '1/8', '1/4', '3/8', '1/2']
            axes.set_xlabel('f (1/day)')
        axes.set_xticks(xticks)
        axes.set_xticklabels(xticklabels)

        axes.set_xticks(xticks)
        axes.set_xticklabels(xticklabels, fontsize=10)

    def config_fit_residuals_axis(self, axes):
        axes.set_xlabel('t (days)')
        axes.set_ylabel('Residuals')
        self.config_axis_plain_style(axes)
