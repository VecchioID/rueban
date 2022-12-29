# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'
# only run in local macos
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
import torch
import torch.utils.data.dataset

plt.style.use(['science', 'nature'])


# 加载文件
class Dataset(torch.utils.data.Dataset):
    def __init__(self, dataset_path, dataset_type, config):
        self.dataset_path = dataset_path
        self.file_names = [f for f in glob.glob(os.path.join(self.dataset_path, config, "*.npz")) \
                           if dataset_type in f and "rule" not in f]
        self.config = config
        self.second_component = None

    def __len__(self):
        return len(self.file_names)

    def __getitem__(self, idx):
        data_path = self.file_names[idx]
        data = np.load(data_path)
        image = data["image"]
        target = data["target"]
        return image, target

'''
# plot raven demo
dataset_path = "/Users/vecchio/documents/phd_resource/paper/hippocampus_literature_code/code/dataset/"
dataset_type = "train"
config = "distribute_four"
dataset = Dataset(dataset_path, dataset_type, config)
image, target = dataset.__getitem__(1)

# 因为要使用scienceplot的绘图风格，还要保存图片，因为必须采用fig， ax的方式进行作图
# 绘制context
fig, ax = plt.subplots(3, 3)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1.5)
for row in range(0, 3):
    for col in range(0, 3):
        ax[row, col].imshow(image[row * 3 + col], cmap='gray')
        ax[2, 2].imshow(np.ones((160, 160)) * 255, cmap='gray')
        ax[row, col].set_xticks([])
        ax[row, col].set_yticks([])

fig.suptitle('Contexts')
plt.tight_layout()
fig.savefig('RPM_context.jpg', dpi=600)
plt.show()

# 绘制answer
fig, ax = plt.subplots(2, 4)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1.5)
for row in range(0, 2):
    for col in range(0, 4):
        ax[row, col].imshow(image[8 + 4 * row + col], cmap='gray')
        ax[row, col].set_xticks([])
        ax[row, col].set_yticks([])

fig.suptitle('Answer')
plt.tight_layout()
fig.savefig('RPM_answer.jpg', dpi=600)
plt.show()

# plot single panel
for i in range(0, 8):
    fig, ax = plt.subplots()
    fig.tight_layout()
    ax.imshow(image[i], cmap='gray')
    ax.set_xticks([])
    ax.set_yticks([])
    save_panel_name = 'RPM_context_' + str(i) + '_.png'
    fig.savefig(save_panel_name, dpi=600)
    # plt.show()
'''

# plot PGM demo
dataset_path = "./pgm_data/PGM_neutral_train_50679.npz"
dataset = np.load(dataset_path)
image = dataset["image"].reshape(16, 160, 160)
target = dataset["target"]

# 因为要使用scienceplot的绘图风格，还要保存图片，因为必须采用fig， ax的方式进行作图
# 绘制context
fig, ax = plt.subplots(3, 3)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1.5)
for row in range(0, 3):
    for col in range(0, 3):
        ax[row, col].imshow(image[row * 3 + col], cmap='gray')
        ax[2, 2].imshow(np.ones((160, 160)) * 255, cmap='gray')
        ax[row, col].set_xticks([])
        ax[row, col].set_yticks([])

fig.suptitle('Contexts')
plt.tight_layout()
fig.savefig('RPM_context.jpg', dpi=600)
plt.show()

# 绘制answer
fig, ax = plt.subplots(2, 4)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1.5)
for row in range(0, 2):
    for col in range(0, 4):
        ax[row, col].imshow(image[8 + 4 * row + col], cmap='gray')
        ax[row, col].set_xticks([])
        ax[row, col].set_yticks([])

fig.suptitle('Answer')
plt.tight_layout()
fig.savefig('RPM_answer.jpg', dpi=600)
plt.show()

# plot single panel
for i in range(0, 8):
    fig, ax = plt.subplots()
    fig.tight_layout()
    ax.imshow(image[i], cmap='gray')
    ax.set_xticks([])
    ax.set_yticks([])
    save_panel_name = 'RPM_context_' + str(i) + '_.png'
    fig.savefig(save_panel_name, dpi=600)
    # plt.show()
