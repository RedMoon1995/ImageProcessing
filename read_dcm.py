import pydicom 
 
filepath = "./"
data = pydicom.dcmread(filepath+'1.2.392.200036.9116.2.5.1.48.1215508268.1316403075.674857.dcm') #读取一张dcm文件\
print(data.data_element)