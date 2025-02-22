import torch
import torch.nn as nn
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import torch.nn.functional as F
from torchvision import transforms


from scipy.ndimage import rotate


import random

# from preprocess import remove_noise, padd_and_resize, restore_padding_and_resizing, move_to_center_and_scale, restore_centering_and_scaling, create_templates_tensor, duplicate_seg_mask_to_tensor, crop_segmented_mask, process_segmentation_to_tensor, restore_matched_template_to_original_image, process_template_to_standard, extract_scores_and_transformations_from_result
from preprocess import *
from refinement import *


class Conv2dLayer(nn.Module):
    def __init__(self, res = 512):
        super(Conv2dLayer, self).__init__()
        self.res = res

    def forward(self, x1, x2):
        # 将输入的两个二值mask进行逐点乘法操作
        fore_convolved = x1 * x2
        back_convolved = (1 - x1) * (1 - x2)
        
        score_fore = torch.sum(fore_convolved, dim=(2,3), keepdim=True) 
        score_back = torch.sum(back_convolved, dim=(2,3), keepdim=True)
    	
        score = score_fore + score_back 
        
        return score/(self.res**2)
    



class Template_Matcher():
    def __init__(self, angle_per_rotation = 5, device = "cuda"):

        self.angle_per_rotation = angle_per_rotation
        self.num_R_per_template = len(range(0,360,angle_per_rotation))

        if device == "cpu":
            self.device = "cpu"
        else:
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.nn = Conv2dLayer().to(self.device)


        self.template_scores_for_segmentations = []
        self.matching_info = []
        #self.matched_template_indices = []
        self.restored_template_masks = []


    def get_templates(self, templates):
        self.templates = templates
        self.num_templates = len(self.templates)


        processed_templates_list = []
        for iii in range(self.num_templates):
            temp_template = self.templates[iii]

            processed_template, _ = process_template_to_standard(temp_template)

            processed_templates_list.append(processed_template)

        self.templates_tensor = create_templates_tensor(processed_templates_list, angle_per_rotation=self.angle_per_rotation)


    def get_masks(self, masks):
        self.masks = masks

    # def init_nn(self):
    #     self.nn = Conv2dLayer()

    def reset_params(self, angle_per_rotation = 5):
        self.angle_per_rotation = angle_per_rotation
        self.num_R_per_template = len(range(0,360,angle_per_rotation))
        self.template_scores_for_segmentations = []
        self.matching_info = []
        #self.matched_template_indices = []
        self.restored_template_masks = []


    def match_by_nn(self, visualize = True):
        self.processed_masks = []
        for temp_seg_mask in self.masks:

            # process and convert segmentation into a tensor
            temp_seg_tensor, process_seg_info = process_segmentation_to_tensor(temp_seg_mask, self.templates_tensor.shape[0])
            self.processed_masks.append(temp_seg_tensor[0][0].cpu().numpy())


            # run torch matching and get matching results
            CNN_result = self.nn(temp_seg_tensor.to(self.device) , self.templates_tensor.to(self.device))


            # extract scores and transformation 
            scores, TP_info, restored_TP_for_vis = extract_scores_and_transformations_from_result(CNN_result, process_seg_info, self.templates_tensor, self.angle_per_rotation, self.num_R_per_template)
            # print(scores)
            # print(TP_info)


            self.template_scores_for_segmentations.append(scores)

            self.matching_info.append(TP_info)

            #self.matched_template_indices.append(np.argmax(scores))

            if visualize:
                self.restored_template_masks.append(restored_TP_for_vis)





    def refine_by_icp(self, visualize = True):
        for iii in range(len(self.masks)):
            img_1 = self.processed_masks[iii]

            chosen_template_idx = self.matching_info[iii]['template_idx']
            img_2 = self.templates_tensor[chosen_template_idx * self.num_R_per_template][0].cpu().numpy()

            img_1 = (img_1 > 0 ) * np.iinfo(np.int32).max
            img_2 = (img_2 > 0 ) * np.iinfo(np.int32).max

            mask1 = torch.from_numpy(img_1)
            mask2 = torch.from_numpy(img_2)

            init_angle = self.matching_info[iii]['rotation']

            mask2 = rotate(mask2, init_angle, reshape=True)
            mask2 = torch.from_numpy(mask2)

            #print(f"GT rotation angle: {init_angle:2f} degrees")

            # 提取点集
            source_points = extract_points_from_mask(mask2)
            target_points = extract_points_from_mask(mask1)




            # 运行 ICP
            _, _, _, tR = icp(source_points, target_points)
            tR = np.degrees(tR)

            if abs(tR) >= self.angle_per_rotation/2:
                continue


            self.matching_info[iii]['rotation'] += tR


            if visualize:
                self.restored_template_masks[iii] = refine_mask_rotation_visualization(self.restored_template_masks[iii], -tR)








    def visualize_result(self, image):

        total_mask = np.zeros_like(image)
        for iii in range(len(self.restored_template_masks)):
            restored_template_mask = self.restored_template_masks[iii]


            restored_template_mask = np.repeat(restored_template_mask[:, :, np.newaxis], 3, axis=2)

            temp_color = np.array([random.randint(128,255), random.randint(128,255), random.randint(128,255) ])
            colored_restored_template_mask = (restored_template_mask>0) * temp_color
            colored_restored_template_mask =colored_restored_template_mask.astype(np.uint8)

            total_mask += colored_restored_template_mask

            temp_restore_info = self.matching_info[iii]
            cx,cy,radius = temp_restore_info['cx'],temp_restore_info['cy'],temp_restore_info['radius']


            cv2.circle(total_mask, (round(cx),round(cy)), round(radius), (0,0,255), 10)

            
            text = "Template idx "+str(self.matching_info[iii]['template_idx'])
            (text_width, _), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            text_x = round(cx-radius+2*(radius - text_width) // 2) 
            text_y = min(round(cy+radius+5),image.shape[0])

            # 绘制文字
            cv2.putText(total_mask, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)
        
        merge_img = cv2.addWeighted(image, 1 , total_mask, 0.75, 0)
        return merge_img









    
    