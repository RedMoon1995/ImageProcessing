import pydicom as dicom

#ds = dicom.read_file('G:\\project\\data\\crop_CTdata\\E0001270V3crop\\1.2.392.200036.9116.2.5.1.48.1215508268.1335413123.433624.dcm')
#ds = dicom.read_file('G:\\project\\data\\CTdata\\E0001270V3\\1.2.392.200036.9116.2.5.1.48.1215508268.1335413123.433624.dcm')
#ds = dicom.read_file('G:\\project\\data\\lixiong200508-1297836\\lixiong200508-1297836\\1.3.12.2.1107.5.1.4.49732.30000020042006051217100111653.dcm')
#ds = dicom.read_file("G:\\project\\data\\Patients\\Structure_CardiacSegmentation\\Patients\\AFre\\IM-0002-0021_an.dcm")


#ds = dicom.read_file("G:\\project\\data\\CTdata\\denoise\\E0001270V3denoise\\1.2.392.200036.9116.2.5.1.48.1215508268.1335413125.15630.dcm")
ds = dicom.read_file("G:\\project\\tool_code\\dcm\\dcm_single\\ct_train_1001_image-3.dcm")

#print (ds)
#print(ds.StudyInstanceUID)
print(ds.InstanceNumber)