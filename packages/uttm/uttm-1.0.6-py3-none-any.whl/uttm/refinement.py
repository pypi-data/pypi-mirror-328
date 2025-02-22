import torch
import torch.nn.functional as F
import numpy as np
from scipy.ndimage import rotate
import cv2
import time


def extract_points_from_mask(mask):
    """从二值 mask 中提取点集"""
    y, x = torch.where(mask.squeeze())
    points = torch.stack((x, y), dim=1).float()  # 转换为 (N, 2) 的点集
    return points

def compute_rotation_translation(source, target):
    """计算旋转矩阵和平移向量"""
    # 中心化点集
    source_mean = source.mean(dim=0)
    target_mean = target.mean(dim=0)
    source_centered = source - source_mean
    target_centered = target - target_mean

    # 计算协方差矩阵
    H = torch.mm(source_centered.T, target_centered)

    # SVD 分解
    U, S, V = torch.svd(H)
    R = torch.mm(V, U.T)  # 旋转矩阵

    # 计算平移向量
    t = target_mean - torch.mm(R, source_mean.unsqueeze(1)).squeeze()

    return R, t

def icp(source_points, target_points, max_iterations=100, error_tolerance=1e-3, rotation_tolerance=1e-3):
    total_R = 0
    """ICP 算法"""
    prev_error = 0
    for i in range(max_iterations):
        # 找到最近邻点
        flann = cv2.flann_Index(target_points.numpy(), {'algorithm': 1, 'trees': 1})  # 1 表示 KDTree
        k = 1  # 最近邻的数量
        indices, _ = flann.knnSearch(source_points.numpy(), k, params={})
        closest_points = target_points[indices.flatten()]

        # 计算旋转和平移
        R, t = compute_rotation_translation(source_points, closest_points)
        total_R += torch.atan2(R[1, 0], R[0, 0]).item()

        # 更新 source 点集
        source_points = torch.mm(source_points, R.T) + t

        # 计算误差
        mean_error = torch.mean(torch.norm(source_points - closest_points, dim=1))
        if torch.abs(prev_error - mean_error) < error_tolerance and torch.abs(torch.atan2(R[1, 0], R[0, 0])) < rotation_tolerance:
            #print(f"Iteration {i+1}, Error: {mean_error.item()}, Tmp Rotation : {np.degrees(torch.atan2(R[1, 0], R[0, 0]).item())}, Total Rotation: {np.degrees(total_R)}")
            break
        prev_error = mean_error + 0.

        

        #print(f"Iteration {i+1}, Error: {mean_error.item()}, Tmp Rotation : {np.degrees(torch.atan2(R[1, 0], R[0, 0]).item())}, Total Rotation: {np.degrees(total_R)}")

        

    return R, t, source_points,total_R


