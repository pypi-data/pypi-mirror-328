import os
import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms

# class Conv2dLayer(nn.Module):
#     def __init__(self):
#         super(Conv2dLayer, self).__init__()

#     def forward(self, x1, x2):
#         # 将输入的两个二值mask进行逐点乘法操作
#         fore_convolved = x1 * x2
#         back_convolved = (1 - x1) * (1 - x2)
        
#         score_fore = torch.sum(fore_convolved, dim=(2,3), keepdim=True) 
#         score_back = torch.sum(back_convolved, dim=(2,3), keepdim=True)
    	
#         score = score_fore + score_back 
        
#         return score/(512**2)
    
    
    
def remove_noise(mask, kernel_size=10):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    # 开运算：先腐蚀后膨胀
    mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    return mask_open


def padd_and_resize(mask, target_size=(512, 512)):

    h, w = mask.shape
    max_dim = max(h, w)
    padded_mask = np.zeros((max_dim, max_dim), dtype=np.uint8)
    pad_top = (max_dim - h) // 2
    pad_left = (max_dim - w) // 2
    padded_mask[pad_top:pad_top+h, pad_left:pad_left+w] = mask

    # 缩放到 512x512
    resized_mask = cv2.resize(padded_mask, target_size, interpolation=cv2.INTER_NEAREST)

    padd_params = {
        "original_size_before_padding": (h, w),
        "pad_top": pad_top,
        "pad_left": pad_left,
        "resize_scale": target_size[0] / max_dim
    }

    return resized_mask, padd_params


def restore_padding_and_resizing(mask, padd_params):
    max_dim = int(mask.shape[0] / padd_params["resize_scale"])
    restored_mask = cv2.resize(mask, (max_dim, max_dim), interpolation=cv2.INTER_NEAREST)

    # 3. 还原填充
    pad_top = padd_params["pad_top"]
    pad_left = padd_params["pad_left"]
    h, w = padd_params["original_size_before_padding"]
    original_mask = restored_mask[pad_top:pad_top+h, pad_left:pad_left+w]

    return original_mask



def move_to_center_and_scale(mask, resized_R = 128):

    mask = mask > 0
    mask = mask.astype(np.uint8)
    mask *= 255

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        raise ValueError("No contours found in the mask.")

    # 找到最大的轮廓
    largest_contour = max(contours, key=cv2.contourArea)

    largest_contour = largest_contour.reshape(-1, 2)
    (cx, cy), radius = cv2.minEnclosingCircle(np.array(largest_contour, dtype=np.int32))

    h, w = mask.shape

    # 移动图像中心到掩码的轮廓中心
    # 计算需要移动的偏移量
    offset_x = w // 2 - cx
    offset_y = h // 2 - cy

    # 创建平移矩阵
    M = np.float32([[1, 0, offset_x], [0, 1, offset_y]])
    translated_mask = cv2.warpAffine(mask, M, (w,h))

    center = (w//2, h//2)

    #scaling
    angle = 0

    scale = resized_R/radius
    M = cv2.getRotationMatrix2D(center, angle, scale)  
    final_mask = cv2.warpAffine(translated_mask, M, (w, h)) 

    move_scale_params = {
        "offset_x": offset_x,
        "offset_y": offset_y,
        "scale": scale
    }

    return final_mask, move_scale_params



def restore_centering_and_scaling(processed_mask, restore_params):
    h,w = processed_mask.shape

    center = (h//2, w//2)

    restore_scale = 1. /restore_params["scale"]
    angle = 0
    M = cv2.getRotationMatrix2D(center, angle, restore_scale)  
    processed_mask = cv2.warpAffine(processed_mask, M, (w, h)) 
    

    # 还原平移
    offset_x = restore_params["offset_x"]
    offset_y = restore_params["offset_y"]
    M = np.float32([[1, 0, -offset_x], [0, 1, -offset_y]])
    restored_mask = cv2.warpAffine(processed_mask, M, (w, h))

    return restored_mask




# 读取文件夹中的所有二值 mask，并转化为一个 tensor
def create_templates_tensor(processed_TP_list, angle_per_rotation = 5):

    mask_tensors = []

    angles = range(0,360,angle_per_rotation)
    for temp_TP in processed_TP_list:
        center = (temp_TP.shape[1] // 2, temp_TP.shape[0] // 2)  # 获取图像中心点
        for angle in  angles:
            M = cv2.getRotationMatrix2D(center, angle, 1)  # 获取旋转矩阵
            rotated_TP = cv2.warpAffine(temp_TP, M, (temp_TP.shape[1], temp_TP.shape[0]))  # 进行旋转

            mask_tensor = transforms.ToTensor()(rotated_TP)
            mask_tensors.append(mask_tensor)
    mask_tensors = torch.stack(mask_tensors)
    return mask_tensors
        




# 复制一个 mask 并生成相同数量的 tensor
def duplicate_seg_mask_to_tensor(mask, num_duplicates):
    # 确保 mask 是二值图像
    _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

    # 将 mask 转换为 tensor
    mask_tensor = transforms.ToTensor()(mask)

    # 复制 mask 并生成相同数量的 tensor
    duplicated_masks = mask_tensor.repeat(num_duplicates, 1, 1, 1)
    return duplicated_masks


def crop_segmented_mask(mask):
    h,w = mask.shape

    # 查找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    if len(contours) == 0:
        raise ValueError("No contours found in the mask.")

    # 找到最大的轮廓
    largest_contour = max(contours, key=cv2.contourArea)

    (x, y), radius = cv2.minEnclosingCircle(np.array(largest_contour, dtype=np.int32))

    x_min = round(max(0, x-radius*1.25))
    x_max = round(min(w-1, x+radius*1.25))

    y_min = round(max(0, y-radius*1.25))
    y_max = round(min(h-1, y+radius*1.25))

    crop_info = {"x_min":x_min, "x_max":x_max, "y_min":y_min, "y_max":y_max, "original_size_before_cropping": (h,w)}

    return mask[y_min:y_max, x_min:x_max ], crop_info


def process_segmentation_to_tensor(seg, len_tensor):

    temp_seg_mask = seg.astype(np.uint8)
    temp_seg_mask *= 255


    temp_seg_mask = remove_noise(temp_seg_mask, kernel_size=20)

    cropped_seg_mask, crop_info = crop_segmented_mask(temp_seg_mask)
    padded_seg_mask, padd_resize_info = padd_and_resize(cropped_seg_mask)
    processed_seg_mask, move_scale_info= move_to_center_and_scale(padded_seg_mask)

    seg_tensor = duplicate_seg_mask_to_tensor(processed_seg_mask, len_tensor)

    process_info = {}
    process_info["crop_x_min"] = crop_info['x_min']
    process_info["crop_x_max"] = crop_info['x_max']
    process_info["crop_y_min"] = crop_info['y_min']
    process_info["crop_y_max"] = crop_info['y_max']
    process_info["original_size_before_cropping"] = crop_info['original_size_before_cropping']

    process_info['original_size_before_padding'] = padd_resize_info['original_size_before_padding']
    process_info['pad_top'] = padd_resize_info['pad_top']
    process_info['pad_left'] = padd_resize_info['pad_left']
    process_info['resize_scale'] = padd_resize_info['resize_scale']

    process_info['offset_x'] = move_scale_info['offset_x']
    process_info['offset_y'] = move_scale_info['offset_y']
    process_info['scale'] = move_scale_info['scale']

    

    return seg_tensor, process_info


def restore_matched_template_to_original_image(TP, process_info):
    processed_TP = restore_centering_and_scaling(TP, process_info)
    processed_TP = restore_padding_and_resizing(processed_TP, process_info)
    processed_TP = cv2.resize(processed_TP, 
                              (process_info["crop_x_max"]-process_info["crop_x_min"], 
                               process_info["crop_y_max"]-process_info["crop_y_min"]))

    
    h, w = process_info['original_size_before_cropping']
    final_TP = np.zeros((h,w))
    final_TP[process_info["crop_y_min"]:process_info["crop_y_max"],
             process_info["crop_x_min"]:process_info["crop_x_max"]] = processed_TP
    
    
    temp_TP = final_TP > 0
    temp_TP = temp_TP.astype(np.uint8)
    temp_TP *= 255
    contours, _ = cv2.findContours(temp_TP, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 找到最大的轮廓
    largest_contour = max(contours, key=cv2.contourArea)

    largest_contour = largest_contour.reshape(-1, 2)
    (cx, cy), radius = cv2.minEnclosingCircle(np.array(largest_contour, dtype=np.int32))
    restore_info = {}
    restore_info['cx'] = cx
    restore_info['cy'] = cy
    restore_info['radius'] = radius

    
    return final_TP, restore_info



def process_template_to_standard(TP):

    padded_template, padd_resize_info = padd_and_resize(TP)
    processed_template, move_scale_info = move_to_center_and_scale(padded_template)

    process_info = {}
    process_info['original_size_before_padding'] = padd_resize_info['original_size_before_padding']
    process_info['pad_top'] = padd_resize_info['pad_top']
    process_info['pad_left'] = padd_resize_info['pad_left']
    process_info['resize_scale'] = padd_resize_info['resize_scale']

    process_info['offset_x'] = move_scale_info['offset_x']
    process_info['offset_y'] = move_scale_info['offset_y']
    process_info['scale'] = move_scale_info['scale']

    return processed_template, process_info


def extract_scores_and_transformations_from_result(result, process_info, TP_tensor,theta, num_R):

    _, inds = torch.topk(result.flatten() ,1)
    result = result.cpu().numpy().reshape(-1)

    score_per_template = [max(result[kkk*num_R:(kkk+1)*num_R]) for kkk in range(int(TP_tensor.shape[0]/num_R))]

    
    chosen_inds = inds.cpu().numpy()
    matched_template = (TP_tensor.cpu())[chosen_inds[0]]
    matched_template = matched_template[0].numpy().astype(np.uint8)

    

    restored_TP, restored_TP_info = restore_matched_template_to_original_image(matched_template, 
                                                             process_info)
    
    restored_TP_info['rotation'] = range(0,360,theta)[chosen_inds[0] % num_R]

    template_idx = np.argmax(score_per_template)
    restored_TP_info['template_idx'] = template_idx

    return score_per_template, restored_TP_info, restored_TP



def refine_mask_rotation_visualization(mask, angle):

    mask = mask > 0
    mask = mask.astype(np.uint8)
    mask *= 255


    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = max(contours, key=cv2.contourArea)
    largest_contour = largest_contour.reshape(-1, 2)
    (cx, cy), radius = cv2.minEnclosingCircle(np.array(largest_contour, dtype=np.int32))

    # # 获取轮廓的外接圆圆心和半径
    # (cx, cy), radius = cv2.minEnclosingCircle(contours[0])
    # cx, cy = round(cx), round(cy)  # 将圆心坐标转换为整数

    # 获取旋转矩阵
    rotation_matrix = cv2.getRotationMatrix2D((cx, cy), angle, 1)

    # 创建一个新的掩码
    rotated_mask  = cv2.warpAffine(mask, rotation_matrix, (mask.shape[1], mask.shape[0]))

    return rotated_mask

