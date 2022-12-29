# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'

import torch
import torch.nn as nn
import torch.nn.functional as F


class pred_res_block(nn.module):
    def __init__(self):
        super(pred_res_block, self).__init__()
        self.left_mid = nn.Sequential(
            nn.Conv1d(8, 1, 1)
        )

        self.left = nn.Sequential(
            nn.Conv2d(1, out_channel, kernel_size=3, stride=stride, padding=1, bias=False),
            nn.BatchNorm2d(out_channel),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channel, out_channel, kernel_size=3, stride=1, bias=False),
            nn.BatchNorm2d(out_channel)
        )

    def forward(self, x):
        c = x[:,0:8]
        a = x[:,8:16]
        e_ = self.left_mid(c)-a
        x_ = torch.cat((c, a+e_), dim=1)


        return 0


class pred_res_network(nn.Module):
    def __init__(self):
        super(pred_res_network, self).__init__()

    def forward(self, x):
        return 0
