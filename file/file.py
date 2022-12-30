# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'
import sys
import os


# 获取当前路径下所有文件
def get_all_files(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


# 获取当前路径下所有文件夹
def get_all_dirs(path):
    dir_list = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            dir_list.append(os.path.join(root, dir))
    return dir_list


def check_path_is_exist(path):
    # if not exist, create it
    if not os.path.exists(path):
        os.mkdir(path)