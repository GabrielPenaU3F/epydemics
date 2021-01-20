from matplotlib import pyplot as plt

from analyzers.contagion_fitter import ContagionFitter


class Plotter:

    def plot_data_vs_prediction(self, data, a, b):
        x = data.get_days()
        y = data.get_values()
        prediction = ContagionFitter().mean_value_function(x, a, b)
        fig, axes = plt.subplots()
        axes.plot(x, y, linewidth=1, color='#263859', linestyle='--',
                  label='Real data (' + data.get_country_name() + ')')
        axes.plot(x, prediction, linewidth=1, color='red', linestyle='-',
                  label='Model curve')

        self.format_plot(axes)
        plt.show()

    def format_plot(self, axes):
        self.config_axes_limits(axes)
        self.config_plot_background(axes)
        axes.legend()

    def config_axes_limits(self, axes):
        axes.set_xlim(left=0, auto=True)
        axes.set_ylim(bottom=0, auto=True)

    def config_plot_background(self, axes):
        axes.patch.set_facecolor("#ffffff")
        axes.patch.set_edgecolor('black')
        axes.patch.set_linewidth('1')
        axes.set_facecolor("#ffffff")
        axes.grid(color='black', linestyle='--', linewidth=0.5)

    def plot_parameters_over_time(self, data, a_params, b_params, start_from):
        x = data.get_days()[start_from:len(data.get_days())]
        fig, axes = plt.subplots(1, 2)
        axes[0].plot(x, a_params, linewidth=1, color='blue', linestyle='-',
                     label=data.get_country_name() + ', ρ over time')
        axes[1].plot(x, b_params, linewidth=1, color='green', linestyle='-',
                     label=data.get_country_name() + ', γ/ρ over time')
        self.format_plot(axes[0])
        self.format_plot(axes[1])
        plt.show()

    def plot_mtb(self, data, mtbs, start_from):
        x = data.get_days()[start_from:len(data.get_days())]
        fig, axes = plt.subplots()
        axes.plot(x, mtbs, linewidth=1, color='red', linestyle='-',
                  label='Mean time between occurrences')
        self.format_plot(axes)
        plt.show()
