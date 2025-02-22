# from preprocess import remove_noise, padd_and_resize, restore_padding_and_resizing, move_to_center_and_scale, restore_centering_and_scaling, create_templates_tensor, duplicate_seg_mask_to_tensor, crop_segmented_mask, process_segmentation_to_tensor, restore_matched_template_to_original_image, process_template_to_standard, extract_scores_and_transformations_from_result
from uttm.template_matcher import *



def main():
    ### define image, template and segmentation paths
    original_img = cv2.imread("../images/XXDQ_00.png")
    filtered_seg_img = cv2.imread("../segmentations/XXDQ_00.png", 0)
    templates_folder = 'templates/'





    '''
    read templates into a list
    '''
    templates_list = []
    templates_names = sorted(os.listdir(templates_folder))
    for template_name in templates_names:
        temp_template = cv2.imread(templates_folder + template_name , 0)
        temp_template = temp_template>0
        templates_list.append(temp_template)


    '''
    load segmentation masks (after running SAM) into a list
    '''
    unique_ids = np.unique(filtered_seg_img.flatten())

    segmentation_masks = [] 
    for seg_value in unique_ids:  
        if seg_value == 0 :  
            continue  # skip background
        temp_seg_mask = filtered_seg_img * (filtered_seg_img == seg_value)
        segmentation_masks.append(temp_seg_mask)





    '''
    run NN template matching
    '''
    # wthetehr refine after NN matching
    if_refine = True

    # intialize matcher
    matcher = Template_Matcher(angle_per_rotation=5)

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
