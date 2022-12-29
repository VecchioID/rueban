# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'
import matplotlib.pyplot as plt


def loss_plot(loss_list, epoches):
    x1 = range(0, epoches)
    y1 = loss_list

    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, 'o-')
    plt.xlabel('Test loss vs. epoches')
    plt.ylabel('Test loss')
    plt.show()
