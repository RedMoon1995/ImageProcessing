import nibabel as nib

filepath = "./1.nii.gz"
img = nib.load(filepath)

print(img.dataobj.shape)