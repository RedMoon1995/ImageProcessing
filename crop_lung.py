import pydicom as dcm


img1 = dcm.read_file("G:\\project\\data\\E0001270V3FC01\\1.2.392.200036.9116.2.5.1.48.1215508268.1335413183.210362.dcm")
img2 = dcm.read_file("G:\\project\\data\\R231\\E0001270V3FC01\\1.2.392.200036.9116.2.5.1.48.1215508268.1335413183.210362.dcm")


def segement_dcms(data_dir_name):
    ct_root_path = "/data/zengnanrong/CTDATA/"
    mask_root_path = "/data/zengnanrong/R231/"
    output_root_path = "/data/zengnanrong/LUNG_SEG/"

    path = os.path.join(ct_root_path, data_dir_name)
    for root, dirs, files in os.walk(path):
        for item in files:
            if '.dcm' in item.lower():
                ct_path = os.path.join(root, item)
                mask_path = ct_path.replace(ct_root_path, mask_root_path)

                ct_image = sitk.ReadImage(ct_path)
                ct_image_array = np.squeeze(sitk.GetArrayFromImage(ct_image))
                mask_image = sitk.ReadImage(mask_path)
                mask_image_array = np.squeeze(sitk.GetArrayFromImage(mask_image))

                height = ct_image_array.shape[0]
                width = ct_image_array.shape[1]

                for h in range(height):
                    for w in range(width):
                        if mask_image_array[h][w] == 0:
                            # 将非肺区域置0
                            ct_image_array[h][w] = 0

                seg_path = ct_path.replace(ct_root_path, output_root_path)
                seg_dir = os.path.split(seg_path)[0]
                if not os.path.exists(seg_dir):
                    os.makedirs(seg_dir)

                ct_image_array = np.reshape(ct_image_array, (1, height, width))
                seg_image = sitk.GetImageFromArray(ct_image_array)
                seg_image.CopyInformation(ct_image)
                sitk.WriteImage(seg_image, seg_path)
                logging.info(f'Save result to: {seg_path}')