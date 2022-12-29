# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'

def calculate_acc(output, target):
    pred = output.data.max(1)[1]
    correct = pred.eq(target.data).cpu().sum().numpy()
    return correct * 100.0 / target.size()[0]