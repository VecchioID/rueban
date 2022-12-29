# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'
import time
import tqdm
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


def train(model, trainloader, optimizer, args, device):
    # 完成训练流程的构建以及模型文件的保存、打印训练精度等功能
    for epoch in args.epochs:
        prog_start = time.time()
        model.train()
        count = 0
        acc_all = 0
        error_all = 0
        for batch_idx, (image, target, meta_target) in enumerate(tqdm(trainloader)):
            image = image.to(device)
            target = target.to(device)
            output_target = model(image)  # batch x n_layers x nt
            loss_target = F.cross_entropy(output_target, target)
            errors = loss_target
            optimizer.zero_grad()
            errors.backward()
            optimizer.step()

            # 统计loss和acc
            count += 1
            pred = output_target.data.max(1)[1]
            correct = pred.eq(target.data).cpu().sum().numpy()
            accuracy = correct * 100 / target.size()[0]
            acc_all += accuracy
            error_all += errors

        prog_end = time.time()
        print("Average training loss:{}, Average training acc:{}".format(error_all / float(count), acc_all / float(count)))
        print("Training completed in {:.2f} minutes.".format((prog_end - prog_start) / 60))
    return error_all / float(count), acc_all / float(count)
