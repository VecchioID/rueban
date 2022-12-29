# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'
import matplotlib.pyplot as plt


def acc_plot(acc_list, epoches):
    x2 = range(0, epoches)
    y2 = acc_list

    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, '.-')
    plt.title('Test accuracy vs. epoches')
    plt.ylabel('Test accuracy')
    plt.show()
