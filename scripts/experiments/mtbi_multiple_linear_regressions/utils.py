import numpy as np
import pandas
import seaborn as sns
from matplotlib import pyplot as plt


def decode_points(points):
    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]
    return x, y, z


def scatterplot_m_K(points):

    m, K, values = decode_points(points)

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.scatter(m, K)
    for i, txt in enumerate(values):
        ax.annotate(str(txt) + ' %', (m[i], K[i]), fontsize=16)

    ax.set_title('Relative error', fontsize=32)
    ax.set_xticks(m)
    ax.set_yticks(K)
    ax.set_xlabel('m', fontsize=24, labelpad=15)
    ax.set_ylabel('K', fontsize=24, labelpad=15)

    plt.show()


def heatmap(points, title):
    df = pandas.DataFrame(points, columns=['x', 'y', 'z'])
    df = df.pivot(columns='x', index='y', values='z')
    df.index = df.index.astype(int)
    df.columns = df.columns.astype(int)
    df.sort_index(inplace=True)
    df.sort_index(axis=1, inplace=True)

    fig, ax = plt.subplots(figsize=(7, 8))
    sns.heatmap(df, linewidths=0.2, fmt='.4f', annot=True, annot_kws={'fontsize': 16}, cmap='flare', ax=ax)
    ax.invert_yaxis()
    ax.tick_params(axis='both', labelsize=18)
    ax.set_xlabel('m', fontsize=24, labelpad=15)
    ax.set_ylabel('K', fontsize=24, labelpad=15)
    ax.set_title(title, fontsize=32, pad=18)
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=18)
    plt.show()
