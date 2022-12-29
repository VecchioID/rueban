# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'
import matplotlib.pyplot as plt
import numpy as np
plt.style.use(['science', 'nature'])

def plot_loss_accuracy(loss_list, acc_list, epoches):
    x1 = np.arange(0, epoches)
    y1 = loss_list

    x2 = np.arange(0, epoches)
    y2 = acc_list

    fig, ax = plt.subplots(2, 1)
    # plt.subplots_adjust()
    fig.tight_layout()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1.5)
    # 第一张图
    ax[0].plot(x1, np.array(y1), '-r')
    ax[0].set_xlabel('Train loss vs. epoches')
    ax[0].set_ylabel('Position')

    ax[1].plot(x2, y2, '-r')
    ax[1].set_xlabel('Train accuracy vs. epoches')
    ax[1].set_ylabel('Train accuracy')

    plt.tight_layout()
    fig.savefig('TrainAndLoss.jpg', dpi=600)
    plt.show()
