import os
import SimpleITK as sitk
import numpy as np
import cv2


def endWith(*endstring):
    ends=endstring
    def run(s):
        f=map(s.endswith,ends)
        if True in f:
            return s
    return run


def convert_from_dicom_to_jpg(img, low_window, high_window, save_path):
    lungwin = np.array([low_window * 1., high_window * 1.])
    newimg = (img - lungwin[0]) / (lungwin[1] - lungwin[0])  # 归一化
    newimg = (newimg * 255).astype('uint8')  # 将像素值扩展到[0,255]
    cv2.imwrite(save_path, newimg, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

if __name__=='__main__':
    #list_file=os.listdir('C:/Data/001/C+ delay')
    #a=endWith('.dcm')
    #f_file=filter(a,list_file)
    #data=[]
    #for i in f_file:
        #print(i)  #dcm的文件名
        #data.append(i)
    # #print(len(data))
    # print(data)
    # data.reverse()
    # print(data)

    # 下面是将对应的dicom格式的图片转成jpg
    #dcm_image_path = 'C:/Data/001/C+ delay/{}'.format(i)  # 读取dicom文件
    dcm_image_path = "G:\\project\\tool_code\\dcm\\dcm_single\\ct_train_1001_image-210.dcm"
    #output_jpg_path = 'C:/Data/001/C+ delay/{}.jpg'.format(i)
    output_jpg_path = "G:\\project\\tool_code\\dcm\\dcm_single\\ct_train_1001_image-210.jpg"
    ds_array = sitk.ReadImage(dcm_image_path)  # 读取dicom文件的相关信息
    img_array = sitk.GetArrayFromImage(ds_array)  # 获取array
    # SimpleITK读取的图像数据的坐标顺序为zyx，即从多少张切片到单张切片的宽和高，此处我们读取单张，因此img_array的shape
    # 类似于 （1，height，width）的形式
    shape = img_array.shape
    print(shape)
    img_array = np.reshape(img_array, (shape[1], shape[2]))  # 获取array中的height和width
    high = np.max(img_array)
    low = np.min(img_array)
    convert_from_dicom_to_jpg(img_array, low, high, output_jpg_path)  # 调用函数，转换成jpg文件并保存到对应的路径
    #print('正在转换第{}张'.format(i))




