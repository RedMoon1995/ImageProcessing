# coding=UTF-8
import SimpleITK as sitk
import os
 #dicom存放文件夹
img_path = './'
img_names = os.listdir(img_path)
for img_name in img_names:
    ds = sitk.ReadImage(img_path + img_name)

'''file_path = './'
series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(file_path)
series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(file_path)

series_reader = sitk.ImageSeriesReader()
series_reader.SetFileNames(series_file_names)'''

series_reader = sitk.ImageSeriesReader()
series_reader.SetFileNames(ds)

image3D = series_reader.Execute()
sitk.WriteImage(image3D, './2.nii.gz')


'''filedir = './lung_img.nii.gz'
outdir = './lung_img/'
if not os.path.isdir(outdir):
    os.mkdir(outdir) 
img = sitk.ReadImage(filedir)
img = sitk.GetArrayFromImage(img)   
for i in range(img.shape[0]):
    select_img = sitk.GetImageFromArray(img[i])
    sitk.WriteImage(select_img,outdir+str(img.shape[0]-i)+'.dcm')
'''