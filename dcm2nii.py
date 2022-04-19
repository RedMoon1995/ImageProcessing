#dcm2nii.win的执行命令
#dcm2niix.exe -f "27" -i y -l y -p y -x y -v y -z y -o "G:\project\data\CTdata\E0001270V3FC01" "G:\project\data\CTdata\E0001270V3FC01"
#dcm2niix.exe -f "27" -i y -l y -p y -x y -v y -z y -o "G:\project\data\CTdata\denoise\E0001270V3denoise" "G:\project\data\CTdata\denoise\E0001270V3denoise"
#.\dcm2niix.exe -f "27" -i y -l y -p y -x y -v y -z y -o "G:\project\tool_code\dcm\denoise" "G:\project\tool_code\dcm\denoise"
#SG:\project\data\CTdata\denoise\E0001270V3denoise

import numpy as np
import nibabel as nib
import os
import pandas as pd
import SimpleITK as sitk
import matplotlib.pyplot as plt

def dcm2nii_sitk(path_read, path_save):
    reader = sitk.ImageSeriesReader()
    seriesIDs = reader.GetGDCMSeriesIDs(path_read)
    print(seriesIDs)
    N = len(seriesIDs)
    #N = 5
    print(N)
    lens = np.zeros([N])
    for i in range(N):
        dicom_names = reader.GetGDCMSeriesFileNames(path_read, seriesIDs[i])
        print(dicom_names)
        lens[i] = len(dicom_names)
    N_MAX = np.argmax(lens)
    dicom_names = reader.GetGDCMSeriesFileNames(path_read, seriesIDs[N_MAX])
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    if not os.path.exists(path_save):
        os.mkdir(path_save)
    sitk.WriteImage(image, path_save+'/data.nii.gz')

#dcm2nii_sitk("G:\\project\\tool_code\\dcm\\dcm_single\\ct_train_1001_image-347.dcm",".\\")
dcm2nii_sitk("G:\\project\\data\\CTdata\\E0001270V3",".\\")

# DICOMpath = r"F:\Dicomdataset"   //dicom文件夹路径
# Midpath = r"F:\middataset"   //处理中间数据路径
# Resultpath = r"F:\result"    //保存路径
# cases = os.listdir(DICOMpath)  //获取dicom文件夹路径子文件夹名
# for c in cases:  //遍历dicom文件夹路径子文件
#     path_mid = join(DICOMpath , c)  //获取dicom文件夹下每一套数据的路径
#     dcm2nii_sitk(path_mid , Midpath )  //将dicom转换为nii，并保存在Midpath中
#     shutil.copy(join(Midpath , "data.nii.gz"), join(Resultpath , c + ".nii.gz"))
#     //重新对保存后的nii文件名进行命名，并复制到Resultpath下
