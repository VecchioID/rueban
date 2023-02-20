# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from basic_model import BasicModel


# define net here
class Net(nn.Module):
    def __init__(self, model):
        super(Net, self).__init__()
        self.model = model

    def forward(self, x):
        x
        return x


class Solver(BasicModel):
    def __init__(self, args):
        super(Solver, self).__init__(args)
        self.model = args.model
        self.net = nn.DataParallel(Net(args.model, args.trn_n), device_ids=[0, 1]) if args.multi_gpu else Net(
            args.model, args.trn_n)
        self.optimizer = optim.Adam(self.parameters(), lr=args.lr)

    def compute_loss(self, output, target):
        return F.cross_entropy(output, target)

    def forward(self, x):
        x = 1 - x / 255.0
        out = self.net(x)
        return out
