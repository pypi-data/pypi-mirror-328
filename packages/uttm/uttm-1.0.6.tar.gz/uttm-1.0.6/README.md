# Unsupervised-Torch-Template-Matching

A repository for robust 2D template matching based on torch unsupervised learning.

## Installation

```
pip install uttm
```

The main dependencies are:

- numpy
- torch
- torchvision
- opencv-python

## Pipeline

### 1. Preprocess templates and segmentations

By default the binary template and segmentation images can aibitrary.

The preprocessing step will automatically turn a mask into a 512*512 image, where the center of minimum enclosing circle
is at the image center and the radius of the circle is 128. The processing step will keep the infomation of padding,
translation, rotation and scaling, so that we can restore the templates back to original images.

### 2. Compute statistics by unsupervised learning

### 3. Fine-tune the rotation by 2d-icp (optional)

### 4. Visualization for matching evaluation (optional)

## Data Preparation

We provide the [example data](https://drive.google.com/drive/folders/1m9idEbKWOyDbeqHgnHHvbdW2UAv4ANhC) used for
template matching, the input mainly

- template images
- segmentation image
- (Optional) Origina image before segmentation, used only for visualization

For custom data, a user can either extract foreground mask through online platforms
like https://www.fotor.com/features/background-remover/, or locally run segmentation model like Segment
Anthing (https://huggingface.co/docs/transformers/model_doc/sam) or
Birefnet(https://huggingface.co/ZhengPeng7/BiRefNet).

## Parameters for our Template_Matcher class

### Inputs

- ```angle_per_rotation```: angle for each rotation resolution for one template (e.g. if we define it as 10, we will
  have 36 preprocessed separate masks for one template). It's defined through class initialization or function
  ```reset_params()```
- template: a list of binary template masks. Defined through function ```get_templates```
- segmentation masks: a list of binary segmentation masks. Defined through function ```get_masks```

### Outputs

- ```template_scores_for_segmentations```: n * m array for n segmentations and m templates;
- ```matching_info```: matching infomation according to maximum score of per m-dimention array for n segmentations,
  including best matched template index, rotation wrt. input template, translation and scales of template to original
  segmentation image (represented by center position and radius of minimum enclosing circle).

## How to use

Assume the inputs are in ```./templates/```, ```./segmentations/```.

```python
import os

import cv2
import numpy as np
from matplotlib import pyplot as plt

import uttm


def main():
    ### define image, template and segmentation paths
    original_img = cv2.imread("./images/XXDQ_00.png")
    filtered_seg_img = cv2.imread("./segmentations/XXDQ_00.png", 0)
    templates_folder = './templates/'

    '''
    read templates into a list
    '''
    templates_list = []
    templates_names = sorted(os.listdir(templates_folder))
    for template_name in templates_names:
        temp_template = cv2.imread(templates_folder + template_name, 0)
        temp_template = temp_template > 0
        templates_list.append(temp_template)

    '''
    load segmentation masks (after running SAM) into a list
    '''
    unique_ids = np.unique(filtered_seg_img.flatten())

    segmentation_masks = []
    for seg_value in unique_ids:
        if seg_value == 0:
            continue  # skip background
        temp_seg_mask = filtered_seg_img * (filtered_seg_img == seg_value)
        segmentation_masks.append(temp_seg_mask)

    '''
    run NN template matching
    '''
    # wthetehr refine after NN matching
    if_refine = True

    # intialize matcher
    matcher = uttm.Template_Matcher(angle_per_rotation=5)

    # feed templates and masks to matcher
    matcher.get_templates(templates_list)
    matcher.get_masks(segmentation_masks)
    # matcher.reset_params()  

    # run unsupervised NN matching
    matcher.match_by_nn()

    print(matcher.matching_info)
    # visualize matching results
    merge_img = matcher.visualize_result(original_img)
    plt.imshow(merge_img)
    plt.axis('off')
    plt.show()

    cv2.imwrite("../results/XXDQ_00_01.png", merge_img)

    # run refinement 
    if if_refine:
        matcher.refine_by_icp()

        print(matcher.matching_info)
        # visualize matching results
        merge_img = matcher.visualize_result(original_img)
        plt.imshow(merge_img)
        plt.axis('off')
        plt.show()

        cv2.imwrite("../results/XXDQ_00_02.png", merge_img)


if __name__ == "__main__":
    main()
```

