import os
import SimpleITK as sitk
import cv2
import pydicom
import numpy as np


def nii2png_single(nii_path, IsData = True):
    ori_data = sitk.ReadImage(nii_path)  # 读取一个数据
    data1 = sitk.GetArrayFromImage(ori_data)  # 获取数据的array
    if IsData:  #过滤掉其他无关的组织，标签不需要这步骤
        data1[data1 > 250] = 250
        data1[data1 < -250] = -250
    img_name = os.path.split(nii_path)  #分离文件名
    img_name = img_name[-1]
    img_name = img_name.split('.')
    img_name = img_name[0]
    i = data1.shape[0]
    png_path = './png/single_png'   #图片保存位置
    if not os.path.exists(png_path):
        os.makedirs(png_path)
    for j in range(0, i):   #将每一张切片都转为png
        if IsData:  # 数据
            #归一化
            slice_i = (data1[j, :, :] - data1[j, :, :].min()) / (data1[j, :, :].max() - data1[j, :, :].min()) * 255
            cv2.imwrite("%s/%s-%d.png" % (png_path, img_name, j), slice_i)  #保存
        else:   # 标签
            slice_i = data1[j, :, :] * 122
            cv2.imwrite("%s/%s-%d.png" % (png_path, img_name, j), slice_i)  # 保存


def nii2png(data_path, label_path):
    dataname_list2 = os.listdir(label_path)
    for nii_label in dataname_list2:
        print("process:", nii_label)
        data1 = sitk.ReadImage(os.path.join(data_path, nii_label.replace('segmentation', 'volume'))) # 读取一个数据
        liver_tumor_data = sitk.GetArrayFromImage(data1)  # 获取数据的array
        data2 = sitk.ReadImage(os.path.join(label_path, nii_label))  # 读取一个数据
        liver_tumor_label = sitk.GetArrayFromImage(data2)  # 获取数据的array
        img_name = os.path.split(nii_label.replace('segmentation', 'volume'))     # 分离文件名，用以保存时的文件名前缀
        img_name = img_name[-1]
        img_name = img_name.split('.')
        img_name = img_name[0]
        i = liver_tumor_label.shape[0]
        liver_tumor_data[liver_tumor_data > 250] = 250
        liver_tumor_data[liver_tumor_data < -250] = -250
        outpath = r'./png/data_png'  # 数据保存文件夹
        outpath2 = r'./png/label_png'   # 标签保存文件夹
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        if not os.path.exists(outpath2):
            os.makedirs(outpath2)
        for j in range(0, i):
            if liver_tumor_label[j, :, :].max() > 0:    # 只保存有肝脏的切片
                img1 = (liver_tumor_data[j, :, :] - liver_tumor_data[j, :, :].min()) / (liver_tumor_data[j, :, :].max() - liver_tumor_data[j, :, :].min()) * 255
                img2 = liver_tumor_label[j, :, :] * 122
                cv2.imwrite("%s/%s-%d.png" % (outpath, img_name, j), img1)
                cv2.imwrite("%s/%s-%d.png" % (outpath2, img_name, j), img2)

def dcm2nii_single(dcm_path):
    path = dcm_path
    #save_folder = 'G:\\project\\data\\tem\\dcm'
    save_folder = "G:\\project\\data\\crop_CTdata"
    data = np.zeros((400,200,200))

    img_sitk = sitk.ReadImage("G:\\project\\data\\CTdata\\E0001270V3\\1.2.392.200036.9116.2.5.1.48.1215508268.1335413119.347938.dcm")
    img_spacing = img_sitk.GetSpacing()
    img_origin = img_sitk.GetOrigin()
    img_direction = img_sitk.GetDirection()
    print(img_direction,img_origin,img_spacing)

    for root, dirs, files in os.walk(path):
        for j in range(0,len(files)-1):
            #ct_path = os.path.join(root, "ct_test_2001_image-%s.dcm"% str(j+1))
            ct_path = os.path.join(root,str(j + 100)+".dcm")
            #print(ct_path)
            ct_image = sitk.ReadImage(ct_path)  # 读取dcm图片
            ct_image_array = sitk.GetArrayFromImage(ct_image)
            #print(ct_image_array.shape)
            #data[j:,:] = np.flip(ct_image_array[0,:,:],axis=0)
            data[j:, :] = ct_image_array[0, :, :]

        print(data.shape)
        data = np.array(data)
        data = sitk.GetImageFromArray(data)

        space = np.array([1.0,1.0,0.5])

        data.SetDirection(img_direction)
        data.SetSpacing(space)
        data.SetOrigin(img_origin)

        sitk.WriteImage(data, save_folder+'\\1270_denoise.nii.gz')
        print('Save result to: %s' % save_folder)

                


def nii2dcm_single(nii_path, IsData = True):
    save_folder = 'G:\\project\\data\\tem\\dcm'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    ori_data = sitk.ReadImage(nii_path)  # 读取一个数据
    data1 = sitk.GetArrayFromImage(ori_data)  # 获取数据的array
    if IsData:  # 过滤掉其他无关的组织，标签不需要这步骤
        data1[data1 > 250] = 250
        data1[data1 < -250] = -250
    img_name = os.path.split(nii_path)  #分离文件名
    img_name = img_name[-1]
    img_name = img_name.split('.')
    img_name = img_name[0]
    i = data1.shape[0]
    print(i)
    # 关键部分
    castFilter = sitk.CastImageFilter()
    castFilter.SetOutputPixelType(sitk.sitkInt16)
    for j in range(0, i):   #将每一张切片都转为png
        if IsData:  # 数据
            slice_i = data1[j, :, :]
            data_img = sitk.GetImageFromArray(slice_i)
            # Convert floating type image (imgSmooth) to int type (imgFiltered)
            data_img = castFilter.Execute(data_img)

            sitk.WriteImage(data_img, "%s/%s-%d.dcm" % (save_folder, img_name, j+1))
        else:   # 标签
            #slice_i = data1[j, :, :] * 122
            slice_i = np.flip(data1[j, :, :],axis=0)
            label_img = sitk.GetImageFromArray(slice_i)
            # Convert floating type image (imgSmooth) to int type (imgFiltered)
            label_img = castFilter.Execute(label_img)
            label_img.SetMetaData("0020|0013", str(j+1))
            label_img.SetMetaData("0010|1010", "30")  # Patient's Age
            label_img.SetMetaData("0028|1052", "-1024.0")  # Rescale Intercept
            label_img.SetMetaData("0028|1053", "1.0")  # Rescale Slope
            sitk.WriteImage(label_img, "%s/%s-%d.dcm" % (save_folder, img_name, j+1))


def nii2dcm(data_path, lable_path, IsTrain = False):
    save_folder = './dcm'
    nii_list = os.listdir(lable_path)
    for nii_label in nii_list:
        print("process:", nii_label)
        data1 = sitk.ReadImage(os.path.join(lable_path, nii_label)) # 读取一个数据
        liver_tumor_label = sitk.GetArrayFromImage(data1)  # 获取数据的array
        print(np.unique(liver_tumor_label))
        data2 = sitk.ReadImage(os.path.join(data_path, nii_label.replace('segmentation', 'volume')))  # 读取一个数据
        liver_tumor_data = sitk.GetArrayFromImage(data2)  # 获取数据的array
        slice_num = liver_tumor_label.shape[0]     # 获取切片数量
        if IsTrain:
            save_img = save_folder+'/train'
        else:
            save_img = save_folder + '/val'
        label_path = save_folder+'/label'     # 设置保存路径
        if not os.path.exists(save_img):      # 判断文件目录是否存在，不存在则创建
            os.makedirs(save_img)
        if not os.path.exists(label_path):
            os.makedirs(label_path)

        img_name = os.path.split(nii_label.replace('segmentation', 'volume'))     # 分离文件名，用以保存时的文件名前缀
        img_name = img_name[-1]
        img_name = img_name.split('.')
        img_name = img_name[0]

        for i in range(0, slice_num):
            # 关键部分
            if liver_tumor_label[i, :, :].max() > 0:    # 肝脏标签图片
                label_img = sitk.GetImageFromArray(liver_tumor_label[i, :, :] * 122)
                data_img = sitk.GetImageFromArray(liver_tumor_data[i, :, :])
                castFilter = sitk.CastImageFilter()
                castFilter.SetOutputPixelType(sitk.sitkInt16)
                # Convert floating type image (imgSmooth) to int type (imgFiltered)
                label_img = castFilter.Execute(label_img)
                data_img = castFilter.Execute(data_img)
                sitk.WriteImage(label_img, "%s/%s-%d.dcm" % (label_path, img_name, i))
                sitk.WriteImage(data_img, "%s/%s-%d.dcm" % (save_img, img_name, i))


def dcm2png_single(dcm_path): #这个不好用，用dcm2png.py
    save_pa = r'./png/single'
    if not os.path.exists(save_pa):
        os.makedirs(save_pa)
    img_name = os.path.split(dcm_path.replace('.dcm', '.jpg'))  # 替换后缀名并分离路径
    img_name = img_name[-1]
    ds = pydicom.read_file(dcm_path, force=True)       # 注意这里，强制读取
    img = ds.pixel_array  # 提取图像信息
    cv2.imwrite(os.path.join(save_pa, img_name), img)


def dcm2png(dcm_path, label_path):
    labellist = os.listdir(label_path)
    save_data = r'./png/dcm_png_data'
    save_lab = r'./png/dcm_png_lab'
    if not os.path.exists(save_data):
        os.makedirs(save_data)
    if not os.path.exists(save_lab):
        os.makedirs(save_lab)
    for lab in labellist:
        print('process', lab)
        ds = pydicom.read_file(os.path.join(label_path, lab), force=True)   # 注意这里，强制读取
        label = ds.pixel_array  # 提取图像信息
        ds1 = pydicom.read_file(os.path.join(dcm_path, lab), force=True)
        img = ds1.pixel_array  # 提取图像信息
        cv2.imwrite(os.path.join(save_data, lab.replace('.dcm', '.png')), img)
        cv2.imwrite(os.path.join(save_lab, lab.replace('.dcm', '.png')), label)


if __name__ == "__main__":
    # # 单个nii文件转png
    # nii_single = r'G:\Python\liversegment\ImageResource\ImageTraning\data\volume-0.nii'
    # nii2png_single(nii_single, IsData=False)
    # # 按照标签提取切片，只保存有肝脏的切片
    # niipath = r'G:\Python\liversegment\ImageResource\ImageTraning\data'
    # labpath = r'G:\Python\liversegment\ImageResource\ImageTraning\label'
    # nii2png(niipath, labpath)
    #
    # # 单个nii转dcm
    # nii2dcm_single(nii_single, True)
    # # 批量nii转dcm
    # nii2dcm(niipath, labpath, IsTrain=True)
    #
    # # 单个dcm转png
    # dcm_single = r'F:\Liver\Unet_4_23\dcm\train\volume-0-55.dcm'
    # dcm2png_single(dcm_single)
    # # 批量dcm转png
    # dcm_pa = r'F:\Liver\Unet_4_23\dcm\train'
    # lab_dcm = r'F:\Liver\Unet_4_23\dcm\label'
    # dcm2png(dcm_pa, lab_dcm)


    #nii2dcm_single("G:\\project\\data\\MMWHS_test_data\\test_data\\ct_test_2001_image.nii.gz",False)
    #dcm2nii_single("G:\\project\\data\\tem\\denoise")
    dcm2nii_single("G:\\project\\data\\crop_CTdata\\1270denoise")
    #dcm2png_single("G:\\project\\tool_code\\dcm\\dcm_single\\ct_train_1001_image-173.dcm")
    #dcm2png_single("G:\\project\\data\\CTdata\\E0001001V3\\1.2.392.200036.9116.2.5.1.48.1215508268.1316403078.758536.dcm")