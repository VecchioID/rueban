# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'
import matplotlib.pyplot as plt
import numpy as np
plt.style.use(['science', 'nature'])


# to install the lastest release (from PyPI)
# pip install SciencePlots
# todo 还没有完善完
def plot_with_science_sty(data_x, data_y, row_panel, col_panel, save_dpi, show_at_once):
    fig, ax = plt.subplots(row_panel, col_panel)
    # plt.subplots_adjust()
    fig.tight_layout()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1.5)

    ax[0].plot(x1, np.array(y1), '-r')
    ax[0].set_xlabel('Train loss vs. epoches')
    ax[0].set_ylabel('Position')

    ax[1].plot(x2, y2, '-r')
    ax[1].set_xlabel('Train accuracy vs. epoches')
    ax[1].set_ylabel('Train accuracy')

    plt.tight_layout()
    fig.savefig('TrainAndLoss.jpg', dpi=600)
    plt.show()
