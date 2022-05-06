import SimpleITK as sitk
import numpy as np
from PIL import Image
import os


def crop_dcms(data_dir_name):
    ct_root_path = "G:\\project\\data\\CTdata\\"
    # mask_root_path = "/data/zengnanrong/crop_CTdata/"
    output_root_path = "G:\\project\\data\\crop_CTdata\\"

    path = os.path.join(ct_root_path, data_dir_name)
    for root, dirs, files in os.walk(path):
        i = 0
        j = 0
        for item in files:
            i = i + 1
            j = j + 1
            if '.dcm' in item.lower() and i<=499 and i>=100:
                ct_path = os.path.join(root, item)  # dcm文件完整绝对路径
                # mask_path = ct_path.replace(ct_root_path, mask_root_path)

                ct_image = sitk.ReadImage(ct_path)  # 读取dcm图片
                ct_image_array = sitk.GetArrayFromImage(ct_image)

                #ct_image_array = np.squeeze(sitk.GetArrayFromImage(ct_image))  # 将dcm图片转为数组 array[z,x,y]
                # mask_image = sitk.ReadImage(mask_path)
                # mask_image_array = np.squeeze(sitk.GetArrayFromImage(mask_image))

                print(ct_image_array.shape)

                crop_dir = os.path.join(output_root_path, data_dir_name + "crop")
                crop_path = os.path.join(output_root_path, data_dir_name + "crop",str(j)+".dcm")

                if not os.path.exists(crop_dir):
                    os.makedirs(crop_dir)

                # ct_crop_array = np.zeros((512, 512), dtype = int)
                # i = 0
                # for j in range(0,155):
                #     ct_crop_array[0:155][i] = ct_image_array[190:345]
                #     i += 1

                ct_crop_array = []
                ct_crop_array.append(ct_image_array[0][150:350, 200:400])
                #ct_crop_array.append(ct_image_array[0][0:512, 0:512])
                #ct_crop_array.append(ct_image_array[0][117:272,190:345])
                #ct_crop_array.append(ct_image_array[0][97:292, 170:365])
                #ct_crop_array[0] = np.pad(ct_crop_array[0], ((80, 237), (80, 237)), 'constant', constant_values=(0, 0)) #三维数组，z维度为1
                ct_crop_array = np.array(ct_crop_array) #把list转化为array


                print(ct_crop_array.shape)
                #print(ct_crop_array)
                crop_image = sitk.GetImageFromArray(ct_crop_array)
                #crop_image.CopyInformation(ct_image)
                crop_image.SetMetaData("0010|0010", ct_image.GetMetaData("0010|0010"))  #Patient's Name
                crop_image.SetMetaData("0010|0020", ct_image.GetMetaData("0010|0020"))  #Patient ID
                crop_image.SetMetaData("0010|0030", ct_image.GetMetaData("0010|0030"))
                crop_image.SetMetaData("0010|0040", ct_image.GetMetaData("0010|0040"))
                crop_image.SetMetaData("0018|0022", ct_image.GetMetaData("0018|0022"))
                crop_image.SetMetaData("0020|0013", str(j))
                #insNum = i - 174
                #crop_image.SetMetaData("0020|0013", "%d"%insNum) #Instance Number
                crop_image.SetMetaData("0018|0050", ct_image.GetMetaData("0018|0050")) #Slice Thickness
                crop_image.SetMetaData("0020|1041", ct_image.GetMetaData("0020|1041")) #Slice Location
                crop_image.SetMetaData("0028|0030", ct_image.GetMetaData("0028|0030")) #Pixel Spacing
                crop_image.SetMetaData("0010|1010", ct_image.GetMetaData("0010|1010")) #Patient's Age
                crop_image.SetMetaData("0008|103e", ct_image.GetMetaData("0008|103e"))  #Series Description
                crop_image.SetMetaData("0020|0011", ct_image.GetMetaData("0020|0011"))  #序列号：识别不同检查的号码.
                crop_image.SetMetaData("0020|000e", ct_image.GetMetaData("0020|000e"))  #序列实例号：唯一标记不同序列的号码.
                crop_image.SetMetaData("0020|0010", ct_image.GetMetaData("0020|0010"))  # Study ID
                crop_image.SetMetaData("0008|0050", ct_image.GetMetaData("0008|0050"))
                crop_image.SetMetaData("0008|0020", ct_image.GetMetaData("0008|0020"))
                crop_image.SetMetaData("0008|0022", ct_image.GetMetaData("0008|0022"))
                crop_image.SetMetaData("0008|0023", ct_image.GetMetaData("0008|0023"))
                crop_image.SetMetaData("0008|0030", ct_image.GetMetaData("0008|0030"))
                crop_image.SetMetaData("0008|0032", ct_image.GetMetaData("0008|0032"))
                crop_image.SetMetaData("0008|0033", ct_image.GetMetaData("0008|0033"))
                crop_image.SetMetaData("0008|0060", ct_image.GetMetaData("0008|0060"))
                crop_image.SetMetaData("0008|0008", ct_image.GetMetaData("0008|0008"))
                crop_image.SetMetaData("0008|0016", ct_image.GetMetaData("0008|0016"))
                crop_image.SetMetaData("0008|0018", ct_image.GetMetaData("0008|0018"))

                crop_image.SetMetaData("0018|5100", ct_image.GetMetaData("0018|5100"))
                #crop_image.SetMetaData("0020|000d", ct_image.GetMetaData("0020|000d"))
                crop_image.SetMetaData("0020|000d", "1")
                crop_image.SetMetaData("0020|0052", ct_image.GetMetaData("0020|0052"))
                crop_image.SetMetaData("0020|000e", ct_image.GetMetaData("0020|000e"))
                crop_image.SetMetaData("0028|1050", "[250,250]") #WL
                crop_image.SetMetaData("0028|1051", "[1300,1300]") #WW
                crop_image.SetMetaData("0028|1052", "-1024.0") #Rescale Intercept
                crop_image.SetMetaData("0028|1053", "1.0") #Rescale Slope

                crop_image.SetMetaData("0040|0002", ct_image.GetMetaData("0040|0002"))
                crop_image.SetMetaData("0040|0003", ct_image.GetMetaData("0040|0003"))
                crop_image.SetMetaData("0040|0004", ct_image.GetMetaData("0040|0004"))
                crop_image.SetMetaData("0040|0005", ct_image.GetMetaData("0040|0005"))
                crop_image.SetMetaData("0040|0244", ct_image.GetMetaData("0040|0244"))
                crop_image.SetMetaData("0040|0245", ct_image.GetMetaData("0040|0245"))
                crop_image.SetMetaData("0040|0253", ct_image.GetMetaData("0040|0253"))


                #crop_image.SetMetaData("0028|0010", '195')
                #crop_image.SetMetaData("0028|0011", '195')
                print(crop_image.GetMetaData("0020|0013"))
                print(ct_image.GetMetaData("0020|1041"))

                sitk.WriteImage(crop_image, crop_path)
                print('Save result to: %s' % crop_path)


dcmfilename = input('input dcmfilename: ')
crop_dcms(dcmfilename)

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
