import numpy as np
from matplotlib import pyplot as plt

from scripts.experiments.countries_feature_selection.codigo_original_2021.useful_functions import get_full_dataframe

full_df = get_full_dataframe()
df = full_df[full_df['location'] == 'United States']
df = df[df['new_cases'].notna()]
df = df.drop(columns=['new_deaths'])
data = df['new_cases'].to_numpy()

spectrum = np.abs(np.fft.fft(data))
spectrum = spectrum[:int(len(spectrum) / 2)]

fig, axes = plt.subplots(figsize=(8, 5))
f = np.linspace(0, 1 / 2, len(spectrum), endpoint=None)

axes.plot(f, spectrum, linestyle='-', linewidth=1, color='#6F17A6', label='Spectrum absolute value')
xticks = [0, 1/7, 2/7, 3/7, 1/2]
xticklabels = ['0', '1/7', '2/7', '3/7', '1/2']
axes.set_xlabel('Frequency (1/day)', fontsize=14, labelpad=15)
axes.set_xticks(xticks)
axes.set_xticklabels(xticklabels)
axes.yaxis.get_offset_text().set_fontsize(16)
axes.set_title('United States (spectrum)', fontsize=20)
axes.grid(linewidth=0.3)
axes.legend(loc='upper right', fontsize=16)
fig.tight_layout()
plt.show()

fig_filename = \
    'E:/Universidad/Investigación/Coronavirus/SeleccionAtributos/resources/results/figs_publication/fig_usa_spectrum.png'
fig.savefig(fig_filename)
