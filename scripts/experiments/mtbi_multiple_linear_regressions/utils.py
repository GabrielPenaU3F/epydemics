import numpy as np
import pandas
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats as st
from statsmodels.stats import diagnostic as diag


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


def create_heatmap(ax, points, title):
    df = pandas.DataFrame(points, columns=['x', 'y', 'z'])
    df = df.pivot(columns='x', index='y', values='z')
    df.index = df.index.astype(int)
    df.columns = df.columns.astype(int)
    df.sort_index(inplace=True)
    df.sort_index(axis=1, inplace=True)

    sns.heatmap(df, linewidths=0.2, fmt='.4f', annot=True, annot_kws={'fontsize': 16},
                cmap='flare', ax=ax)
    ax.invert_yaxis()
    ax.tick_params(axis='both', labelsize=18)
    ax.set_xlabel('m', fontsize=24, labelpad=15)
    ax.set_ylabel('K', fontsize=24, labelpad=15)
    ax.set_title(title, fontsize=32, pad=18)
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=18, direction='in', width=0)


def heatmap(points, title):
    fig, ax = plt.subplots(figsize=(7, 8))
    create_heatmap(ax, points, title)
    plt.show()


def coef_barplot(coefs):
    fig, ax = plt.subplots(figsize=(9, 8))
    coefs = np.array(list(map(float, coefs)))
    labels = [r'$a_{' + str(i) + '}$' for i in range(len(coefs))]
    ax.bar(labels, coefs, bottom=0, color='#000285', width=0.3)
    ax.axhline(0, linewidth=1.5, color='black')
    ax.set_title('Regression coefficients', fontsize=32, pad=18)
    ax.tick_params(axis='both', labelsize=18)
    ax.set_xlabel('Coefficient', fontsize=24, labelpad=15)
    plt.show()


def three_heatmaps(points_1, alpha_1, points_2, alpha_2, points_3, alpha_3, title):
    fig, axes = plt.subplots(1, 3, figsize=(20, 10), constrained_layout=True)
    fig.suptitle(title, fontsize=32)
    create_heatmap(axes[0], points_1, '\u03B1 = ' + str(alpha_1))
    create_heatmap(axes[1], points_2, '\u03B1 = ' + str(alpha_2))
    create_heatmap(axes[2], points_3, '\u03B1 = ' + str(alpha_3))
    plt.show()


def test_normality_dagostino_pearson(data):
    return st.normaltest(data)


def test_normality_lilliefors(data):
    return diag.lilliefors(data)
