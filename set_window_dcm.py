
import nibabel as nib
import numpy as np
import SimpleITK as sitk
center = 40  # 窗位
width = 300  # 窗宽

filename = 'E0001270V3_1.nii.gz'
img_sitk = sitk.ReadImage(filename)
img = sitk.GetArrayFromImage(img_sitk)
img_spacing = img_sitk.GetSpacing()
img_origin = img_sitk.GetOrigin()
img_direction = img_sitk.GetDirection()
# img = nib.load(filename)
# img_fdata = img.get_fdata()
print(img.shape)
min = (2 * center - width) / 2.0 + 0.5
max = (2 * center + width) / 2.0 + 0.5
      
# dFactor = 255.0 / (max - min)

img[img<min] = min
img[img>max] = max
# # 进行转置，因为需要按照原来的方向进行保存
# data = np.transpose(img_fdata, [2, 1, 0])
# (x, y, z) = data.shape
# print(z," ",y," ",x)
# for i in range(x):
#     for j in range(y):
#         for k in range(z):
#             value = data[i,j,k]
#             if value <= min:
#                 value = 0
#             elif value < max:
#                 value = (value - min) / width * 255
#             elif value >= max:
#                 value = 255
#             data[i,j,k] = value 
#进行保存
print("-----------------")
filesname = "./5_transfer.nii.gz"    
print(img.shape)        
img = sitk.GetImageFromArray(img)
img.SetDirection(img_direction)
img.SetSpacing(img_spacing)
img.SetOrigin(img_origin)
sitk.WriteImage(img, filesname)
print("+++++++++++++++++")