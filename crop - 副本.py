import SimpleITK as sitk
import numpy as np
import os

def crop_dcms(data_dir_name):
    ct_root_path = "G:/project/data/CTdata/"
    #mask_root_path = "/data/zengnanrong/crop_CTdata/"
    output_root_path = "G:/project/data/crop_CTdata/"

    path = os.path.join(ct_root_path, data_dir_name)
    for root, dirs, files in os.walk(path):
        for item in files:
            if '.dcm' in item.lower():
                ct_path = os.path.join(root, item) #dcm文件完整绝对路径
                #mask_path = ct_path.replace(ct_root_path, mask_root_path)

                ct_image = sitk.ReadImage(ct_path) #读取cm图片
                ct_image_array = np.squeeze(sitk.GetArrayFromImage(ct_image)) #将dcm图片转为数组 array[z,x,y]
                #mask_image = sitk.ReadImage(mask_path)
                #mask_image_array = np.squeeze(sitk.GetArrayFromImage(mask_image))

                print (ct_image_array.shape)

                

str = input('input dcmfilename: ')
crop_dcms(str)
                
                # height = ct_image_array.shape[0]
                # width = ct_image_array.shape[1]

                # for h in range(height): #循环高
                #     '''for w in range(width): #循环宽
                #         if mask_image_array[h][w] == 0:
                #             # 将非肺区域置0
                #             ct_image_array[h][w] = 0'''
                #     ct_image_array[h][w] = ct_image_array[100:200,100:200]
                
                 
                # seg_path = ct_path.replace(ct_root_path, output_root_path)
                # seg_dir = os.path.split(seg_path)[0]
                # if not os.path.exists(seg_dir):
                #     os.makedirs(seg_dir)

                # ct_image_array = np.reshape(ct_image_array, (1, height, width))
                # seg_image = sitk.GetImageFromArray(ct_image_array)
                # seg_image.CopyInformation(ct_image)
                # sitk.WriteImage(seg_image, seg_path)
                # logging.info(f'Save result to: {seg_path}')