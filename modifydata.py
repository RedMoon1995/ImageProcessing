import nibabel as nib
from glob import glob
import numpy as np
import os

testdata_dir = 'D:\\result\\hybrid_AG_5RVBC\\pred_data_32w_a'
labeling_dir = 'D:\\result\\hybrid_AG_5RVBC\\pred_data_32w_b'

test_list = glob('{}/*.nii.gz'.format(testdata_dir))
print(test_list)
test_list.sort()

for k in range(0, len(test_list)):
    sort = k+1
    # load the volume
    vol_file = nib.load(test_list[k])
    ref_affine = vol_file.affine
    # get volume data
    vol_data = vol_file.get_data().copy()

    #modify
    composed_label = np.zeros(vol_data.shape, dtype='int16')
    composed_label[vol_data == 1] = 600
    composed_label = composed_label.astype('int16')

    #save
    labeling_path = os.path.join(labeling_dir, ('ct_test_' + str(2000 + sort) + '_label.nii.gz'))
    labeling_vol = nib.Nifti1Image(composed_label, ref_affine)
    nib.save(labeling_vol, labeling_path)
