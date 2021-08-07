import numpy as np
from matplotlib import pyplot as plt

from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep


def config_plot_background(axes):
    axes.patch.set_facecolor("#ffffff")
    axes.patch.set_edgecolor('black')
    axes.patch.set_linewidth('1')
    axes.set_facecolor("#ffffff")
    axes.grid(color='black', linestyle='--', linewidth=0.5)


def config_axis_plain_style(axes):
    axes.ticklabel_format(axis='x', style='plain')
    axes.ticklabel_format(axis='y', style='plain')


def config_spectrum_plot_axis(axes, xscale):
    config_axis_plain_style(axes)
    xticks = None
    xticklabels = None
    if xscale == 'rad':
        xticks = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi]
        xticklabels = ['0', r'$\pi$/4', r'$\pi$/2', r'3$\pi$/4', r'$\pi$']
        axes.set_xlabel('\u03C9 (rad/day)', fontsize=20, labelpad=15)
    elif xscale == 'freq':
        xticks = [0, 1/7, 2/7, 1/2]
        xticklabels = ['0', '1/7', '2/7', '1/2']
        axes.set_xlabel('Frequency (1/day)', fontsize=20, labelpad=15)
    axes.set_xticks(xticks)
    axes.set_xticklabels(xticklabels, fontsize=14)
    axes.tick_params(axis='y', which='major', labelsize=14)


def plot_spectrum(spectrum_mod, xscale):

    fig, axes = plt.subplots(figsize=(12, 8))

    spectrum_mod = spectrum_mod[:int(len(spectrum_mod) / 2)]
    if xscale == 'rad':
        w = np.linspace(0, np.pi, len(spectrum_mod), endpoint=None)
    elif xscale == 'freq':
        w = np.linspace(0, 1 / 2, len(spectrum_mod), endpoint=None)

    axes.plot(w, spectrum_mod, linewidth=1, color='#6F17A6', linestyle='-', label='Spectrum absolute value')

    config_spectrum_plot_axis(axes, xscale)
    config_plot_background(axes)
    axes.legend(loc='upper right', prop={'size': 20})
    plt.show()


DataManager.load_dataset('owid')

ar_spectrum = np.abs(ep.show_daily_data_spectrum('Argentina', end=515, output=False))
br_spectrum = np.abs(ep.show_daily_data_spectrum('Brazil', end=515, output=False))
plot_spectrum(ar_spectrum, xscale='freq')
plot_spectrum(br_spectrum, xscale='freq')
