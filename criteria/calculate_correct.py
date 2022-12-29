# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'
def calculate_correct(output, target):
    pred = output.data.max(1)[1]
    correct = pred.eq(target.data).cpu().sum().numpy()
    return correct