from matplotlib import pyplot as plt


def scatterplot_m_K(points):
    m = points[:, 0]
    K = points[:, 1]
    values = points[:, 2]

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.scatter(m, K)
    for i, txt in enumerate(values):
        ax.annotate(txt, (m[i], K[i]), fontsize=16)

    ax.set_title('Relative error', fontsize=32)
    ax.set_xlabel('m', fontsize=24, labelpad=15)
    ax.set_ylabel('K', fontsize=24, labelpad=15)

    plt.show()
